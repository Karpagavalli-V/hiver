# Phase 5B: Failure Analysis Report

This report automatically highlights examples where the system's predictions diverged from the Golden Set labels or received low LLM-judge scores.

## 1. Intent Classification Mismatches
Total intent failures: 1

**ID: G-1005**
- Message: So far @115821 has failed to respond to my oil covered package and ruined game.
- True Intent: `DamagedOrDefective` | Predicted: `CustomerServiceEscalation`
- Hypothesis: Ambiguous vocabulary or missing critical context.

## 2. Escalation Decision Mismatches
Total escalation failures: 5

**ID: G-1001**
- Message: @AmazonHelp Thanks for the prompt response.  Here's your link-&gt;
WD My Passport 1TB Portable External Hard Drive (Blue) https://t.co/AU9qOeLQiP
- True Decision: `AUTO-HANDLE` | Predicted: `ESCALATE`
- Hypothesis: Threshold tuning required or safety policy overly aggressive/lenient.

**ID: G-1002**
- Message: @AmazonHelp I spoke to one of your agents tonight on the phone and he went above and beyond (even a follow up email)! Anyway to ID so I can fill out a survey of some sort??
- True Decision: `AUTO-HANDLE` | Predicted: `ESCALATE`
- Hypothesis: Threshold tuning required or safety policy overly aggressive/lenient.

**ID: G-1003**
- Message: @AmazonHelp The last two packages were supposed to be delivered by AMZL US.
- True Decision: `AUTO-HANDLE` | Predicted: `ESCALATE`
- Hypothesis: Threshold tuning required or safety policy overly aggressive/lenient.

**ID: G-1004**
- Message: Wow! @115830 this packaging job is atrocious. I don’t order books for them to arrive damaged 😡 https://t.co/sJNSq2qqM8
- True Decision: `AUTO-HANDLE` | Predicted: `ESCALATE`
- Hypothesis: Threshold tuning required or safety policy overly aggressive/lenient.

**ID: G-1005**
- Message: So far @115821 has failed to respond to my oil covered package and ruined game.
- True Decision: `AUTO-HANDLE` | Predicted: `ESCALATE`
- Hypothesis: Threshold tuning required or safety policy overly aggressive/lenient.

## 3. Low Judge Scores (Reply Quality)
Total low-scoring replies: 0

