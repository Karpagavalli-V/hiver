with open('reports/decision_log.md', 'a', encoding='utf-8') as f:
    f.write("\n\n## Phase 3: Data Foundation & Baselines Decisions\n")
    f.write("- **Data Splits**: Split at the `root_id` (conversation) level into 80/10/10 Train/Val/Test. This guarantees no leakage across splits where a thread's messages are divided.\n")
    f.write("- **Weak Labels**: Due to a lack of 200k manual annotations, a keyword heuristic was used to generate weak labels for the development sets. These are explicitly NOT ground truth and will be replaced by a human-annotated Golden Set in Phase 4.\n")
    f.write("- **Leakage Prevention**: When building contextual features, the chronological thread was strictly filtered to exclude the target message's future and the brand's response. The context was restricted to the 3 immediately preceding messages to cap prompt sizes for future LLM deployment.\n")
    f.write("- **Baselines**: A Majority Class baseline and TF-IDF + Logistic Regression baselines were chosen for their deterministic behavior. The TF-IDF model was trained twice to run a context ablation study (`MESSAGE_ONLY` vs `CONVERSATION_CONTEXT`).\n")
