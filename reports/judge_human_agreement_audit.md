# LLM-as-a-Judge & Human Agreement Audit Report

## 1. Executive Summary

This audit evaluates the implementation, rubric, score calculations, and human agreement status for the **LLM-as-a-Judge** evaluation system in Phase 5B.

- **Rubric Confirmed**: **YES** (5-dimension 1–5 integer scale defined in `src/evaluation/llm_judge.py`)
- **Real Human Reply Ratings Available**: **YES** (20-example human rating validation sample completed in `data/human_judge/human_judge_20.csv`)
- **Macro-Averaged Quadratic Weighted Kappa (QWK)**: **`0.3038`**
- **Macro-Averaged Cohen's Kappa**: **`0.1949`**
- **Number of Human-Rated Generated Replies**: **20**

---

## 2. LLM-as-a-Judge Rubric Specification

The LLM Judge (`src/evaluation/llm_judge.py`) evaluates generated customer support replies against customer messages and historical evidence across **5 distinct dimensions** on a **1 to 5 integer scale** (1 = poor, 5 = excellent):

| Dimension | Description / Evaluation Criteria | Average Score (200 Examples) |
| :--- | :--- | :---: |
| **1. RELEVANCE** | Does the reply address the customer's actual issue? | **4.32 / 5.00** |
| **2. GROUNDEDNESS** | Is the response supported by the retrieved historical evidence/context? | **3.29 / 5.00** |
| **3. HELPFULNESS** | Does it provide a useful next step or answer? | **3.81 / 5.00** |
| **4. SAFETY** | Does it avoid unsupported claims, risky actions, or fabricated account info? | **5.00 / 5.00** |
| **5. TONE** | Is it professional, concise, and appropriate for customer support? | **4.64 / 5.00** |

---

## 3. Score & Pass Rate Calculations

### A. Overall Reply Quality Score (4.20 / 5.00)
- **Model Output**: For each example, the LLM Judge outputs an `overall_score` float between 1.0 and 5.0 based on the 5 dimensions.
- **Aggregation**: The overall 4.20 score is calculated as the unweighted arithmetic mean of `overall_score` across all 200 completed examples:
  $$\text{Mean Overall Score} = \frac{1}{200} \sum_{i=1}^{200} \text{overall\_score}_i = 4.20$$

### B. Pass Rate Calculation (96.5%)
- **Pass Threshold**: A reply receives `pass = True` if and only if:
  $$\text{overall\_score} \ge 3.0 \quad \text{AND} \quad \text{safety} \ge 4.0$$
- **Pass Rate Result**: Out of 200 evaluated replies, **193 passed** and **7 failed** (due to low overall score or safety < 4), yielding:
  $$\text{Pass Rate} = \frac{193}{200} = 96.5\%$$

---

## 4. Human-vs-Judge Agreement Analysis ($N=20$)

### A. Completed 20-Example Agreement Benchmark
A 20-example stratified validation sample was human-rated using `scripts/human_judge_20.py` and validated with `scripts/validate_human_judge_20.py`. The LLM-as-a-Judge evaluated the exact same 20 replies.

| Dimension | Human Mean Score | LLM Judge Mean Score | Cohen's Kappa (Exact) | Quadratic Weighted Kappa (QWK) |
| :--- | :---: | :---: | :---: | :---: |
| **Relevance** | 4.35 | 4.55 | -0.0667 | **0.0244** |
| **Groundedness** | 3.85 | 3.50 | 0.0783 | **0.1875** |
| **Helpfulness** | 3.70 | 4.20 | 0.0000 | **0.3443** |
| **Safety** | 5.00 | 5.00 | 1.0000 | **1.0000** |
| **Tone** | 4.15 | 4.75 | -0.0370 | **-0.0370** |

### B. Statistical & Sample Notes
1. **Validation Sample Scope**: Due to the small sample size ($N=20$), these agreement statistics represent a focused validation benchmark for inter-rater reliability and should not be treated as a population-level estimate.
2. **Agreement Infrastructure**: The calculation code is implemented in [`src/evaluation/human_judge_agreement.py`](file:///d:/hiver/src/evaluation/human_judge_agreement.py) and executed via `scripts/calculate_human_judge_agreement.py`.

