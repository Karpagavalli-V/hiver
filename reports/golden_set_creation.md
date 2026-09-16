# Golden Set Creation Report

## Overview
As part of Phase 5A, a robust, strictly independent **Golden Set** of 200 examples has been created for final human evaluation. 

**The Golden Set labels are intended to be independent human judgments and are not copied from the existing weak labels.**

## Sampling Methodology
- **Source Split**: Exclusively drawn from `INTERNAL_TEST` (`data/splits/amazon_test.csv`). The `VALIDATION` set was deliberately avoided because it was used for prompt engineering and threshold tuning during development. 
- **Sample Size**: Exactly 200 examples.
- **Random Seed**: `42`
- **Sampling Strategy**: Stratified random sampling based on the heuristic `weak_label` to ensure rare intents (e.g., `WrongItem`, `DamagedOrDefective`) are properly represented. We targeted ~22 examples per valid intent to achieve a balanced representation across all 9 classes.

## Annotation Package
The package generated for human annotators consists of:
1. `golden_set_annotation.csv`: Contains the customer message and historical conversation context. The label fields are entirely blank.
2. `ANNOTATION_GUIDE.md`: Comprehensive instructions on how to manually label intents and judge escalation.
3. `golden_set_metadata.json`: A private metadata file storing the trace back to the `tweet_id`, `root_id`, and `weak_label`.

## Leakage Safeguards
An automated audit (`scripts/audit_golden_set.py`) was executed to cryptographically enforce independence:
- **Conversation Leakage**: Verified that zero `root_id`s in the Golden Set exist in either `TRAIN` or `VALIDATION`.
- **Target Response Leakage**: Verified that the brand's response to the target message is excluded from the conversation context.
- **Future Leakage**: Verified that no chronologically future messages are included.
- **Label Bleed**: Verified that the heuristic `weak_label` and all model predictions (classifier/reply generator) are strictly excluded from the annotation CSV interface to prevent anchor bias.

## Limitations
- Stratifying on weak labels means the true class distribution of the Golden Set relies slightly on the accuracy of the heuristic regex. If the regex systematically mischaracterized an intent, that intent might be underrepresented. 
- The evaluation requires human annotators to accurately judge if historical evidence could *plausibly* resolve the issue, which can be subjective.
