# LLM-as-a-Judge & Human Agreement Audit Report

## 1. Executive Summary

This audit evaluates the implementation, rubric, score calculations, and human agreement status for the **LLM-as-a-Judge** evaluation system in Phase 5B.

- **Rubric Confirmed**: **YES** (5-dimension 1–5 integer scale defined in `src/evaluation/llm_judge.py`)
- **Real Human Reply Ratings Available**: **NO** (No genuine human ratings of LLM-generated replies exist)
- **Agreement Score**: **N/A (`NOT AVAILABLE`)**
- **Number of Human-Rated Generated Replies**: **0**

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

## 4. Human-vs-Judge Agreement Analysis

### A. Availability Assessment
- **Status**: **NOT AVAILABLE (`N/A`)**
- **Reason**: The `human_reply_quality` column in `golden_set_final.csv` contains historical assessments of raw Twitter/brand responses from dataset preparation, **not** human ratings of the AI agent's generated replies (`generated_reply`).
- **Policy**: Per project guidelines and assignment requirements, **zero agreement score is fabricated**.

### B. Agreement Infrastructure
The code infrastructure for computing inter-rater reliability is fully implemented and unit-tested in [`src/evaluation/human_judge_agreement.py`](file:///d:/hiver/src/evaluation/human_judge_agreement.py):
1. **Categorical Agreement**: `calculate_cohen_kappa(human_scores, judge_scores)`
2. **Ordinal Agreement**: `calculate_weighted_kappa(human_scores, judge_scores)` (Quadratic Weighted Kappa)
3. **Availability Enforcement**: `check_human_ratings_available(df)` returns `False` until independent ratings of generated replies are supplied.

---

## 5. Smallest Practical Way to Obtain Human-Judge Agreement

To collect genuine agreement for submission without high labor overhead:

1. **Sample**: Extract a stratified sample of **20 generated replies** from `reports/evaluation_results.json`.
2. **Annotate**: Have a human reviewer rate the 20 generated replies on a 1–5 scale using the same 5-dimension rubric.
3. **Compute**: Run `calculate_weighted_kappa()` between the 20 human ratings and the LLM Judge ratings.
