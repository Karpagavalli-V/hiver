# AmazonHelp Intent Taxonomy

## 1. DeliveryStatus
### Description
Customer is asking about the location, tracking, or delay of their package, or reporting a package marked as delivered but not received.
### Inclusion criteria
- Order tracking ("Where is my package?")
- Late or delayed packages ("Supposed to arrive yesterday")
- Lost in transit
- Delivered but not received (DNR) ("App says delivered but it's not here")
### Exclusion criteria
- Complaints about *how* it was delivered (e.g., thrown over fence) -> `CourierFeedback`
### Representative examples
- "Order no. 403-7992585-3142701 was suppsd to arrive by 25/09. Item not rcivd yet."
- "Starting to get REALLY irritated with the shipping of my Amazon package. So freaking late."
### Approximate frequency
High (~35%)
### Classification difficulty
Easy (Keywords like "arrive", "delayed", "tracking" are strong signals)
### Expected support behavior
Amazon requests the user to securely verify their account via a link and then provides a tracking update or offers a replacement/refund for lost items.

---

## 2. RefundsAndReturns
### Description
Customer is inquiring about the process of returning an item, tracking a refund, or cancelling an order.
### Inclusion criteria
- "Where is my refund?"
- "How do I return this?"
- "Cancel my order"
### Exclusion criteria
- Returning an item explicitly because it is damaged -> `DamagedOrDefective`
- Returning because it's the wrong item -> `WrongItem`
### Representative examples
- "Details have already been sent. Kindly make it hassle free for me and get the refund done ASAP."
- "Spoke to ur abysmal customer service team. 6 working days for a refund?"
### Approximate frequency
Medium (~15%)
### Classification difficulty
Medium (Can be confused with damaged goods if the customer says "I want a refund because it's broken")
### Expected support behavior
Amazon provides a link to the Returns Center or explains the standard 3-5 business day processing time for refunds.

---

## 3. DamagedOrDefective
### Description
Customer received a product that is physically damaged, defective, soiled, or missing parts.
### Inclusion criteria
- "Broken item"
- "Missing pieces"
- "Box arrived crushed"
- "Not working out of the box"
### Exclusion criteria
- Item works but is not what was ordered -> `WrongItem`
### Representative examples
- "Recieved soiled and dirty product delivered by Amazon today. Worst experience as this was supposed to be a Diwali Gift"
- "And the box is damaged!!! [Image]"
### Approximate frequency
Low (~5%)
### Classification difficulty
Easy (Highly specific descriptive words like "broken", "dirty", "damaged")
### Expected support behavior
Amazon apologizes for the condition and directs the customer to the Returns/Replacements portal.

---

## 4. WrongItem
### Description
Customer received an incorrect product, wrong size, wrong color, or wrong version of an item.
### Inclusion criteria
- "I ordered an iPhone X and got an 8"
- "Wrong color sent"
- "Not what was pictured"
### Exclusion criteria
- Item is what they ordered but it is broken -> `DamagedOrDefective`
### Representative examples
- "Ordered cases for our new iPhone X and sent me iPhone 8 cases for BOTH ones. NOT THE SAME PHONE!"
### Approximate frequency
Low (~2%)
### Classification difficulty
Easy (Usually explicitly states "wrong item" or "ordered X but got Y")
### Expected support behavior
Amazon apologizes for the mix-up and offers a free replacement or return label.

---

## 5. CourierFeedback
### Description
Customer is providing feedback or complaints about the delivery driver's behavior, instructions ignored, or where the package was left.
### Inclusion criteria
- "Driver threw my package"
- "Left in the rain"
- "Didn't ring doorbell"
- "Delivery instructions ignored"
### Exclusion criteria
- Package is completely lost without a delivery scan -> `DeliveryStatus`
### Representative examples
- "READ MY DELIVERY INSTRUCTUONS! I SAID TO LEAVE THE PARCEL OUT OF SIGHT BEHIND THE BIN. I DID NOT SAY DUMP IT IN FRONT OF THE DOOR!!!!!!!!!"
- "On the phone with @AmazonHelp again for another botched delivery. They have no idea what they are doing."
### Approximate frequency
Medium (~10%)
### Classification difficulty
Medium (Often overlaps with DeliveryStatus if they complain about a late courier)
### Expected support behavior
Amazon asks for the tracking number to pass feedback to the specific carrier/delivery station.

---

