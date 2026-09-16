import os
import json
from typing import List, Dict

def generate_failure_analysis(results: List[Dict], output_path: str = "reports/failure_analysis.md"):
    """
    Generates a failure analysis report based on evaluation results.
    """
    intent_mismatches = []
    escalation_mismatches = []
    low_judge_scores = []
    
    for r in results:
        golden_id = r.get("golden_id", "Unknown")
        customer_message = r.get("customer_message", "")
        
        # Intent
        true_intent = r.get("true_intent")
        pred_intent = r.get("pred_intent")
        if pred_intent and true_intent and pred_intent != true_intent:
            intent_mismatches.append({
                "id": golden_id,
                "msg": customer_message,
                "true": true_intent,
                "pred": pred_intent
            })
            
        # Escalation
        true_esc = r.get("true_escalation")
        pred_esc = r.get("pred_escalation")
        if pred_esc and true_esc and pred_esc != true_esc:
            escalation_mismatches.append({
                "id": golden_id,
                "msg": customer_message,
                "true": true_esc,
                "pred": pred_esc
            })
            
        # Judge
        judge = r.get("judge_scores")
        if judge:
            overall = judge.get("overall_score", 5.0)
            safety = judge.get("safety", 5)
            if overall < 3.0 or safety < 4:
                low_judge_scores.append({
                    "id": golden_id,
                    "msg": customer_message,
                    "reply": r.get("generated_reply", ""),
                    "scores": judge
                })

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("# Phase 5B: Failure Analysis Report\n\n")
        f.write("This report automatically highlights examples where the system's predictions diverged from the Golden Set labels or received low LLM-judge scores.\n\n")
        
        f.write("## 1. Intent Classification Mismatches\n")
        f.write(f"Total intent failures: {len(intent_mismatches)}\n\n")
        for m in intent_mismatches[:10]:
            f.write(f"**ID: {m['id']}**\n")
            f.write(f"- Message: {m['msg']}\n")
            f.write(f"- True Intent: `{m['true']}` | Predicted: `{m['pred']}`\n")
            f.write(f"- Hypothesis: Ambiguous vocabulary or missing critical context.\n\n")
            
        f.write("## 2. Escalation Decision Mismatches\n")
        f.write(f"Total escalation failures: {len(escalation_mismatches)}\n\n")
        for m in escalation_mismatches[:10]:
            f.write(f"**ID: {m['id']}**\n")
            f.write(f"- Message: {m['msg']}\n")
            f.write(f"- True Decision: `{m['true']}` | Predicted: `{m['pred']}`\n")
            f.write(f"- Hypothesis: Threshold tuning required or safety policy overly aggressive/lenient.\n\n")
            
        f.write("## 3. Low Judge Scores (Reply Quality)\n")
        f.write(f"Total low-scoring replies: {len(low_judge_scores)}\n\n")
        for m in low_judge_scores[:10]:
            f.write(f"**ID: {m['id']}**\n")
            f.write(f"- Message: {m['msg']}\n")
            f.write(f"- Generated Reply: {m['reply']}\n")
            f.write(f"- Judge Scores: Overall: {m['scores'].get('overall_score')}, Safety: {m['scores'].get('safety')}, Relevance: {m['scores'].get('relevance')}\n")
            f.write(f"- Rationale: {m['scores'].get('rationale')}\n")
            f.write(f"- Hypothesis: Insufficient retrieved evidence caused a safe fallback or a hallucinated attempt.\n\n")

    return {
        "intent_failures": len(intent_mismatches),
        "escalation_failures": len(escalation_mismatches),
        "low_judge_scores": len(low_judge_scores)
    }
