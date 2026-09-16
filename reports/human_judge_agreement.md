# LLM-Judge vs. Human Agreement Report (20-Example Validation Sample)

## 1. Summary
- **Sample Size**: 20 examples
- **Sampling Methodology**: Stratified deterministic sampling (seed=42) across 9 intent classes and 2 escalation states (`AUTO-HANDLE` and `ESCALATE`).
- **Rating Scale**: 1 to 5 integer ordinal scale per dimension (1 = Poor, 5 = Excellent).
- **Macro-Averaged Quadratic Weighted Kappa (QWK)**: **0.3038**
- **Macro-Averaged Cohen's Kappa**: **0.1949**

---

## 2. Dimension-Wise Agreement Results

| Dimension | Human Mean Score | LLM Judge Mean Score | Cohen's Kappa (Exact) | Quadratic Weighted Kappa (QWK) |
| :--- | :---: | :---: | :---: | :---: |
| **Relevance** | 4.35 | 4.55 | -0.0667 | **0.0244** |
| **Groundedness** | 3.85 | 3.50 | 0.0783 | **0.1875** |
| **Helpfulness** | 3.70 | 4.20 | 0.0000 | **0.3443** |
| **Safety** | 5.00 | 5.00 | 1.0000 | **1.0000** |
| **Tone** | 4.15 | 4.75 | -0.0370 | **-0.0370** |

---

## 3. Methodological & Statistical Notes

> [!IMPORTANT]
> **Sample Size Limitation Notice**:
> This 20-example evaluation sample serves as a focused human-validation benchmark for LLM judge agreement required by the Hiver assignment. It provides a measure of inter-rater reliability, but should **not** be treated as a statistically high-powered representation of the full 200-example Phase 5B dataset.

1. **Quadratic Weighted Kappa (QWK)** is the primary metric because 1–5 ratings are ordinal; small discrepancies (e.g. 4 vs 5) receive smaller penalties than large discrepancies (e.g. 1 vs 5).
2. **Unbiased Annotation**: Human ratings were performed independently without displaying LLM judge scores to prevent anchoring bias.
