import pandas as pd
import json
import os
import joblib
from sklearn.metrics import accuracy_score, f1_score, classification_report, confusion_matrix
from data_utils import build_dataset

def main():
    print("Building evaluation dataset (VALIDATION)...")
    val_df = build_dataset("data/twcs.csv", "data/splits/amazon_val.csv")
    
    X_msg = val_df['message_only']
    X_ctx = val_df['context_aware']
    y_true = val_df['label']
    tweet_ids = val_df['tweet_id']
    
    print(f"Evaluating on {len(val_df)} weakly labelled validation examples.")
    
    # 1. Majority Class Baseline
    with open("models/majority_baseline.json", "r") as f:
        maj = json.load(f)["majority_class"]
    y_pred_maj = [maj] * len(y_true)
    
    # 2. TF-IDF Message Only
    vec_msg = joblib.load("models/vec_msg.joblib")
    clf_msg = joblib.load("models/clf_msg.joblib")
    X_msg_tfidf = vec_msg.transform(X_msg)
    y_pred_msg = clf_msg.predict(X_msg_tfidf)
    
    # 3. TF-IDF Context Aware
    vec_ctx = joblib.load("models/vec_ctx.joblib")
    clf_ctx = joblib.load("models/clf_ctx.joblib")
    X_ctx_tfidf = vec_ctx.transform(X_ctx)
    y_pred_ctx = clf_ctx.predict(X_ctx_tfidf)
    
    # METRICS
    def get_metrics(y_t, y_p):
        acc = accuracy_score(y_t, y_p)
        macro_f1 = f1_score(y_t, y_p, average='macro')
        weighted_f1 = f1_score(y_t, y_p, average='weighted')
        return acc, macro_f1, weighted_f1
        
    acc_maj, m_f1_maj, w_f1_maj = get_metrics(y_true, y_pred_maj)
    acc_msg, m_f1_msg, w_f1_msg = get_metrics(y_true, y_pred_msg)
    acc_ctx, m_f1_ctx, w_f1_ctx = get_metrics(y_true, y_pred_ctx)
    
    # Context Ablation Report
    os.makedirs("reports", exist_ok=True)
    with open("reports/context_ablation.md", "w") as f:
        f.write("# Context Ablation Study\n\n")
        f.write("This report compares the performance of the intent classifier using only the target message versus including the conversation context (up to 3 preceding messages).\n\n")
        
        f.write("## Baseline Metrics\n")
        f.write("| Metric | Majority Class | TF-IDF (Message Only) | TF-IDF (Context Aware) |\n")
        f.write("|--------|----------------|-----------------------|------------------------|\n")
        f.write(f"| Accuracy | {acc_maj:.4f} | {acc_msg:.4f} | {acc_ctx:.4f} |\n")
        f.write(f"| Macro F1 | {m_f1_maj:.4f} | {m_f1_msg:.4f} | {m_f1_ctx:.4f} |\n")
        f.write(f"| Weighted F1 | {w_f1_maj:.4f} | {w_f1_msg:.4f} | {w_f1_ctx:.4f} |\n\n")
        
        f.write("## Intent Distribution\n")
        for k, v in y_true.value_counts().items():
            f.write(f"- {k}: {v}\n")
            
        f.write("\n## Per-Intent Metrics (Message Only)\n")
        f.write("```text\n")
        f.write(classification_report(y_true, y_pred_msg))
        f.write("\n```\n\n")
        
        f.write("## Per-Intent Metrics (Context Aware)\n")
        f.write("```text\n")
        f.write(classification_report(y_true, y_pred_ctx))
        f.write("\n```\n\n")
        
        f.write("## Interpretation\n")
        if m_f1_ctx > m_f1_msg:
            f.write("Adding conversation context **improved** performance overall. This is likely because many tweets are conversational fragments (e.g. 'Done', 'Here is the info') where the actual intent is established in earlier messages. By including the context, the classifier can map these fragments to the correct support workflow.\n")
        else:
            f.write("Adding conversation context **did not improve** performance. This could be due to the naive TF-IDF representation treating context text as identical to the target message text, causing the classifier to overweight words from the brand's prompts or previous unrelated customer complaints. An LLM capable of distinguishing speaker roles might fare better.\n")
            
    # Error Analysis
    errors = []
    # Let's compare where context failed vs message failed
    for i in range(len(y_true)):
        true_label = y_true.iloc[i]
        pred_msg = y_pred_msg[i]
        pred_ctx = y_pred_ctx[i]
        msg_text = X_msg.iloc[i]
        ctx_text = X_ctx.iloc[i]
        
        if pred_msg != true_label or pred_ctx != true_label:
            errors.append({
                "tweet_id": int(tweet_ids.iloc[i]),
                "context": ctx_text,
                "target_message": msg_text,
                "true_label": true_label,
                "predicted_message_only": pred_msg,
                "predicted_context_aware": pred_ctx,
                "hypothesis": "Model struggled with overlapping keywords or lacked sufficient context/reasoning capability."
            })
            
    with open("reports/error_analysis.json", "w") as f:
        json.dump(errors[:100], f, indent=2) # Save top 100 errors to avoid massive files
        
    print("Evaluation complete. Results saved to reports/context_ablation.md and reports/error_analysis.json")

if __name__ == "__main__":
    main()
