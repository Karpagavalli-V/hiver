# AI-Assisted Golden Set Review Audit

**CRITICAL DISCLAIMER**: The labels within `data/golden_set/golden_set_ai_reviewed.csv` are **AI-assisted pre-annotations**, NOT final human hand labels. They must undergo human review before being treated as ground truth for any evaluation.

## Methodology

To accelerate the Golden Set annotation process, we utilized an AI pipeline to independently re-evaluate the 200 Golden Set examples.

### Settings
- **Model**: `gemini-1.5-flash` (via OpenAI compatibility layer)
- **Temperature**: 0.0 (Strictly deterministic)
- **Input Size**: 200 Examples (`G-1000` through `G-1199`)

### Anti-Leakage Safeguards
To prevent anchoring and bias, the LLM was **strictly hidden** from the following data:
- Original heuristic "weak labels"
- System predicted intents
- System predicted escalation decisions
- Historical retrieval evidence
- Any prior AI pre-annotations from earlier runs

The LLM was solely provided:
1. The raw `customer_message`
2. The raw `conversation_context`
3. The official 9-intent taxonomy (`configs/intents.json`)
4. The Golden Set Annotation rules

### Handling Uncertainty
The LLM was instructed to explicitly flag any ambiguities in the `ai_uncertainty_flags` column and output its confidence (`LOW`, `MEDIUM`, `HIGH`). These flags are aggressively utilized by the Priority Queue to force human review on borderline cases.

## Review Queue Priority Distribution
The AI outputs were processed by `scripts/ai_review_queue.py` to identify cases genuinely requiring human intervention.

- **Priority 1 (Must Review)**: 80 examples (Security, legal threats, manager requests, low confidence, ambiguous intents, missing context, or conflicting auto-handle logic).
- **Priority 2 (Review If Time)**: 0 examples (Moderate uncertainty).
- **Priority 3 (Clear)**: 120 examples (High confidence, clean taxonomy match).
