# Context Ablation Study

This report compares the performance of the intent classifier using only the target message versus including the conversation context (up to 3 preceding messages).

## Baseline Metrics
| Metric | Majority Class | TF-IDF (Message Only) | TF-IDF (Context Aware) |
|--------|----------------|-----------------------|------------------------|
| Accuracy | 0.7087 | 0.9380 | 0.7550 |
| Macro F1 | 0.0922 | 0.8714 | 0.6342 |
| Weighted F1 | 0.5879 | 0.9391 | 0.7718 |

## Intent Distribution
- OTHER: 13243
- DigitalServices: 1444
- CustomerServiceEscalation: 1080
- DeliveryStatus: 964
- RefundsAndReturns: 837
- CourierFeedback: 541
- AccountAndPayment: 312
- DamagedOrDefective: 186
- WrongItem: 79

## Per-Intent Metrics (Message Only)
```text
                           precision    recall  f1-score   support

        AccountAndPayment       0.81      0.94      0.87       312
          CourierFeedback       0.88      0.97      0.92       541
CustomerServiceEscalation       0.88      0.90      0.89      1080
       DamagedOrDefective       0.65      0.90      0.76       186
           DeliveryStatus       0.93      0.96      0.95       964
          DigitalServices       0.85      0.87      0.86      1444
                    OTHER       0.97      0.94      0.96     13243
        RefundsAndReturns       0.92      0.97      0.95       837
                WrongItem       0.58      0.89      0.70        79

                 accuracy                           0.94     18686
                macro avg       0.83      0.93      0.87     18686
             weighted avg       0.94      0.94      0.94     18686

```

## Per-Intent Metrics (Context Aware)
```text
                           precision    recall  f1-score   support

        AccountAndPayment       0.49      0.85      0.62       312
          CourierFeedback       0.55      0.88      0.67       541
CustomerServiceEscalation       0.49      0.79      0.61      1080
       DamagedOrDefective       0.39      0.82      0.53       186
           DeliveryStatus       0.50      0.84      0.62       964
          DigitalServices       0.56      0.76      0.64      1444
                    OTHER       0.95      0.73      0.83     13243
        RefundsAndReturns       0.56      0.83      0.67       837
                WrongItem       0.38      0.78      0.51        79

                 accuracy                           0.76     18686
                macro avg       0.54      0.81      0.63     18686
             weighted avg       0.83      0.76      0.77     18686

```

## Interpretation
Adding conversation context **did not improve** performance. This could be due to the naive TF-IDF representation treating context text as identical to the target message text, causing the classifier to overweight words from the brand's prompts or previous unrelated customer complaints. An LLM capable of distinguishing speaker roles might fare better.
