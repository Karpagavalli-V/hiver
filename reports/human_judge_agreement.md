# LLM-Judge vs. Human Agreement Report (20-Example Validation Sample)

## 1. Summary
- **Sample Size**: 20 examples
- **Sampling Methodology**: Stratified deterministic sampling (seed=42) across 9 intent classes and balanced escalation states (10 `AUTO-HANDLE`, 10 `ESCALATE`).
- **Rating Scale**: 1 to 5 integer ordinal scale per dimension (1 = Poor, 5 = Excellent).
- **Workflow Status**: **SAMPLING COMPLETE — AWAITING HUMAN ANNOTATION**
- **Annotation Tool**: `python scripts/human_judge_20.py`
- **Validation Script**: `python scripts/validate_human_judge_20.py`

---

## 2. LLM-as-a-Judge vs. Human Evaluation Rubric

Each generated customer support reply is independently rated on 5 core quality dimensions:

1. **RELEVANCE (1–5)**: Does the reply address the customer's actual inquiry?
2. **GROUNDEDNESS (1–5)**: Is the response supported by historical conversation context/retrieved evidence?
3. **HELPFULNESS (1–5)**: Does it provide a concrete next step, link, or resolution?
4. **SAFETY (1–5)**: Does it avoid making unsupported promises, risky policy commitments, or leaking information?
5. **TONE (1–5)**: Is the communication professional, concise, empathetic, and appropriate for Amazon customer support?

---

## 3. Sample Stratification Summary

The 20 validation examples were deterministically selected from the completed 200-example evaluation dataset (`reports/evaluation_results.json`) using seed 42:

- **Intent Coverage (9 intents)**:
  - `DeliveryStatus`: 3 examples
  - `CourierFeedback`: 3 examples
  - `RefundsAndReturns`: 2 examples
  - `DamagedOrDefective`: 2 examples
  - `DigitalServices`: 2 examples
  - `WrongItem`: 2 examples
  - `AccountAndPayment`: 2 examples
  - `CustomerServiceEscalation`: 2 examples
  - `OTHER`: 2 examples
- **Ground Truth Escalation Balance**:
  - `AUTO-HANDLE`: 10 examples (50%)
  - `ESCALATE`: 10 examples (50%)

---

## 4. Methodological & Statistical Notes

> [!IMPORTANT]
> **Sample Size Limitation Notice**:
> This 20-example validation sample is designed to satisfy the Hiver assignment requirement for human-vs-judge agreement. It provides a focused inter-rater reliability measurement (Quadratic Weighted Kappa) between the LLM Judge and a human annotator. However, due to its small size ($N=20$), agreement metrics derived from this sample should **not** be extrapolated as a statistically high-powered representation of the entire 200-example Phase 5B evaluation.
