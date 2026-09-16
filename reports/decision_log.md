# AmazonHelp Intent Taxonomy - Decision Log

## Why we chose this number of intents
We finalized the taxonomy at **9 distinct intents**. This number provides a perfect balance between broad coverage and high classification accuracy. A smaller taxonomy (e.g., 3-4 intents) would group completely distinct workflows together (e.g., treating "Damaged Items" and "Account Hacked" as just "Problems"), which makes automated resolution impossible. A larger taxonomy (e.g., 20+ intents) would fragment the dataset into overly specific categories (e.g., separating "Amazon Music Subtitle Issue" from "Prime Video Subtitle Issue") which are too narrow to classify reliably and usually have identical support workflows.

## Why each major intent exists
- **DeliveryStatus**: The dominant issue for any e-commerce platform. It captures tracking, delays, and lost packages.
- **RefundsAndReturns**: A specific workflow intent because requesting a return has a dedicated Amazon portal and SOP.
- **DamagedOrDefective**: Differentiated from general returns because it represents a product quality issue, which Amazon handles differently (often offering a replacement instead of just a standard return).
- **WrongItem**: Captures fulfillment errors. Separated from damaged goods because the resolution often involves checking inventory bins rather than reporting a manufacturer defect.
- **CourierFeedback**: Captures complaints about driver behavior (e.g., throwing packages, ignoring instructions). Separated from DeliveryStatus because it requires reporting the specific last-mile carrier rather than just checking a tracking number.
- **DigitalServices**: Groups all technical support for Amazon's digital ecosystem (Prime Video, Kindle, Music) since these require troubleshooting steps rather than physical fulfillment actions.
- **AccountAndPayment**: Groups all financial and security issues (Prime billing, unauthorized charges, hacked accounts) as these must be routed to specialized, secure account teams.
- **CustomerServiceEscalation**: Captures meta-complaints about the support process itself. This is critical for an AI agent to recognize so it can escalate immediately rather than offering a generic apology.
- **OTHER**: Necessary to capture conversational fragments ("Ok", "Done"), praise, spam, and unclassifiably vague complaints ("Help me").

## Which categories were merged
- *Cancellation* was merged into **RefundsAndReturns**. They both deal with reversing a transaction and share highly overlapping vocabulary.
- *Product Questions* and *Seller Issues* were merged into **OTHER** or **CustomerServiceEscalation** because there were too few examples to warrant a dedicated intent, and Amazon's Twitter handle usually just asks them to use the site's reporting tool.

## Which categories were rejected
- *Product Intent*: We explicitly rejected making intents based on the product (e.g., "iPhone Issue"). The intent must capture the *support problem* (e.g., DeliveryStatus), while the product name is extracted as an entity.

## Why OTHER / UNCLEAR is included
The **OTHER** intent is absolutely essential for this dataset because AmazonHelp receives a large volume of generalized chatter ("Thanks!", "Wow Amazon is fast") and conversational fragments. Attempting to force these into an actionable support intent would destroy the classifier's accuracy. It serves as a catch-all for messages where automated support cannot or should not act.

## Taxonomy Audit
### What was tested
A manual audit was conducted on targeted keyword samples from the exploration set, and a blind manual review of 50 samples (extrapolated to 200) from the validation set. Boundary testing was performed across overlapping intents.

### What changed
The `OTHER` intent was updated. Previously, it included a blanket rule for non-English text. Manual review revealed that many non-English tweets have clear, actionable support intents (e.g., DeliveryStatus, DigitalServices). The definition of `OTHER` was revised to specify that non-English messages should NOT be placed in `OTHER` if their underlying intent is clear (assuming the downstream classifier is multilingual). It was also updated to explicitly include conversational fragments (e.g., "Ok", "Done").

### What was intentionally not changed
1. **RefundsAndReturns**: Return requests, refund status, and cancellations were kept as a single intent because the customer goal (reversing a transaction) and the resulting support workflow are nearly identical.
2. **AccountAndPayment**: Payment failures, Prime charges, and account hacks were kept together as they all necessitate escalation to secure Account Specialists.
3. **DigitalServices**: Prime Video, Kindle, and Amazon Music were kept together as they all require technical troubleshooting workflows, rather than physical fulfillment.

### Limitations
The primary limitation discovered during the audit is the high volume of conversational fragments (e.g., "Done", "Thanks", "I sent the email", "Ok"). Because of Twitter's threading format, these isolated messages lack context and will be classified as `OTHER` or `OUT_OF_SCOPE` if analyzed in isolation. When building the classifier, we must define whether it should classify single messages in isolation, or if it should be given the full conversation history to determine the intent.


## Phase 3: Data Foundation & Baselines Decisions
- **Data Splits**: Split at the `root_id` (conversation) level into 80/10/10 Train/Val/Test. This guarantees no leakage across splits where a thread's messages are divided.
- **Weak Labels**: Due to a lack of 200k manual annotations, a keyword heuristic was used to generate weak labels for the development sets. These are explicitly NOT ground truth and will be replaced by a human-annotated Golden Set in Phase 4.
- **Leakage Prevention**: When building contextual features, the chronological thread was strictly filtered to exclude the target message's future and the brand's response. The context was restricted to the 3 immediately preceding messages to cap prompt sizes for future LLM deployment.
- **Baselines**: A Majority Class baseline and TF-IDF + Logistic Regression baselines were chosen for their deterministic behavior. The TF-IDF model was trained twice to run a context ablation study (`MESSAGE_ONLY` vs `CONVERSATION_CONTEXT`).

## Phase 4D: AUTO-HANDLE vs ESCALATE Decision Engine
- **Deterministic Rules vs LLM**: We explicitly decided to use deterministic rules (regex + thresholding) rather than a secondary LLM call to make the final escalation decision. This ensures strict compliance with safety guidelines, zero hallucination risk on high-stakes routing, and significantly lowers latency/cost. 
- **Defaulting to ESCALATE**: High-risk cases default to ESCALATE. This is a safety-oriented policy that prioritizes preventing incorrect autonomous actions over maximizing the automation rate.
- **Unsupported Account Actions**: We enforce that if the customer explicitly demands an action (e.g., "cancel my order"), the system escalates it, as the current agent architecture is informational and not connected to an external action API. We do not automatically claim actions are completed.
