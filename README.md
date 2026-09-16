# AmazonHelp AI Customer Support System & Copilot

This repository contains the end-to-end implementation, evaluation harness, and interactive web application for the **AmazonHelp AI Customer Support System**, developed for the Hiver SDE Intern Take-Home Assignment.

---

## 1. Project Overview

The AmazonHelp AI Support Copilot automates e-commerce customer support workflows on social channels (Twitter/X). The system classifies customer inquiries, retrieves grounded historical evidence, generates safe and empathetic brand-aligned responses, and evaluates whether a ticket can be safely auto-handled or requires human escalation.

### Core System Pipeline
```
Customer Message (+ Context) ➔ Intent Classification ➔ Historical Retrieval ➔ Reply Generation ➔ Escalation Engine
```
1. **Intent Classification**: Predicts 1 of 9 operational intents using `openai/gpt-4o-mini` via OpenRouter.
2. **Historical Retrieval**: Retrieves top-3 past resolved interactions from training data via TF-IDF + Cosine Similarity.
3. **Grounded Reply Generation**: Generates safe, brand-aligned replies grounded in historical context.
4. **Escalation Decision Engine**: Evaluates safety, financial, security, and retrieval risk flags to output `AUTO-HANDLE` or `ESCALATE`.

---

## 2. Dataset Context & Split Methodology

- **Dataset**: Twitter Customer Support (TWCS) dataset.
- **Brand Focus**: `AmazonHelp` (169,838 tweets across 82,534 conversation threads).
- **Split Strategy**: Grouped at the conversation thread level (`root_id`) to prevent data contamination:
  - **Train**: 66,027 conversation threads (80%)
  - **Validation**: 8,253 conversation threads (10%)
  - **Internal Test**: 8,254 conversation threads (10%)
- **Golden Set Benchmark**: 200 test examples drawn from `INTERNAL_TEST`, with 100% human-verified ground truth labels (`human_intent`, `human_auto_handle`).

---

## 3. Intent Taxonomy (9 Categories)

1. `DeliveryStatus`: Package tracking, shipping delays, carrier updates.
2. `RefundsAndReturns`: Refund inquiries, return label requests, refund processing delays.
3. `DamagedOrDefective`: Broken, defective, or oil-covered items.
4. `WrongItem`: Wrong product, size, or color received.
5. `CourierFeedback`: Feedback/complaints regarding carrier service (AMZL, UPS, etc.).
6. `AccountAndPayment`: Password reset, account login, credit card charges.
7. `DigitalServices`: Prime Video, Kindle, Music, digital subscriptions.
8. `CustomerServiceEscalation`: Complaints about poor agent service or long unresolved delays.
9. `OTHER`: General praise, ambiguous statements, or queries outside defined operational intents.

---

## 4. Benchmark Evaluation Results

Evaluated on the frozen 200-example Golden Set benchmark:

| Metric | Majority Baseline | TF-IDF Baseline | Live LLM Pipeline (`gpt-4o-mini`) |
| :--- | :---: | :---: | :---: |
| **Completed Examples** | 200 / 200 | 200 / 200 | **200 / 200 (0 Failed)** |
| **Intent Accuracy** | 39.50% | 34.50% | **56.50%** (`0.5650`) |
| **Intent Macro F1** | 6.29% | 35.93% | **60.61%** (`0.6061`) |
| **Escalation Accuracy** | N/A | N/A | **44.50%** (`0.4450`) |
| **Reply Quality (LLM Judge)** | N/A | N/A | **4.20 / 5.00** |
| **Reply Pass Rate** | N/A | N/A | **96.5%** (`193 / 200`) |

*Performance Comparison*: The live LLM pipeline demonstrates a **+22.0 percentage-point difference in accuracy** versus the TF-IDF baseline and a **+24.68 percentage-point difference in Macro F1**.

---

## 5. Judge-Human Agreement Evaluation ($N=20$)

- **LLM-as-Judge Evaluation**: **COMPLETE** (All 200 generated replies judged across Relevance, Groundedness, Helpfulness, Safety, and Tone).
- **Human Ratings of Generated Replies**: **COMPLETED** (20-example validation sample in `data/human_judge/human_judge_20.csv`).
- **Macro-Averaged Quadratic Weighted Kappa (QWK)**: **`0.3038`** (Cohen's Kappa = **`0.1949`**).
- **Dimension QWK Breakdown**: Safety (1.0000), Helpfulness (0.3443), Groundedness (0.1875), Relevance (0.0244), Tone (-0.0370).
- **Statistical Scope**: Small validation sample ($N=20$), providing inter-rater reliability measurement without treating it as a population-level estimate.

---

## 6. Key System Limitations

1. **Benchmark Sample Size ($N=200$)**: Evaluated on a 200-example Golden Set; rarer intent classes have smaller support counts.
2. **Conservative Escalation Policy**: The escalation decision engine prioritizes safety over automation volume, triggering `ESCALATE` whenever retrieval confidence is low.
3. **No Real Transactional Actions**: The system generates customer support text but does not execute real SQL database mutations or actual credit card refunds.

---

## 7. Quick Start & Reproducibility Instructions

### Prerequisites & Installation
Ensure Python 3.9+ is installed, then run:

```bash
# 1. Install required dependencies
pip install -r requirements.txt
```

### Run Automated Test Suite (33 Unit Tests)
```bash
python scripts/run_eval_tests.py
```

### Run Evaluation Harness in Offline Mock Mode (Zero API Calls)
```bash
python scripts/run_evaluation.py --judge --offline
```

### Launch Interactive Streamlit Frontend Demo
```bash
streamlit run app.py
```

---

## 8. Principal Submission Reports

For detailed technical analysis, inspect the following documentation artifacts in `reports/`:
- [`reports/FINAL_REPORT.md`](file:///d:/hiver/reports/FINAL_REPORT.md): Comprehensive 16-section technical submission report.
- [`reports/final_evaluation_audit.md`](file:///d:/hiver/reports/final_evaluation_audit.md): Phase 5B evaluation audit & metric verification.
- [`reports/failure_analysis.md`](file:///d:/hiver/reports/failure_analysis.md): In-depth failure mode analysis on Golden Set errors.
- [`reports/decision_log.md`](file:///d:/hiver/reports/decision_log.md): Log of major architectural and engineering decisions.
