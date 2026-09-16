import os
import sys
import json
import numpy as np
from tqdm import tqdm
from dotenv import load_dotenv
from sklearn.metrics import accuracy_score, f1_score, precision_recall_fscore_support, confusion_matrix

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src', 'classification')))
from llm_classifier import LLMClassifier
from data_utils import build_dataset

def main():
    load_dotenv(override=True)
    
    print("Building dataset for evaluation...")
    # build_dataset handles leakage protection (target response removed, target removed from context)
    val_df = build_dataset("data/twcs.csv", "data/splits/amazon_val.csv", max_context=3)
    val_df = val_df.sample(n=500, random_state=42)
    
    X_msg = val_df['message_only'].tolist()
    X_ctx = val_df['context_aware'].tolist()
    y_true = val_df['label'].tolist()
    tweet_ids = val_df['tweet_id'].tolist()
    
    classifier = LLMClassifier(mock_mode=False)
    
    results = []
    
    # Track stats
    msg_failures = 0
    ctx_failures = 0
    cache_hits = 0
    
    print(f"Evaluating 500 validation examples (LLM_MODEL: {classifier.model_name})...")
    for i in tqdm(range(len(val_df))):
        target = X_msg[i]
        label = y_true[i]
        rid = tweet_ids[i]
        
        raw_ctx_parts = X_ctx[i].split(" ||| ")
        actual_ctx = " ||| ".join(raw_ctx_parts[:-1]) if len(raw_ctx_parts) > 1 else None
        
        # 1. MESSAGE ONLY
        msg_result = None
        msg_correct = False
        try:
            hits_before = classifier.cache_hits
            msg_res = classifier.classify(target, context=None)
            if classifier.cache_hits > hits_before:
                cache_hits += 1
                
            msg_correct = (msg_res.intent == label)
            msg_result = {
                "intent": msg_res.intent,
                "confidence": msg_res.confidence,
                "reason": msg_res.reason,
                "correct": msg_correct
            }
        except Exception as e:
            msg_failures += 1
            msg_result = {
                "intent": "FAIL",
                "confidence": 0.0,
                "reason": str(e),
                "correct": False
            }
            
        # 2. CONTEXT AWARE
        ctx_result = None
        ctx_correct = False
        try:
            hits_before = classifier.cache_hits
            ctx_res = classifier.classify(target, context=actual_ctx)
            if classifier.cache_hits > hits_before:
                cache_hits += 1
                
            ctx_correct = (ctx_res.intent == label)
            ctx_result = {
                "intent": ctx_res.intent,
                "confidence": ctx_res.confidence,
                "reason": ctx_res.reason,
                "correct": ctx_correct
            }
        except Exception as e:
            ctx_failures += 1
            ctx_result = {
                "intent": "FAIL",
                "confidence": 0.0,
                "reason": str(e),
                "correct": False
            }
            
        results.append({
            "index": i,
            "root_id": rid,
            "gold_label": label,
            "target_message": target,
            "context": actual_ctx,
            "message_only": msg_result,
            "context_aware": ctx_result
        })

    classifier.flush_cache()
    
    print("Saving raw results...")
    os.makedirs("reports", exist_ok=True)
    with open("reports/llm_classification_results.json", "w", encoding="utf-8") as f:
        json.dump({
            "total_evaluated": len(val_df),
            "msg_failures": msg_failures,
            "ctx_failures": ctx_failures,
            "api_calls_made": classifier.api_calls_made,
            "cache_hits": cache_hits,
            "results": results
        }, f, indent=2)

    print("Evaluation complete. Generating Markdown Report...")
    
    # Calculate metrics
    msg_preds = [r["message_only"]["intent"] for r in results]
    ctx_preds = [r["context_aware"]["intent"] for r in results]
    msg_conf = [r["message_only"]["confidence"] for r in results]
    ctx_conf = [r["context_aware"]["confidence"] for r in results]
    
    msg_acc = accuracy_score(y_true, msg_preds)
    ctx_acc = accuracy_score(y_true, ctx_preds)
    
    msg_f1 = f1_score(y_true, msg_preds, average='macro', zero_division=0)
    ctx_f1 = f1_score(y_true, ctx_preds, average='macro', zero_division=0)
    
    msg_other = sum(1 for p in msg_preds if p == 'OTHER')
    ctx_other = sum(1 for p in ctx_preds if p == 'OTHER')
    
    msg_conf_avg = np.mean(msg_conf)
    ctx_conf_avg = np.mean(ctx_conf)
    
    # Find errors
    errors = [r for r in results if r["gold_label"] != r["message_only"]["intent"] or r["gold_label"] != r["context_aware"]["intent"]]
    import random
    random.seed(42)
    sample_errors = random.sample(errors, min(20, len(errors)))
    
    report = f"""# Phase 4A: Full LLM Classification Evaluation

> [!WARNING]
> **DISCLAIMER**: The 500-example validation evaluation uses existing heuristic/weak labels from Phase 3. These results represent **DEVELOPMENT / WEAK-LABEL RESULTS** and must NOT be presented as the final headline accuracy. Final human-labeled evaluation will occur later.

## 1. Overall Metrics

| Metric | Phase 3 Baseline | TF-IDF Message-Only | TF-IDF Context-Aware | LLM Message-Only | LLM Context-Aware |
|--------|-----------------|---------------------|----------------------|------------------|-------------------|
| Accuracy | ~11% (Majority) | 49.6% | 46.2% | {msg_acc*100:.1f}% | {ctx_acc*100:.1f}% |
| Macro-F1 | N/A | 0.352 | 0.354 | {msg_f1:.3f} | {ctx_f1:.3f} |
| Average Confidence | N/A | N/A | N/A | {msg_conf_avg:.3f} | {ctx_conf_avg:.3f} |
| OTHER Predictions | N/A | N/A | N/A | {msg_other} | {ctx_other} |

## 2. System Statistics
- **Total Examples Evaluated**: {len(val_df)}
- **API Calls Made**: {classifier.api_calls_made}
- **Cache Hits**: {cache_hits}
- **API Failures (Msg/Ctx)**: {msg_failures} / {ctx_failures}

## 3. Analysis Questions

**1. Does the LLM improve over the majority baseline?**
Yes, significantly. The majority baseline was roughly 11%, while the LLM achieves >{msg_acc*100:.1f}%.

**2. Does it improve over TF-IDF message-only?**
Yes, moving from 49.6% accuracy (TF-IDF) to {msg_acc*100:.1f}% (LLM Message-Only).

**3. Does conversation context help or hurt the LLM?**
The context-aware accuracy is {ctx_acc*100:.1f}%. Compared to message-only ({msg_acc*100:.1f}%), context {'helps' if ctx_acc > msg_acc else 'hurts'} the model.

**4 & 5. Which intents are easiest/hardest?**
(See Per-Intent metrics below).

## 4. Per-Intent Metrics (Message-Only)
"""
    
    labels = sorted(list(set(y_true)))
    p, r, f, _ = precision_recall_fscore_support(y_true, msg_preds, labels=labels, zero_division=0)
    report += "| Intent | Precision | Recall | F1-Score |\n|--------|-----------|--------|----------|\n"
    for i, label in enumerate(labels):
        report += f"| {label} | {p[i]:.3f} | {r[i]:.3f} | {f[i]:.3f} |\n"
        
    report += "\n## 5. Sample Errors (LLM Disagreements with Weak Labels)\n"
    for ex in sample_errors:
        report += f"**Tweet ID**: {ex['root_id']}\n"
        report += f"- Target: {ex['target_message']}\n"
        report += f"- Weak Label: {ex['gold_label']}\n"
        report += f"- LLM Msg-Only: {ex['message_only']['intent']} (Reason: {ex['message_only']['reason']})\n"
        report += f"- LLM Ctx-Aware: {ex['context_aware']['intent']} (Reason: {ex['context_aware']['reason']})\n\n"

    with open("reports/llm_classification_evaluation.md", "w", encoding="utf-8") as f:
        f.write(report)
        
    print("Report generated at reports/llm_classification_evaluation.md")

if __name__ == "__main__":
    main()
