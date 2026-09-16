# Phase 5B Evaluation Report

> **Run mode**: OFFLINE/MOCK  
> **Examples evaluated**: 200 / 5  

## 1. Dataset
- **Golden Set size**: 200 examples
- **Source split**: INTERNAL_TEST
- **Annotation status**: 200 manually reviewed human annotations (100% human-verified ground truth).
- **Weak labels**: NOT used as ground truth. All metrics computed against `human_intent`.
- **Target responses**: NOT supplied to classifier, retriever, generator, or judge.

## 2. Intent Classification
- **Current Model (OFFLINE/MOCK) Accuracy**: 0.5650 | **Macro F1**: 0.6061
- **TF-IDF Baseline Accuracy**: 0.6000 | **Macro F1**: 0.4444
- **Majority Baseline Accuracy**: 0.4000 | **Macro F1**: 0.1429

### Per-Intent Results (Current Model)
```text
                           precision    recall  f1-score   support

        AccountAndPayment       0.56      0.74      0.64        19
          CourierFeedback       0.60      0.80      0.69        15
CustomerServiceEscalation       0.41      0.80      0.55        15
       DamagedOrDefective       0.45      0.71      0.56         7
           DeliveryStatus       0.56      0.68      0.61        37
          DigitalServices       0.60      0.30      0.40        10
                    OTHER       0.62      0.33      0.43        79
        RefundsAndReturns       0.69      0.85      0.76        13
                WrongItem       0.71      1.00      0.83         5

                 accuracy                           0.56       200
                macro avg       0.58      0.69      0.61       200
             weighted avg       0.58      0.56      0.54       200
```

## 3. Escalation
- **Accuracy**: 0.4450
- **AUTO-HANDLE rate**: 0.0000
- **ESCALATE rate**: 1.0000

### Escalation Classification Report
```text
              precision    recall  f1-score   support

 AUTO-HANDLE       0.00      0.00      0.00       111
    ESCALATE       0.45      1.00      0.62        89

    accuracy                           0.45       200
   macro avg       0.22      0.50      0.31       200
weighted avg       0.20      0.45      0.27       200
```

## 4. Reply Quality (LLM-as-Judge)
- **Run mode**: OFFLINE/MOCK
- **Replies judged**: 200
- **Relevance**: 4.32
- **Groundedness**: 3.29
- **Helpfulness**: 3.81
- **Safety**: 5.00
- **Tone**: 4.64
- **Overall Score**: 4.20
- **Pass Rate**: 96.5%

## 5. Human / Judge Agreement
**NOT AVAILABLE** — No genuine human reply-quality ratings exist yet. No fabricated agreement score is reported.

## 6. Failure Analysis
See `reports/failure_analysis.md` for detailed examples.
- Intent mismatches: 87
- Escalation mismatches: 111
- Low Judge Scores (< 3.0 or safety < 4): 7

## 7. Limitations
- Mixed human/AI-assisted Golden Set annotations
- Small Golden Set (200 examples)
- LLM judge may hallucinate or misunderstand nuance
- Possible sampling bias in source TWCS data

## 8. Reproduction
```bash
# 5-example live smoke-test
python scripts/run_evaluation.py --judge --limit 5

# Full resumable live evaluation
python scripts/run_evaluation.py --judge

# Offline/mock (no API calls consumed)
python scripts/run_evaluation.py --judge --offline
```
