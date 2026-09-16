# Golden Set Design & Evaluation Harness Audit

This document outlines the final evaluation strategy for the AmazonHelp AI agent, moving from weak/heuristic labels to a pristine, hand-labelled Golden Set.

## 1. Audit Findings

### A. Proposed Golden Set Source Split
The final Golden Set must be drawn exclusively from the **`INTERNAL_TEST`** split (`data/splits/amazon_test.csv`). 
- The `TRAIN` split was used for retriever indexing and baseline model training.
- The `VALIDATION` split was heavily utilized during Phase 4 for LLM evaluation, escalation threshold tuning, and iterative rule development. 
- The `INTERNAL_TEST` split is completely unseen and pristine, ensuring zero data leakage.

### B. Leakage & Contamination Analysis
**Safeguards Confirmed:**
- **Retrieval Index**: The `HistoricalRetriever` explicitly builds its TF-IDF matrix and database *only* from the `TRAIN` split. `INTERNAL_TEST` examples literally do not exist in the vector space, making target-leakage impossible.
- **Baseline Training**: All scikit-learn baselines were trained strictly on the `TRAIN` split.
- **LLM Caches**: Any existing LLM caching maps to exact prompt strings. Because `INTERNAL_TEST` examples are mutually exclusive at the conversation level, their prompts will be unique cache misses.

### C. Independence of Splits
`scripts/create_splits.py` guarantees independence by routing entire conversations via `root_id`. This prevents the "future" of a test conversation from accidentally appearing in the training data, structurally preserving evaluation integrity.

### D. Available Fields
By joining the test split with the main `twcs.csv`, we have access to:
- `tweet_id` & `root_id`
- `created_at` timestamps
- `text` (The customer message)
- Conversation history (via recursive `in_response_to_tweet_id` tracing)
- Brand response (via `in_response_to_tweet_id` matching from the brand)
- `weak_label`

### E. Historical Retrieval Safety
Yes, retrieval can be performed safely. The `HistoricalRetriever` already enforces safety in two ways:
1. It is physically partitioned (built only on `TRAIN`).
2. It programmatically filters `query_root_id` and `query_timestamp` at inference time, ensuring robust zero-leakage retrieval.

### F. Cache Contamination
Caches (`cache/tfidf_*.pkl`) are safe as they are derived from `TRAIN`. The evaluation script must ensure it does not accidentally overwrite the global cache, though reading from it is standard.

### G. Methodological Risks
1. **Class Imbalance**: A purely random sample of `INTERNAL_TEST` will be overwhelmingly dominated by `OTHER` and `DeliveryStatus`, leaving rare intents like `AccountAndPayment` severely underrepresented. **Mitigation**: We must use **stratified sampling** based on `weak_label` to ensure all 9 intents are represented in the 150-250 sample size.
2. **Anchor Bias**: If human annotators see the `weak_label` during annotation, they might lazily agree with the heuristic. **Mitigation**: The UI or annotation spreadsheet must hide the `weak_label` column.
3. **Escalation Subjectivity**: Deciding whether to escalate is subjective. **Mitigation**: Annotators must be given the same escalation policy guidelines defined in Phase 4D.

## 2. Golden Set Schema Design

The Golden Set will be serialized as a JSON array. Below is the proposed schema for the 150-250 examples.

```json
[
  {
    "tweet_id": 123456,
    "root_id": 10001,
    "timestamp": "2017-10-31 22:28:00+00:00",
    "customer_message": "My package hasn't arrived, where is it?",
    "conversation_context": [
      {
        "author": "customer",
        "text": "Hello, I have an issue."
      },
      {
        "author": "AmazonHelp",
        "text": "Hi there, how can we help?"
      }
    ],
    "actual_brand_response": "I'm sorry to hear that. Could you DM us your tracking number?",
    "weak_label": "DeliveryStatus",
    
    // Human Annotation Fields (To be filled blindly)
    "human_label_intent": null,        // Must map to one of the 9 taxonomy intents
    "human_label_escalate": null,      // Boolean: True (ESCALATE) or False (AUTO-HANDLE)
    "human_label_notes": null          // Optional rationale for ambiguous cases
  }
]
```

## 3. Evaluation Procedure

1. **Sampling**: Generate `data/golden_set_unlabelled.json` using stratified sampling on `INTERNAL_TEST`.
2. **Annotation**: Hand-label the `human_label_intent` and `human_label_escalate` fields.
3. **Execution**: Pass the customer messages through the full pipeline (`HistoricalRetriever` -> `LLMClassifier` -> `ReplyGenerator` -> `EscalationDecisionEngine`).
4. **Scoring**: 
   - Compute Intent Accuracy (Predicted Intent vs `human_label_intent`).
   - Compute Escalation Accuracy, Precision, and Recall (Engine Decision vs `human_label_escalate`).
   - Compare performance against the Phase 3 Baselines using the human labels.
