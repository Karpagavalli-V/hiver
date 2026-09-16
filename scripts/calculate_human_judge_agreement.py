import os
import sys
import pandas as pd
from typing import Dict
from src.evaluation.human_judge_agreement import calculate_weighted_kappa, calculate_cohen_kappa

CSV_PATH = "data/human_judge/human_judge_20.csv"
REPORT_PATH = "reports/human_judge_agreement.md"

DIMENSIONS = ["relevance", "groundedness", "helpfulness", "safety", "tone"]

def calculate_agreement_metrics(df: pd.DataFrame) -> Dict[str, Dict]:
    results = {}
    
    for dim in DIMENSIONS:
        h_col = f"human_{dim}"
        j_col = f"judge_{dim}"
        
        h_scores = [int(float(x)) for x in df[h_col].dropna()]
        j_scores = [int(float(x)) for x in df[j_col].dropna()]
        
        if len(h_scores) != len(j_scores) or len(h_scores) == 0:
            results[dim] = {
                "human_mean": 0.0,
                "judge_mean": 0.0,
                "cohen_kappa": 0.0,
                "weighted_kappa": 0.0
            }
            continue
            
        h_mean = sum(h_scores) / len(h_scores)
        j_mean = sum(j_scores) / len(j_scores)
        cohen = calculate_cohen_kappa(h_scores, j_scores)
        qwk = calculate_weighted_kappa(h_scores, j_scores)
        
        results[dim] = {
            "human_mean": round(h_mean, 2),
            "judge_mean": round(j_mean, 2),
            "cohen_kappa": round(cohen, 4),
            "weighted_kappa": round(qwk, 4)
        }
        
    return results

def generate_report(df: pd.DataFrame, metrics: Dict[str, Dict], report_path: str = REPORT_PATH):
    n = len(df)
    macro_qwk = sum(m["weighted_kappa"] for m in metrics.values()) / len(metrics) if metrics else 0.0
    macro_cohen = sum(m["cohen_kappa"] for m in metrics.values()) / len(metrics) if metrics else 0.0
    
    md = f"""# LLM-Judge vs. Human Agreement Report (20-Example Validation Sample)

## 1. Summary
- **Sample Size**: {n} examples
- **Sampling Methodology**: Stratified deterministic sampling (seed=42) across 9 intent classes and 2 escalation states (`AUTO-HANDLE` and `ESCALATE`).
- **Rating Scale**: 1 to 5 integer ordinal scale per dimension (1 = Poor, 5 = Excellent).
- **Macro-Averaged Quadratic Weighted Kappa (QWK)**: **{macro_qwk:.4f}**
- **Macro-Averaged Cohen's Kappa**: **{macro_cohen:.4f}**

---

## 2. Dimension-Wise Agreement Results

| Dimension | Human Mean Score | LLM Judge Mean Score | Cohen's Kappa (Exact) | Quadratic Weighted Kappa (QWK) |
| :--- | :---: | :---: | :---: | :---: |
"""
    for dim, m in metrics.items():
        md += f"| **{dim.capitalize()}** | {m['human_mean']:.2f} | {m['judge_mean']:.2f} | {m['cohen_kappa']:.4f} | **{m['weighted_kappa']:.4f}** |\n"

    md += f"""
---

## 3. Methodological & Statistical Notes

> [!IMPORTANT]
> **Sample Size Limitation Notice**:
> This 20-example evaluation sample serves as a focused human-validation benchmark for LLM judge agreement required by the Hiver assignment. It provides a measure of inter-rater reliability, but should **not** be treated as a statistically high-powered representation of the full 200-example Phase 5B dataset.

1. **Quadratic Weighted Kappa (QWK)** is the primary metric because 1–5 ratings are ordinal; small discrepancies (e.g. 4 vs 5) receive smaller penalties than large discrepancies (e.g. 1 vs 5).
2. **Unbiased Annotation**: Human ratings were performed independently without displaying LLM judge scores to prevent anchoring bias.
"""

    os.makedirs(os.path.dirname(report_path), exist_ok=True)
    with open(report_path, "w", encoding="utf-8") as f:
        f.write(md)
    print(f"Agreement report successfully written to {report_path}.")

def main():
    if not os.path.exists(CSV_PATH):
        print(f"Error: {CSV_PATH} does not exist.")
        sys.exit(1)
        
    df = pd.read_csv(CSV_PATH)
    
    # Check if human ratings exist
    if df["human_relevance"].isna().all():
        print("Human ratings are currently EMPTY. Run 'python scripts/human_judge_20.py' to enter ratings first.")
        sys.exit(0)
        
    metrics = calculate_agreement_metrics(df)
    generate_report(df, metrics)

if __name__ == "__main__":
    main()
