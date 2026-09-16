# Phase 5B Evaluation Report

> **Run mode**: LIVE  
> **WARNING**: 1 example(s) failed due to API errors and are **excluded** from metrics.  
> **Examples evaluated**: 6 / 1  

## 1. Dataset
- **Golden Set size**: 200 examples
- **Source split**: INTERNAL_TEST
- **Annotation status**: 78 manually reviewed + 122 AI-assisted annotations. AI-assisted annotations are **not** treated as independent human labels.
- **Weak labels**: NOT used as ground truth. All metrics computed against `human_intent`.
- **Target responses**: NOT supplied to classifier, retriever, generator, or judge.

## 2. Intent Classification
- **Current Model (LIVE) Accuracy**: 0.8333 | **Macro F1**: 0.7333
- **TF-IDF Baseline Accuracy**: 1.0000 | **Macro F1**: 1.0000
- **Majority Baseline Accuracy**: 0.0000 | **Macro F1**: 0.0000

### Per-Intent Results (Current Model)
```text
                           precision    recall  f1-score   support

CustomerServiceEscalation       0.00      0.00      0.00         0
       DamagedOrDefective       1.00      0.50      0.67         2
           DeliveryStatus       1.00      1.00      1.00         1
                    OTHER       1.00      1.00      1.00         2
        RefundsAndReturns       1.00      1.00      1.00         1

                 accuracy                           0.83         6
                macro avg       0.80      0.70      0.73         6
             weighted avg       1.00      0.83      0.89         6
```

## 3. Escalation
- **Accuracy**: 0.1667
- **AUTO-HANDLE rate**: 0.0000
- **ESCALATE rate**: 1.0000

### Escalation Classification Report
```text
              precision    recall  f1-score   support

 AUTO-HANDLE       0.00      0.00      0.00         5
    ESCALATE       0.17      1.00      0.29         1

    accuracy                           0.17         6
   macro avg       0.08      0.50      0.14         6
weighted avg       0.03      0.17      0.05         6
```

## 4. Reply Quality (LLM-as-Judge)
- **Run mode**: LIVE
- **Replies judged**: 6
- **Relevance**: 4.00
- **Groundedness**: 4.33
- **Helpfulness**: 3.67
- **Safety**: 5.00
- **Tone**: 4.83
- **Overall Score**: 4.37
- **Pass Rate**: 100.0%

## 5. Human / Judge Agreement
**NOT AVAILABLE** — No genuine human reply-quality ratings exist yet. No fabricated agreement score is reported.

## 6. Failure Analysis
See `reports/failure_analysis.md` for detailed examples.
- Intent mismatches: 1
- Escalation mismatches: 5
- Low Judge Scores (< 3.0 or safety < 4): 0

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
