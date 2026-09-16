# Phase 4D: AUTO-HANDLE vs ESCALATE Decision Engine

## Overview
The decision engine acts as the final gatekeeper before an AI-generated reply is surfaced to the customer. It determines whether a case can safely be routed to `AUTO-HANDLE` or whether it must `ESCALATE` to a human agent.

*This is a safety-oriented decision policy, not a claim that the agent can autonomously perform account actions. High-risk intents and action requests are deliberately blocked.*

## Decision Architecture

The engine uses purely **deterministic rules** instead of a second LLM evaluation call. This ensures:
- Zero hallucination risk on safety policies.
- Guaranteed enforcement of account security and action limitations.
- Faster, cheaper, and fully reproducible routing.

### AUTO-HANDLE Criteria
A case is approved for `AUTO-HANDLE` only if **ALL** the following are true:
1. Classifier confidence is $\ge 0.70$.
2. The `HistoricalRetriever` found at least one relevant historical example.
3. The top retrieved example has a similarity score $\ge 0.65$.
4. The retrieved evidence is not contradictory.
5. The customer message contains NO high-risk keywords (security, finance, legal threats).
6. The customer message does not demand an unsupported account action (e.g., "cancel my order").
7. The customer did not explicitly request a human manager/agent.
8. The intent is not a severe escalation (`CustomerServiceEscalation`).

### ESCALATE Criteria (Precedence Order)
If any criteria fail, the system escalates with one of the following risk flags in order of precedence:
1. `ACCOUNT_SECURITY`, `FINANCIAL_DISPUTE`, `LEGAL_OR_SAFETY`
2. `UNSUPPORTED_ACTION`
3. `HUMAN_REQUEST`
4. `REPEATED_ESCALATION`
5. `NO_RETRIEVAL_EVIDENCE`, `CONTRADICTORY_EVIDENCE`, `WEAK_RETRIEVAL`
6. `LOW_CLASSIFIER_CONFIDENCE`

## Evaluation Results

Evaluated on a deterministic sample of 500 cases from the Validation split.

- **Total Cases**: 500
- **AUTO-HANDLE**: 80 (16.0%)
- **ESCALATE**: 420 (84.0%)

### Escalation Rate by Risk Flag
The majority of escalations were due to conservative retrieval thresholds ensuring high-quality grounding.

- WEAK_RETRIEVAL: 398
- LOW_CLASSIFIER_CONFIDENCE: 48
- REPEATED_ESCALATION: 30
- NO_RETRIEVAL_EVIDENCE: 12
- FINANCIAL_DISPUTE: 2
- UNSUPPORTED_ACTION: 2
- HUMAN_REQUEST: 2
- ACCOUNT_SECURITY: 1
- LEGAL_OR_SAFETY: 1

## Representative Examples

### AUTO-HANDLE
**Customer**: `@AmazonHelp No, I'm on my phone, or I can use my iPad` (Intent: OTHER)
**Reason**: All safety criteria met. High confidence and strong evidence.

**Customer**: `@AmazonHelp Neither, just that it's been delayed.` (Intent: DeliveryStatus)
**Reason**: All safety criteria met. High confidence and strong evidence.

### ESCALATE
**Customer**: `@AmazonHelp ... I want to speak to a manager...` (Intent: CustomerServiceEscalation)
**Flags**: `['HUMAN_REQUEST', 'REPEATED_ESCALATION']`
**Reason**: Customer explicitly requested a human agent.

**Customer**: `@AmazonHelp My account was hacked and there's a fraud charge` (Intent: AccountAndPayment)
**Flags**: `['ACCOUNT_SECURITY', 'FINANCIAL_DISPUTE']`
**Reason**: Account security issue detected.

## Known Limitations
- Relying on regex/heuristics for keywords can lead to false positives (e.g., "I don't need a manager").
- The retrieval similarity threshold is deliberately conservative (0.65), resulting in a low `AUTO-HANDLE` rate, but ensuring only the safest cases pass through.
