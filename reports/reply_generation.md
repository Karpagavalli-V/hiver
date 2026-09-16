# Phase 4C: Grounded Reply Generation

## Objective
The goal of Phase 4C was to build the generation infrastructure to transform an inbound customer message, predicted intent, and retrieved historical evidence into a coherent AmazonHelp customer support reply.

## Provider-Agnostic Architecture
We structured the logic using a `BaseReplyProvider` abstraction layer. Because the external LLM API is currently unavailable to the test environment, we implemented a deterministic `MockReplyProvider`. 

**Decision Log Context**: Why avoid external APIs right now?
1. The primary focus of this phase is *infrastructure stability* and *grounding safeguards*, not tuning prompt linguistics.
2. Building `LLMReplyProvider` against an abstract interface ensures that whether the system is eventually run on `gpt-4o-mini`, `Claude`, or `Gemini`, the generation engine and its schema validation/fallback logic remain exactly the same.

## Grounding Strategy & Safeguards
The prompt instructions inside the `LLMReplyProvider` are structurally designed to prevent hallucination. The rules enforce that the model must:
- Extract facts *only* from the historical evidence block.
- Refuse to invent refund timelines or compensation.
- Never claim to have taken an action (since this is an offline drafting tool).

If the `HistoricalRetriever` returns empty evidence (which occurs in ~2.4% of validation queries), the `ReplyGenerator` guarantees a safe fallback response by rejecting to run generation entirely.

## Offline Generation Evaluation
We ran the pipeline against a random 500-example sample from the Validation Set using the `MockReplyProvider`. The primary goal was to verify infrastructure constraints:

- **Total Test Cases**: 500
- **Valid Schema Output Rate**: 100.0% (The generator perfectly maintains the requested JSON-equivalent python dictionary schema).
- **Missing-Evidence Rate**: 2.4% 
- **Fallback Rate**: 2.4% (Direct 1:1 parity with missing evidence confirms the safeguard works).
- **Evidence Attachment Rate**: 97.6% (Confirmed that historical `root_id` citations are accurately tracked to the output).

## Known Limitations
- The current output quality metric is entirely unmeasured since `MockReplyProvider` simply outputs `[MOCK]` placeholder text. Real human-rated quality scoring must be performed after Phase 4D (Golden Set Construction) and once a valid external LLM API is authenticated.