## 6. AccountAndPayment
### Description
Issues related to Amazon Prime subscription fees, account security, unauthorized purchases, or payment failures.
### Inclusion criteria
- "Charged for Prime without asking"
- "Account hacked"
- "Gift card not working"
- "Promo code failed"
### Exclusion criteria
- Refund for a physical item -> `RefundsAndReturns`
### Representative examples
- "how long does it take to investigate an acct? Acct was jacked & I need access to it. Haven't heard anything in almost 2 wks."
- "I've been charged by you but haven't bought anything .. Can u not"
### Approximate frequency
Medium (~10%)
### Classification difficulty
Medium (Financial terms can overlap with Refunds)
### Expected support behavior
Amazon directs the user to an Account Specialist via a secure form or phone call.

---

## 7. DigitalServices
### Description
Technical support for Amazon digital products like Prime Video, Kindle, Amazon Music, or Fire TV.
### Inclusion criteria
- "Video streaming is buffering"
- "Kindle book won't download"
- "Missing subtitles on a movie"
### Exclusion criteria
- Questions about billing for these services -> `AccountAndPayment`
### Representative examples
- "I download one movie but language not in hindi"
- "I’ve bought a kindle book instead of a real book, can I change it please?"
### Approximate frequency
Low (~5%)
### Classification difficulty
Easy (Contains specific entities like "Kindle", "Movie", "Music")
### Expected support behavior
Amazon provides troubleshooting steps (e.g., "clear cache", "restart app") or links to specific device support.

---

## 8. CustomerServiceEscalation
### Description
Customer is angry about a previous interaction with Amazon support, waiting for a promised callback, or demanding a manager.
### Inclusion criteria
- "Been on hold for 30 mins"
- "Agent hung up on me"
- "No one replied to my email"
- "Worst customer service"
### Exclusion criteria
- General frustration about an order delay -> `DeliveryStatus`
### Representative examples
- "The fifth try worked, Finally got to talk to someone who helped. Five calls and an hour on the phone."
- "Reported more than 20 times in last 20 days... poor Customer support"
### Approximate frequency
Medium (~10%)
### Classification difficulty
Hard (Customers usually embed this within another complaint, e.g., "My order is late AND your reps are useless")
### Expected support behavior
Amazon apologizes for the poor experience and offers to personally look into the ticket via DM.

---

## 9. OTHER
### Description
Messages that do not fit into actionable support categories, including praise, spam, conversational fragments, or overly vague complaints. Non-English messages should ONLY be placed here if their underlying intent cannot be determined.
### Inclusion criteria
- "Thank you!"
- "Great job"
- "Help me" (Too vague)
- Conversational fragments ("Ok", "Done", "Will do")
### Exclusion criteria
- Vague complaints that mention "my order" (should be investigated)
- Non-English messages that clearly express one of the other intents
### Representative examples
- "Great job by @AmazonHelp ! Order was supposed to come by 24 oct, got it delivered today. Real quick. Impressive."
- "Ah. Danke, das erklärt es natürlich."
### Approximate frequency
Medium (~8%)
### Classification difficulty
Easy
### Expected support behavior
Amazon says "You're welcome!" or provides a link to standard help pages.

---

## Confusing Intent Pairs

### DeliveryStatus vs CourierFeedback
- **Distinction**: `DeliveryStatus` is about *when* or *if* a package will arrive. `CourierFeedback` is about *how* it was handled by the driver.
- **Common Ambiguity**: "My package says delivered but I can't find it."
- **Classification Signals**: If the customer mentions the driver's specific actions ("didn't knock", "left in rain"), it's `CourierFeedback`. If they are just confused about the location, it's `DeliveryStatus`.

### DamagedOrDefective vs RefundsAndReturns
- **Distinction**: A damaged item is the *cause*. A refund is the *resolution*.
- **Common Ambiguity**: "My item is broken so I want my money back."
- **Classification Signals**: Always prefer the cause. If physical damage or a defect is explicitly mentioned, map to `DamagedOrDefective` so the agent knows to address the product quality.

### AccountAndPayment vs DigitalServices
- **Distinction**: One is about billing, the other is about technical functionality.
- **Common Ambiguity**: "I was charged $12.99 for a movie that won't play."
- **Classification Signals**: If the core issue preventing usage is technical (won't play), it's `DigitalServices`. If it's a dispute over the charge, it's `AccountAndPayment`.
