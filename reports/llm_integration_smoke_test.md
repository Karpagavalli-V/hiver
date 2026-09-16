# LLM Integration Smoke Test

## Infrastructure Tests

- **Environment Config**: The `LLMReplyProvider` successfully uses the configured `.env` file parameters, securely importing the API key as an environment variable and dynamically fetching the Gemini-compatible `OPENAI_BASE_URL` and `LLM_MODEL`. (No hardcoded secrets).
- **Test Suite Result**: The complete test suite (`python -m pytest`) passes. The offline `test_reply_generator.py` validates schema checks correctly.
- **Rate-limit Smoke Test**: `scripts/smoke_test_rate_limit.py` was executed. The test validates that 429 API errors are gracefully handled by the retry/backoff mechanism within the proxy client wrapper without fatal crashes.

## Real API Reply-Generation Smoke Test

A localized test was conducted using exactly 2 representative AmazonHelp validation examples through `scripts/smoke_test_real_reply.py`. 
*Note: These 2 examples verify pipeline integration and structural constraints; they do NOT demonstrate reply quality statistically.*

### Structural and Policy Validations

For the 2 generated API calls, all structural requirements were verified:
- **API Request**: Succeeded using the real `LLMReplyProvider` connected to the `gemini-3.6-flash` model. 
- **Structured JSON**: Parsed successfully matching the expected schema.
- **Reply non-empty**: Both generated replies contained substantive textual responses.
- **Evidence Attached**: The `evidence_used` arrays were correctly populated with the underlying root IDs.
- **Grounding Preserved**: The `grounding_summary` explicitly described how the historical example justified the reply.
- **Policy Checks**: No unsupported action claims were generated. (e.g. For a mobile number intent, the system safely avoided inventing account actions and politely advised that details couldn't be accessed securely).
- **No API Errors**: Execution completed continuously without unhandled exceptions.

### Leakage Safeguards

- The real smoke test explicitly utilized `query_root_id` and `query_timestamp` constraints on the `HistoricalRetriever`.
- The retriever was successfully restricted to `TRAIN` data, preventing evaluation dataset leakage.
- Target conversations were successfully isolated from being returned as their own evidence.

## Example Responses (From API)

> **Customer**: `@AmazonHelp No, I'm on my phone, or I can use my iPad`
> **Reply**: Thank you. Are you using a browser to browse with or the Amazon shopping app?
> **Grounding**: Following Example 1, when a customer indicates they are using a mobile device or iPad, ask if they are using a browser or the Amazon shopping app.
> **Evidence**: `[2153020.0]`

> **Customer**: `@AmazonHelp You can search my problem with my Mobile number`
> **Reply**: We're unable to access your account details via Twitter using your mobile number. Also, please refrain from sharing personal information as our page is visible to the public. Please connect with us directly via the Help section on our app/website so we can assist you safely.
> **Grounding**: Informed the customer that we cannot access details via Twitter using a mobile number and requested they refrain from sharing personal information publicly, following Example 1 and Example 2.
> **Evidence**: `[180617.0, 1666041.0]`

## Conclusion
The full end-to-end integration of the `LLMReplyProvider` with the real API backend is strictly validated and operational. 
