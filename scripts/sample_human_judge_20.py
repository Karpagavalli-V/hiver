import os
import json
import csv
import random
from typing import Dict, List
import pandas as pd

def load_evaluation_results(filepath: str = "reports/evaluation_results.json") -> List[Dict]:
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data.get("results", [])

def load_golden_set_context(filepath: str = "data/golden_set/golden_set_final.csv") -> Dict[str, str]:
    if not os.path.exists(filepath):
        return {}
    df = pd.read_csv(filepath)
    context_map = {}
    for _, row in df.iterrows():
        gid = str(row.get("golden_id", "")).strip()
        ctx = str(row.get("conversation_context", "")).strip()
        context_map[gid] = ctx if ctx and ctx != "nan" and ctx != "[]" else ""
    return context_map

def perform_stratified_sampling(results: List[Dict], target_n: int = 20, seed: int = 42) -> List[Dict]:
    random.seed(seed)
    
    # Group by (pred_intent, pred_escalation)
    strata: Dict[str, List[Dict]] = {}
    for item in results:
        intent = item.get("pred_intent", "OTHER")
        esc = item.get("true_escalation", "AUTO-HANDLE")
        key = f"{intent}||{esc}"
        if key not in strata:
            strata[key] = []
        strata[key].append(item)
        
    sampled: List[Dict] = []
    
    # First pass: pick at least 1 item from each stratum
    strata_keys = sorted(list(strata.keys()))
    for key in strata_keys:
        items = strata[key]
        random.shuffle(items)
        if items and len(sampled) < target_n:
            sampled.append(items.pop(0))
            
    # Second pass: fill remaining quota proportionally from largest strata
    remaining_pool = []
    for items in strata.values():
        remaining_pool.extend(items)
    random.shuffle(remaining_pool)
    
    while len(sampled) < target_n and remaining_pool:
        item = remaining_pool.pop(0)
        if item not in sampled:
            sampled.append(item)
            
    # Sort deterministically by golden_id
    sampled.sort(key=lambda x: x.get("golden_id", ""))
    return sampled

def create_human_judge_csv(sampled: List[Dict], context_map: Dict[str, str], output_csv: str = "data/human_judge/human_judge_20.csv"):
    os.makedirs(os.path.dirname(output_csv), exist_ok=True)
    
    fieldnames = [
        "golden_id",
        "customer_message",
        "predicted_intent",
        "predicted_escalation",
        "generated_reply",
        "retrieved_evidence_summary",
        "human_relevance",
        "human_groundedness",
        "human_helpfulness",
        "human_safety",
        "human_tone",
        "human_notes",
        "judge_relevance",
        "judge_groundedness",
        "judge_helpfulness",
        "judge_safety",
        "judge_tone",
        "judge_overall"
    ]
    
    rows = []
    for item in sampled:
        gid = item.get("golden_id", "")
        ctx = context_map.get(gid, "")
        judge_scores = item.get("judge_scores", {})
        
        row = {
            "golden_id": gid,
            "customer_message": item.get("customer_message", ""),
            "predicted_intent": item.get("pred_intent", ""),
            "predicted_escalation": item.get("pred_escalation", ""),
            "generated_reply": item.get("generated_reply", ""),
            "retrieved_evidence_summary": ctx[:300] if ctx else "None available",
            "human_relevance": "",
            "human_groundedness": "",
            "human_helpfulness": "",
            "human_safety": "",
            "human_tone": "",
            "human_notes": "",
            "judge_relevance": judge_scores.get("relevance", ""),
            "judge_groundedness": judge_scores.get("groundedness", ""),
            "judge_helpfulness": judge_scores.get("helpfulness", ""),
            "judge_safety": judge_scores.get("safety", ""),
            "judge_tone": judge_scores.get("tone", ""),
            "judge_overall": judge_scores.get("overall_score", "")
        }
        rows.append(row)
        
    with open(output_csv, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
        
    print(f"Successfully created {output_csv} with {len(rows)} sampled rows.")

def save_metadata(sampled: List[Dict], output_meta: str = "data/human_judge/sample_20_metadata.json", seed: int = 42):
    intent_counts = {}
    esc_counts = {}
    true_esc_counts = {}
    gids = []
    
    for item in sampled:
        gid = item.get("golden_id", "")
        intent = item.get("pred_intent", "")
        esc = item.get("pred_escalation", "")
        true_esc = item.get("true_escalation", "")
        gids.append(gid)
        intent_counts[intent] = intent_counts.get(intent, 0) + 1
        esc_counts[esc] = esc_counts.get(esc, 0) + 1
        true_esc_counts[true_esc] = true_esc_counts.get(true_esc, 0) + 1
        
    meta = {
        "sample_size": len(sampled),
        "random_seed": seed,
        "sampling_strategy": "stratified_by_intent_and_true_escalation",
        "intent_distribution": intent_counts,
        "predicted_escalation_distribution": esc_counts,
        "true_escalation_distribution": true_esc_counts,
        "sampled_golden_ids": gids
    }
    
    with open(output_meta, "w", encoding="utf-8") as f:
        json.dump(meta, f, indent=2)
    print(f"Saved sampling metadata to {output_meta}.")

def main():
    results = load_evaluation_results()
    context_map = load_golden_set_context()
    sampled = perform_stratified_sampling(results, target_n=20, seed=42)
    create_human_judge_csv(sampled, context_map)
    save_metadata(sampled)

if __name__ == "__main__":
    main()
