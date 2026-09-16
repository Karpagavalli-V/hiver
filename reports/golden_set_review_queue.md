# Golden Set Review Queue

> **Methodology Note**: The labels present in the Golden Set currently represent AI-assisted pre-annotations. To maximize human review efficiency and evaluation validity, this queue specifically prioritizes cases where a human correction is most likely to affect the final benchmark accuracy (e.g., safety issues, ambiguous intents, unsupported automation routing). Straightforward cases require no manual review and are placed in Priority 3.

## Summary
- **Total Rows**: 200
- **Priority 1 (MUST REVIEW)**: 113
- **Priority 2 (REVIEW IF TIME)**: 85
- **Priority 3 (NO MANUAL REVIEW NEEDED)**: 2

### Counts by Review Reason
- Missing/insufficient context that makes the proposed judgment unreliable: 87
- OTHER where the message appears to contain an actual support issue: 51
- MEDIUM confidence: 43
- LOW confidence: 42
- Unauthorized financial/payment issue: 22
- Potentially incorrect AUTO-HANDLE decision: 18
- Legal/safety/injury/threat issue: 9
- Security/account compromise issue: 9
- Explicit manager/supervisor/human escalation or repeated unresolved support issue: 8
- Potentially incorrect intent based on the customer message/context: 5
- Potentially incorrect ESCALATE decision: 2

### Counts by Proposed Intent (Full Dataset)
- OTHER: 98
- DeliveryStatus: 41
- RefundsAndReturns: 14
- DamagedOrDefective: 12
- AccountAndPayment: 12
- WrongItem: 8
- DigitalServices: 6
- CustomerServiceEscalation: 6
- CourierFeedback: 3

### Counts by Proposed AUTO-HANDLE/ESCALATE (Full Dataset)
- AUTO-HANDLE: 179
- ESCALATE: 21

### Counts by Proposed Reply Quality (Full Dataset)
- 4: 104
- 3: 96

## Priority 1 — MUST REVIEW

### G-1002
**Customer Message**: `@AmazonHelp I spoke to one of your agents tonight on the phone and he went above and beyond (even a follow up email)! Anyway to ID so I can fill out a survey of some sort??`

**Context**:
```text
*Empty Context*
```

- **Proposed Intent**: OTHER
- **Proposed Confidence**: LOW
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 3
- **Reasons Flagged**:
  - Explicit manager/supervisor/human escalation or repeated unresolved support issue
  - Potentially incorrect AUTO-HANDLE decision
  - Missing/insufficient context that makes the proposed judgment unreliable

---

### G-1004
**Customer Message**: `Wow! @115830 this packaging job is atrocious. I don’t order books for them to arrive damaged 😡 https://t.co/sJNSq2qqM8`

**Context**:
```text
*Empty Context*
```

- **Proposed Intent**: DamagedOrDefective
- **Proposed Confidence**: MEDIUM
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 3
- **Reasons Flagged**:
  - Legal/safety/injury/threat issue
  - Potentially incorrect AUTO-HANDLE decision
  - Missing/insufficient context that makes the proposed judgment unreliable

---

### G-1005
**Customer Message**: `So far @115821 has failed to respond to my oil covered package and ruined game.`

**Context**:
```text
*Empty Context*
```

- **Proposed Intent**: DeliveryStatus
- **Proposed Confidence**: MEDIUM
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 3
- **Reasons Flagged**:
  - Missing/insufficient context that makes the proposed judgment unreliable

---

### G-1008
**Customer Message**: `@115830 a few bad delivery drivers really spoiling the Amazon brand 😢 ...please be more selective in your delivery services`

**Context**:
```text
*Empty Context*
```

- **Proposed Intent**: DeliveryStatus
- **Proposed Confidence**: MEDIUM
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 3
- **Reasons Flagged**:
  - Missing/insufficient context that makes the proposed judgment unreliable

---

### G-1011
**Customer Message**: `@AmazonHelp Another failed attempt st delivery and the number given by you of the agent incorrect. Problems still oresists! Shameful @173609`

**Context**:
```text
[181479] @8623 @AmazonHelp atrocious service, clueless customer care. Absolute waste. Never ever @348 @120033 @173609 https://t.co/5QeeunWH1e\n[181479] @8623 @AmazonHelp @348 @120033 @173609 @AmazonHelp @171152 bad service, crappy customer care with a discount of Rs100 to cover poor face.Shameful @173609 @348\n[AmazonHelp] @181479 I'm sorry for the trouble. Could you please confirm if you've provided your details in the link mentioned earlier? ^AU\n[181479] @AmazonHelp As suggested earlier it has been provided\n[AmazonHelp] @181479 As you've shared your details, we'll work on it and get back to you at the earliest. ^HN\n[181479] @AmazonHelp You have refunded it!But i am merely stating my views on it.Yet i have places another order.Lets see how u do this @115850 @348\n[181479] @AmazonHelp @115850 @348 Well am sure it does help your more than customers cuz soon u wont have any. Have ordered again for the same product. Lets see what comes\n[AmazonHelp] @181479 We'll surely work on your feedback. ^HK
```

- **Proposed Intent**: DeliveryStatus
- **Proposed Confidence**: MEDIUM
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 4
- **Reasons Flagged**:
  - Explicit manager/supervisor/human escalation or repeated unresolved support issue
  - Potentially incorrect AUTO-HANDLE decision

---

### G-1012
**Customer Message**: `@115821 Amazon delivering packages today at driveway. Didn't bother putting by front door or behind brick wall.  At least they didn't get stolen.  Guess they are trying to get everyone to get their home access kit installed.  Glad I saw them before it was dark. https://t.co/AJmHLJTVlJ`

**Context**:
```text
*Empty Context*
```

- **Proposed Intent**: CourierFeedback
- **Proposed Confidence**: HIGH
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: ESCALATE
- **Proposed Reply Quality**: 3
- **Reasons Flagged**:
  - Missing/insufficient context that makes the proposed judgment unreliable

---

### G-1013
**Customer Message**: `@AmazonHelp My preorder was mishandled.  Was escalated to a PO Box!? #xboxonex #projectscorpio #amazon #preorder #fail`

**Context**:
```text
*Empty Context*
```

- **Proposed Intent**: OTHER
- **Proposed Confidence**: LOW
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 3
- **Reasons Flagged**:
  - Missing/insufficient context that makes the proposed judgment unreliable

---

### G-1014
**Customer Message**: `I’m fearful @115821 is slipping. Recently, we’ve consistently had our packages arrive in 3-4 days instead of 2, including the most recent.`

**Context**:
```text
*Empty Context*
```

- **Proposed Intent**: OTHER
- **Proposed Confidence**: LOW
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 3
- **Reasons Flagged**:
  - Missing/insufficient context that makes the proposed judgment unreliable

---

### G-1017
**Customer Message**: `@AmazonHelp This link requires a log in password we have neither please for a contact telephone number and identify an individual to address this please`

**Context**:
```text
[295773] Please contact me re. unlawful payment from my account - never subscribed for service. Will need to report to Gardaí.  Amazon Prime Ireland\n[AmazonHelp] @295773 If you have signed up for Amazon Prime, you can manage and cancel the subscription here: https://t.co/EMoca4Sfya. ^MC\n[295773] @AmazonHelp Have not signed up for Amazon Prime services in any shape or form. Please forward a contact no and person who can rectify and refund this.\n[AmazonHelp] @295773 You'll be able to cancel the membership and reverse the charges here: https://t.co/qHCVytpucE Let us know if this helps! ^ZW\n[295773] @AmazonHelp We have no membership - we are not members.\n[AmazonHelp] @295773 We'd like to take a look at this with you. Please call or chat with us here: https://t.co/JzP7hlA23B ^MH
```

- **Proposed Intent**: AccountAndPayment
- **Proposed Confidence**: MEDIUM
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: ESCALATE
- **Proposed Reply Quality**: 4
- **Reasons Flagged**:
  - Security/account compromise issue

---

### G-1022
**Customer Message**: `@AmazonHelp I did it but still not showing recharge order`

**Context**:
```text
[259026] @115850 I recharged idea number through amazonpay and yet not received any confirmation message\n[259026] @115850 How long it will take ?? I am waiting for last 20 min\n[AmazonHelp] @259026 I get your concern about order confirmation. Please reach us from here: https://t.co/rS49hgaADF, we'll check your details and help you. ^SV\n[259026] @AmazonHelp Not showing any order placed by when I recharged it was showing successful\n[AmazonHelp] @259026 That's odd. Please reach us from the link provided. We'll check your details and help you further. Be assured. ^SV
```

- **Proposed Intent**: OTHER
- **Proposed Confidence**: LOW
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 4
- **Reasons Flagged**:
  - Unauthorized financial/payment issue

---

### G-1024
**Customer Message**: `@AmazonHelp my friend subscribed for Prime videos. Amt. has been deducted frm her accnt. But prime subscription is still not activated.`

**Context**:
```text
*Empty Context*
```

- **Proposed Intent**: OTHER
- **Proposed Confidence**: LOW
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 3
- **Reasons Flagged**:
  - Missing/insufficient context that makes the proposed judgment unreliable

---

### G-1026
**Customer Message**: `@115850 item not yet received, Order date 26-Nov-2017 Order # 406-8211914-5496311
Tracking #: 350134473493`

**Context**:
```text
*Empty Context*
```

- **Proposed Intent**: DeliveryStatus
- **Proposed Confidence**: MEDIUM
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 3
- **Reasons Flagged**:
  - Missing/insufficient context that makes the proposed judgment unreliable

---

### G-1027
**Customer Message**: `#apptreasurehunt
 @115850 
Give me happiness
Thank you Amazon ☺ https://t.co/UWOx7EpKuj`

**Context**:
```text
*Empty Context*
```

- **Proposed Intent**: OTHER
- **Proposed Confidence**: MEDIUM
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 3
- **Reasons Flagged**:
  - Missing/insufficient context that makes the proposed judgment unreliable

---

### G-1028
**Customer Message**: `After @115817 mucked it @115821 delivers the Elvis; open box &amp; “shake-rattle-roll” broken product guess I’m screwed for weekend.`

**Context**:
```text
*Empty Context*
```

- **Proposed Intent**: DamagedOrDefective
- **Proposed Confidence**: MEDIUM
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 3
- **Reasons Flagged**:
  - Missing/insufficient context that makes the proposed judgment unreliable

---

### G-1032
**Customer Message**: `https://t.co/V0S2BNxmhi
@AmazonHelp 
I wrote to Amazon asking why an image and such for my paperback isn't showing. This does show on Kindle`

**Context**:
```text
*Empty Context*
```

- **Proposed Intent**: DigitalServices
- **Proposed Confidence**: MEDIUM
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 3
- **Reasons Flagged**:
  - Missing/insufficient context that makes the proposed judgment unreliable

---

### G-1034
**Customer Message**: `@AmazonHelp I just got a $59.99 charge for Amazon Digital Downloads, can you help me understand what that is?`

**Context**:
```text
*Empty Context*
```

- **Proposed Intent**: AccountAndPayment
- **Proposed Confidence**: MEDIUM
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: ESCALATE
- **Proposed Reply Quality**: 3
- **Reasons Flagged**:
  - Unauthorized financial/payment issue
  - Missing/insufficient context that makes the proposed judgment unreliable

---

### G-1035
**Customer Message**: `@AmazonHelp Thanks. It was made unnecessarily difficult to find cancel option but I’m not surprised. Congrats, you gained squeeze a few months of fees!`

**Context**:
```text
[327456] @115830 I keep getting charged for Amazon Prime but when I try to cancel it says I don’t have an account. How can I stop this happening?\n[AmazonHelp] @327456 I'm sorry about the unexpected charge! Have you taken a look here: https://t.co/F1XXZG53JF to help locate this charge? ^FR
```

- **Proposed Intent**: RefundsAndReturns
- **Proposed Confidence**: MEDIUM
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 4
- **Reasons Flagged**:
  - Unauthorized financial/payment issue

---

### G-1036
**Customer Message**: `My reaction when Amazon took $99 from my bank account when I was just trying to see the details of 2 day shipping I'm mad https://t.co/u3jn7JSqka`

**Context**:
```text
*Empty Context*
```

- **Proposed Intent**: AccountAndPayment
- **Proposed Confidence**: MEDIUM
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: ESCALATE
- **Proposed Reply Quality**: 3
- **Reasons Flagged**:
  - Unauthorized financial/payment issue
  - Missing/insufficient context that makes the proposed judgment unreliable

---

### G-1037
**Customer Message**: `@AmazonHelp I had my account locked on previous order and provided address and had my account open, this order again same thing.`

**Context**:
```text
[305551] @AmazonHelp I had my account locked yesterday and provided the info and got it open. Again, my account is locked\n[AmazonHelp] @305551 I'm very sorry for the issues with your account. Have you received an e-mail from our Account Specialist regarding this? ^CL
```

- **Proposed Intent**: OTHER
- **Proposed Confidence**: LOW
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 4
- **Reasons Flagged**:
  - Security/account compromise issue
  - Potentially incorrect AUTO-HANDLE decision

---

### G-1039
**Customer Message**: `@115850 I ordered SanDisk 32GB on 4th October 2017 Order No (407-3595273-8505936) they delayed my ordered No Home visit and order delayed.`

**Context**:
```text
*Empty Context*
```

- **Proposed Intent**: OTHER
- **Proposed Confidence**: LOW
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 3
- **Reasons Flagged**:
  - Missing/insufficient context that makes the proposed judgment unreliable

---

### G-1042
**Customer Message**: `@AmazonHelp Update! It’s still not here!!! I doubt it’ll be here by 8 since it hasn’t been shipped yet! And they had a good 4 days to prepare the product to ship! I paid good money for the day one shipping. Amazon please help!! https://t.co/i7WnBMWpP9`

**Context**:
```text
[201328] .@115821 why does it say its coming today but hasn’t shipped I also paid for one day shipping which was an extra 10 bucks I’m mad😠 https://t.co/oByM3rwf8w\n[AmazonHelp] @201328 Orders can ship and be delivered within the same day. Please let us know if it has not been delivered by the date shown. ^TH
```

- **Proposed Intent**: DeliveryStatus
- **Proposed Confidence**: MEDIUM
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 4
- **Reasons Flagged**:
  - Unauthorized financial/payment issue
  - Potentially incorrect intent based on the customer message/context

---

### G-1043
**Customer Message**: `Hi @AmazonHelp , my order id is 406-5211780-7866716, it is in hub from last 36 hours &amp; on hold, can u contact them and make it deliver ?`

**Context**:
```text
*Empty Context*
```

- **Proposed Intent**: CustomerServiceEscalation
- **Proposed Confidence**: MEDIUM
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: ESCALATE
- **Proposed Reply Quality**: 3
- **Reasons Flagged**:
  - Explicit manager/supervisor/human escalation or repeated unresolved support issue
  - Missing/insufficient context that makes the proposed judgment unreliable

---

### G-1044
**Customer Message**: `@AmazonHelp @115850 @AmazonHelp what is this?? More than 1 month over package not pick up.    What to do with this damaged item??`

**Context**:
```text
[348159] @115850 @AmazonHelp Struggling for return my package from 25.09.17, but the same not picked yet. Number of times talked had with CC but ..\n[AmazonHelp] @348159 https://t.co/5p7JdZlcy4 so that we can get in touch with you. (2/2)^VM\n[348159] @AmazonHelp @115850 should I through the package in dustbin. Now almost 1 month has over. Nobody came to pick up the return package. Shocking AMAZON..\n[AmazonHelp] @348159 Apologies for the delay. Please share your details in the link given earlier and we'll be sure to help you. ^ZH
```

- **Proposed Intent**: DeliveryStatus
- **Proposed Confidence**: MEDIUM
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 4
- **Reasons Flagged**:
  - Legal/safety/injury/threat issue
  - Potentially incorrect AUTO-HANDLE decision

---

### G-1047
**Customer Message**: `Wow, the opening of Wolfenstein II is genuinely disturbing. At the very least I need to go give my dog a hug.`

**Context**:
```text
*Empty Context*
```

- **Proposed Intent**: OTHER
- **Proposed Confidence**: LOW
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 3
- **Reasons Flagged**:
  - Missing/insufficient context that makes the proposed judgment unreliable

---

### G-1048
**Customer Message**: `@AmazonHelp That the order should not go through because the account is now locked`

**Context**:
```text
[348599] @115821 your customer service sucks.\n[AmazonHelp] @348599 I'm sorry you've had a poor experience with our Support. We'd like to help, if we can. Would you tell us what's going on? ^AM\n[348599] @AmazonHelp My order got placed on hold because for the some reason it was taken as a risk or something. I called askew for a supervision waited 30 mins\n[AmazonHelp] @348599 Did we connect you to a supervisor? Did we mention letting our Account Specialists know that this order was placed by you? ^MV\n[348599] @AmazonHelp Yes. It took over 30 minutes. No I was already upset so I wanted it canceled right away.\n[AmazonHelp] @348599 Understood. What was the outcome of the phone call? Were we able to provide any options or further information? ^BH
```

- **Proposed Intent**: OTHER
- **Proposed Confidence**: LOW
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 4
- **Reasons Flagged**:
  - Security/account compromise issue
  - Potentially incorrect AUTO-HANDLE decision

---

### G-1049
**Customer Message**: `@AmazonHelp your new tracking method sucks since it does not provide accurate information. Give back the tracking numbers!!`

**Context**:
```text
*Empty Context*
```

- **Proposed Intent**: DeliveryStatus
- **Proposed Confidence**: MEDIUM
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 3
- **Reasons Flagged**:
  - Missing/insufficient context that makes the proposed judgment unreliable

---

### G-1050
**Customer Message**: `@AmazonHelp Take responsibility of damaged occured in my home due to ur false informatio @115851.

What a pathetic company you are @115850`

**Context**:
```text
[338252] False Information on @115850 website lead a blast in my kitchen and amazon doesn't want to take responsibility. @115851 @120320 @146956 https://t.co/tgEgimXGAK\n[AmazonHelp] @338252 Apologies for the ordeal Chitransh. Please share your details here: https://t.co/GIJyeYqKE0 and I'll get back to you. ^HN\n[338252] @AmazonHelp Every thing has been shared already email was sent at cs reply. Pls check internally n confirm how do u plan to compensate for the damages\n[AmazonHelp] @338252 If you have shared your details, our team will surely get back to you with an update soon. Request you to wait. ^NK\n[338252] @AmazonHelp Yes, they came back saying we r nt responsible even if u wud hv died in the blast because of false information on amazon website @115851\n[AmazonHelp] @338252 I'm sorry to know this, Chitransh. You will receive an update from the social media team shortly. Appreciate your patience. ^MP\n[338252] @AmazonHelp I will wait for it. In case i dont get a resolution for this i am going to file a case against ur company for false information n negligence\n[AmazonHelp] @338252 Thanks for understanding, Chitransh. Our team will surely get back to you once they have an update. ^NK\n[338252] @AmazonHelp You team ws suppose to reach out with a solution. You should resolve these issues at priority @115850 @115851\n[AmazonHelp] @338252 I just checked and we haven't received your details yet. Kindly share your details here: https://t.co/beaaDm0muc ^GK\n[338252] @AmazonHelp I have shared the details once again please check and confirm if you have got the same.\n[AmazonHelp] @338252 We've received your details and we are working on it. We'll reach out to you soon. ^GK
```

- **Proposed Intent**: DamagedOrDefective
- **Proposed Confidence**: MEDIUM
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 4
- **Reasons Flagged**:
  - Legal/safety/injury/threat issue
  - Potentially incorrect AUTO-HANDLE decision

---

### G-1051
**Customer Message**: `Item from @115830 just left on the doorstep and the doorbell rung!  Hope that third-party driver gets the push!`

**Context**:
```text
*Empty Context*
```

- **Proposed Intent**: CourierFeedback
- **Proposed Confidence**: MEDIUM
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 3
- **Reasons Flagged**:
  - Missing/insufficient context that makes the proposed judgment unreliable

---

### G-1053
**Customer Message**: `@AmazonHelp Here is the delivery info the annoying thing is the parcel would have fit in my post box, luckily my item is not damaged https://t.co/aDhCEcsyuC`

**Context**:
```text
[672167] @115830 my parcel thrown over the fence AGAIN luckily I found it albeit a day later #delivery #notacceptable #poorservice #nothappy #customer why do I pay my #prime #membership\n[AmazonHelp] @672167 Hi Angie, I'm sorry to hear about this. Was your item damaged at all? ^PJ\n[672167] @AmazonHelp Hi I have not opened it as I was on my way out, I will check when I get home\n[AmazonHelp] @672167 Which carrier delivered your parcel? https://t.co/aaDyEz1VgE. Keep us updated! ^CN
```

- **Proposed Intent**: DeliveryStatus
- **Proposed Confidence**: MEDIUM
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 4
- **Reasons Flagged**:
  - Legal/safety/injury/threat issue
  - Potentially incorrect AUTO-HANDLE decision

---

### G-1054
**Customer Message**: `@AmazonHelp you gotta get your shit together here in SoCal, two orders and this second one is damaged on arrival`

**Context**:
```text
*Empty Context*
```

- **Proposed Intent**: DamagedOrDefective
- **Proposed Confidence**: MEDIUM
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 3
- **Reasons Flagged**:
  - Legal/safety/injury/threat issue
  - Potentially incorrect AUTO-HANDLE decision
  - Missing/insufficient context that makes the proposed judgment unreliable

---

### G-1056
**Customer Message**: `Dear @115830 , how long will you be investigating unauthorised payment made on my wife's credit card? Was expecting an update 48 hrs ago 😡`

**Context**:
```text
*Empty Context*
```

- **Proposed Intent**: AccountAndPayment
- **Proposed Confidence**: MEDIUM
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: ESCALATE
- **Proposed Reply Quality**: 3
- **Reasons Flagged**:
  - Unauthorized financial/payment issue
  - Missing/insufficient context that makes the proposed judgment unreliable

---

### G-1060
**Customer Message**: `@115830 When you pay for prime and your delivery drivers can't find an easy location  🤣 useless`

**Context**:
```text
*Empty Context*
```

- **Proposed Intent**: DeliveryStatus
- **Proposed Confidence**: MEDIUM
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 3
- **Reasons Flagged**:
  - Missing/insufficient context that makes the proposed judgment unreliable

---

### G-1061
**Customer Message**: `@AmazonHelp hello, can you please tell me why my order was canceled and my account closed?`

**Context**:
```text
*Empty Context*
```

- **Proposed Intent**: OTHER
- **Proposed Confidence**: MEDIUM
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 3
- **Reasons Flagged**:
  - Missing/insufficient context that makes the proposed judgment unreliable

---

### G-1062
**Customer Message**: `@137605 @116928 ¿Me pueden explicar como dan como ausente a un reparto en un HOTEL?`

**Context**:
```text
*Empty Context*
```

- **Proposed Intent**: OTHER
- **Proposed Confidence**: LOW
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 3
- **Reasons Flagged**:
  - Missing/insufficient context that makes the proposed judgment unreliable

---

### G-1064
**Customer Message**: `@AmazonHelp WAITING FOR THE REPLY FOR THE DATE AND TIME REIMBURSED THE MONEY TO MY ACCOUNT`

**Context**:
```text
[258304] @AmazonHelp O.No4__credit_card__ Dt.18/05/2017 for Rs.1699 sent on 20/
```

- **Proposed Intent**: OTHER
- **Proposed Confidence**: LOW
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 3
- **Reasons Flagged**:
  - Unauthorized financial/payment issue

---

### G-1065
**Customer Message**: `@AmazonHelp It's just an email asking for feedback on support quality.`

**Context**:
```text
[171433] .@115850 won't do return-&amp;-refund for Bluedio Hurricane T2 headphones, so am stuck with sub-par audio experience &amp; no volume control 😨😢\n[AmazonHelp] @171433 We'd like to check this, kindly share your details here:  https://t.co/GIJyeYqKE0 ^SG\n[171433] @AmazonHelp Responded. Also, I just returned the item to Amazon pickup.\n[AmazonHelp] @171433 the same for further assistance. (2/2)^AU
```

- **Proposed Intent**: OTHER
- **Proposed Confidence**: LOW
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 4
- **Reasons Flagged**:
  - Unauthorized financial/payment issue

---

### G-1067
**Customer Message**: `@115821, why do I have to do work when you send the wrong item...It's also personal care and there's no way of knowing if its been used...`

**Context**:
```text
*Empty Context*
```

- **Proposed Intent**: WrongItem
- **Proposed Confidence**: MEDIUM
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 3
- **Reasons Flagged**:
  - Missing/insufficient context that makes the proposed judgment unreliable

---

### G-1069
**Customer Message**: `@AmazonHelp Hi. I have amazon Prime student and the payment is scheduled in April. I received a charge today for £8 for no reason.`

**Context**:
```text
*Empty Context*
```

- **Proposed Intent**: AccountAndPayment
- **Proposed Confidence**: MEDIUM
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: ESCALATE
- **Proposed Reply Quality**: 3
- **Reasons Flagged**:
  - Unauthorized financial/payment issue
  - Missing/insufficient context that makes the proposed judgment unreliable

---

### G-1071
**Customer Message**: `@AmazonHelp ordered woodland shoes n got delivered just now, Got totally damaged shoes… pls check images, pls look into this @115850 https://t.co/2PQCKft2my`

**Context**:
```text
*Empty Context*
```

- **Proposed Intent**: DamagedOrDefective
- **Proposed Confidence**: MEDIUM
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 3
- **Reasons Flagged**:
  - Legal/safety/injury/threat issue
  - Potentially incorrect AUTO-HANDLE decision
  - Missing/insufficient context that makes the proposed judgment unreliable

---

### G-1072
**Customer Message**: `Ok @115821 #amazon, the USPS #usps took the package from my mail box after you stuck it there, and now I have to... https://t.co/e42JFkxEYt`

**Context**:
```text
*Empty Context*
```

- **Proposed Intent**: DeliveryStatus
- **Proposed Confidence**: MEDIUM
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 3
- **Reasons Flagged**:
  - Missing/insufficient context that makes the proposed judgment unreliable

---

### G-1073
**Customer Message**: `@AmazonHelp I called. Still no real resolution. Waste of time. Should have drove to Target.`

**Context**:
```text
[608467] My last 3+ @115821 Prime orders have been late.  Is this going to be an ongoing theme or is this just some fluke.  I need to know if I can no longer count on your delivery dates @AmazonHelp\n[AmazonHelp] @608467 Sorry for the delays, Jennifer! We aim to get your order to you in the time frame we promise, although unforeseen circumstances could occur to cause these. Have you noticed delays with a specific courier? ^JZ\n[608467] @AmazonHelp It's @115821 not shipping in time. Not courier delays.\n[AmazonHelp] @608467 We'd like to document your feedback, Jennifer. When you get a moment, let's continue working together in real-tme, via phone or chat, here: https://t.co/JzP7hlA23B ^FD
```

- **Proposed Intent**: OTHER
- **Proposed Confidence**: LOW
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 4
- **Reasons Flagged**:
  - Explicit manager/supervisor/human escalation or repeated unresolved support issue
  - Potentially incorrect AUTO-HANDLE decision

---

### G-1074
**Customer Message**: `@115830 ordered item using Amazon drop retailer. collection set up for 3 party to collect. collection refused. wedding surprise ruined`

**Context**:
```text
*Empty Context*
```

- **Proposed Intent**: DamagedOrDefective
- **Proposed Confidence**: MEDIUM
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 3
- **Reasons Flagged**:
  - Missing/insufficient context that makes the proposed judgment unreliable

---

### G-1077
**Customer Message**: `@115850  bought a mobile using city Bank credit card on oct6,17.I haven't received 10% cashback https://t.co/pcNXcNJHJN long does it take?`

**Context**:
```text
*Empty Context*
```

- **Proposed Intent**: AccountAndPayment
- **Proposed Confidence**: HIGH
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: ESCALATE
- **Proposed Reply Quality**: 3
- **Reasons Flagged**:
  - Unauthorized financial/payment issue
  - Missing/insufficient context that makes the proposed judgment unreliable

---

### G-1080
**Customer Message**: `@AmazonHelp Yesterday morning but since then there have have been 2 more failures by Amazon one actually theft of money by amazon that I take see`

**Context**:
```text
[522741] @AmazonHelp Can I have a contact telephone number for your Executive Customer Relations Complaint team. I have an open complaint there\n[AmazonHelp] @522741 Hi, please reply to the email from the agent dealing with your case and request a call back. Thanks! ^AT\n[522741] @AmazonHelp Its getting rather annoying as he isnt reading the emails &amp; dealing with the multiple issues. I need for him to read all my emails &amp; contact\n[AmazonHelp] @522741 sorry to hear that, the best thing to do is repond to the email and confirm the issues you are experiencing. ^AS
```

- **Proposed Intent**: OTHER
- **Proposed Confidence**: LOW
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 4
- **Reasons Flagged**:
  - Unauthorized financial/payment issue

---

### G-1081
**Customer Message**: `What the fuck Amazon, there is no mail room here, where is my shit! https://t.co/ICWgeJFWub`

**Context**:
```text
*Empty Context*
```

- **Proposed Intent**: DeliveryStatus
- **Proposed Confidence**: MEDIUM
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 3
- **Reasons Flagged**:
  - Potentially incorrect intent based on the customer message/context
  - Missing/insufficient context that makes the proposed judgment unreliable

---

### G-1082
**Customer Message**: `Testando o Prime Video pra assistir a tão comentada American Gods. Tô confiando em você @117086!`

**Context**:
```text
*Empty Context*
```

- **Proposed Intent**: DigitalServices
- **Proposed Confidence**: MEDIUM
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 3
- **Reasons Flagged**:
  - Missing/insufficient context that makes the proposed judgment unreliable

---

### G-1083
**Customer Message**: `@115821 you delivered someone’s huge package to our house incorrectly &amp; need to come pick it up. Thx!`

**Context**:
```text
*Empty Context*
```

- **Proposed Intent**: DeliveryStatus
- **Proposed Confidence**: MEDIUM
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 3
- **Reasons Flagged**:
  - Missing/insufficient context that makes the proposed judgment unreliable

---

### G-1084
**Customer Message**: `@116928 tiene que parar de “garantizar” el día de entrega de tu pedido.  Ha sido incorrecta 3 de mis últimas 5 pedidos. #logisticsfail`

**Context**:
```text
*Empty Context*
```

- **Proposed Intent**: DeliveryStatus
- **Proposed Confidence**: MEDIUM
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 3
- **Reasons Flagged**:
  - Potentially incorrect intent based on the customer message/context
  - Missing/insufficient context that makes the proposed judgment unreliable

---

### G-1085
**Customer Message**: `When you use Amazon prime so your mum's birthday present gets here on time, but you get an email saying it will be delayed for two days 😂`

**Context**:
```text
*Empty Context*
```

- **Proposed Intent**: OTHER
- **Proposed Confidence**: LOW
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 3
- **Reasons Flagged**:
  - Missing/insufficient context that makes the proposed judgment unreliable

---

### G-1086
**Customer Message**: `@115821 What is the use to contact you there after you block an account and require sign in for contacting you? you're are upsetting clients https://t.co/9HjwAKrAKm`

**Context**:
```text
*Empty Context*
```

- **Proposed Intent**: OTHER
- **Proposed Confidence**: LOW
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 3
- **Reasons Flagged**:
  - Missing/insufficient context that makes the proposed judgment unreliable

---

### G-1087
**Customer Message**: `@AmazonHelp Well someone is using my email to make there amazon account without my authorization, when I called your support... they questioned why I was even calling and to just "deal with it" 
That's the whole reason I called
So I get a hold of a manager and...`

**Context**:
```text
[564196] @115821 has the WORST customer service over the phone.\n[AmazonHelp] @564196 I'm very sorry to hear you have had a poor experience! This is not the serice we strive for! Without providing personal or account details, could you tell us a little more about what's going on? ^HM
```

- **Proposed Intent**: CustomerServiceEscalation
- **Proposed Confidence**: MEDIUM
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: ESCALATE
- **Proposed Reply Quality**: 4
- **Reasons Flagged**:
  - Explicit manager/supervisor/human escalation or repeated unresolved support issue

---

### G-1088
**Customer Message**: `@AmazonHelp I just order a item it was blue a differnt shape and it’s not what I ordered.`

**Context**:
```text
*Empty Context*
```

- **Proposed Intent**: WrongItem
- **Proposed Confidence**: MEDIUM
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 3
- **Reasons Flagged**:
  - Missing/insufficient context that makes the proposed judgment unreliable

---

### G-1090
**Customer Message**: `@AmazonHelp wenn ich AmazonPrime abschließe um ein Paket per Premiumversand asap zu bekommen, dass dann aber nicht passiert, bekomme ich von Euch die Kosten für Prime erstattet?`

**Context**:
```text
*Empty Context*
```

- **Proposed Intent**: OTHER
- **Proposed Confidence**: LOW
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 3
- **Reasons Flagged**:
  - Missing/insufficient context that makes the proposed judgment unreliable

---

### G-1091
**Customer Message**: `@AmazonHelp ich kann es beheben (bankeinzug wieder auswählen) dann ist es grün, wenn ich neu drauf gehe ist wieder zahlungsart falsch https://t.co/Vx8EujAEWW`

**Context**:
```text
*Empty Context*
```

- **Proposed Intent**: OTHER
- **Proposed Confidence**: LOW
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 3
- **Reasons Flagged**:
  - Unauthorized financial/payment issue
  - Missing/insufficient context that makes the proposed judgment unreliable

---

### G-1092
**Customer Message**: `@115821 want refund for an order,option of refund is not there, only exchange order is auto registered #complaint two disputed orders on 31/08/17  Order# 403-4366840-6761936 and ORDER # 403-5729570-7854719`

**Context**:
```text
*Empty Context*
```

- **Proposed Intent**: RefundsAndReturns
- **Proposed Confidence**: MEDIUM
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 3
- **Reasons Flagged**:
  - Missing/insufficient context that makes the proposed judgment unreliable

---

### G-1093
**Customer Message**: `@171152 @115821 Worst service, 45 days no solutions to complaint, do not trust them #WorldSmileDay #ZefoWaliDiwaliSale #sasikala`

**Context**:
```text
*Empty Context*
```

- **Proposed Intent**: CustomerServiceEscalation
- **Proposed Confidence**: MEDIUM
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: ESCALATE
- **Proposed Reply Quality**: 3
- **Reasons Flagged**:
  - Missing/insufficient context that makes the proposed judgment unreliable

---

### G-1096
**Customer Message**: `Update: my mom said she saw UPS drive by around sunset and didn’t tell me, I’ll never doubt you again mighty @115821 https://t.co/bZ5iGul9xh`

**Context**:
```text
*Empty Context*
```

- **Proposed Intent**: OTHER
- **Proposed Confidence**: LOW
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 3
- **Reasons Flagged**:
  - Missing/insufficient context that makes the proposed judgment unreliable

---

### G-1098
**Customer Message**: `@115821 @AmazonHelp Thank you you to Asha customer service rep for all her help with my order this morning and fixing it. Proud Prime Member`

**Context**:
```text
*Empty Context*
```

- **Proposed Intent**: CustomerServiceEscalation
- **Proposed Confidence**: MEDIUM
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: ESCALATE
- **Proposed Reply Quality**: 3
- **Reasons Flagged**:
  - Missing/insufficient context that makes the proposed judgment unreliable

---

### G-1101
**Customer Message**: `@455179 still on hold more than 30 minutes after @115830 called me back. Staggering isn’t it? https://t.co/19V5jASHBq`

**Context**:
```text
[455179] Sticking with the tech theme ... https://t.co/5VrHw6Le1J
```

- **Proposed Intent**: CustomerServiceEscalation
- **Proposed Confidence**: MEDIUM
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: ESCALATE
- **Proposed Reply Quality**: 3
- **Reasons Flagged**:
  - Explicit manager/supervisor/human escalation or repeated unresolved support issue

---

### G-1102
**Customer Message**: `@AmazonHelp I HAVE RESPONDED PLEASE HELP ME OUT BY GETTING MY ACCOUNT UNBLOCKED`

**Context**:
```text
[686228] @AmazonHelp you can check my recent purchase history and please unblock my account\n[AmazonHelp] @686228 Apologies for your account being blocked. You might have received an email from our Account Specialist team. Kindly check the same and respond and we'll look into it. ^PB
```

- **Proposed Intent**: OTHER
- **Proposed Confidence**: LOW
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 4
- **Reasons Flagged**:
  - Security/account compromise issue
  - Potentially incorrect AUTO-HANDLE decision

---

### G-1103
**Customer Message**: `@AmazonHelp I can't sign on to my account. When I ask for a password reset no email comes with a code. Help!!`

**Context**:
```text
*Empty Context*
```

- **Proposed Intent**: AccountAndPayment
- **Proposed Confidence**: MEDIUM
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: ESCALATE
- **Proposed Reply Quality**: 3
- **Reasons Flagged**:
  - Security/account compromise issue
  - Missing/insufficient context that makes the proposed judgment unreliable

---

### G-1105
**Customer Message**: `Hi @115850, I ordered a new carpet for Diwali on Oct 11. Gave Rs 660 as express delivery charges with an assurance I will get it by Oct 14`

**Context**:
```text
*Empty Context*
```

- **Proposed Intent**: DeliveryStatus
- **Proposed Confidence**: MEDIUM
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 3
- **Reasons Flagged**:
  - Unauthorized financial/payment issue
  - Missing/insufficient context that makes the proposed judgment unreliable

---

### G-1107
**Customer Message**: `Amazon Music初体験してます、これ良いかも`

**Context**:
```text
*Empty Context*
```

- **Proposed Intent**: OTHER
- **Proposed Confidence**: LOW
- **Proposed Resolution Support**: NO
- **Proposed Auto-Handle**: ESCALATE
- **Proposed Reply Quality**: 3
- **Reasons Flagged**:
  - Potentially incorrect ESCALATE decision
  - Missing/insufficient context that makes the proposed judgment unreliable

---

### G-1108
**Customer Message**: `I’ve bought some things from @115821 over the years. Tried to buy a dishwasher from @116316 2 dishwashers both damaged on arrival. 5euro gesture of goodwill a bit lame 😒`

**Context**:
```text
*Empty Context*
```

- **Proposed Intent**: DamagedOrDefective
- **Proposed Confidence**: MEDIUM
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 3
- **Reasons Flagged**:
  - Legal/safety/injury/threat issue
  - Potentially incorrect AUTO-HANDLE decision
  - Missing/insufficient context that makes the proposed judgment unreliable

---

### G-1109
**Customer Message**: `@115850  I hav an idea that will encourage sellers to sell globally. how about Introducing a new feature in the "amazon pay" so sellers can load funds for the subscriptn fees as many sellers still hesitate for Intl Credit Card due to several reasons this might surely help them`

**Context**:
```text
*Empty Context*
```

- **Proposed Intent**: AccountAndPayment
- **Proposed Confidence**: MEDIUM
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: ESCALATE
- **Proposed Reply Quality**: 3
- **Reasons Flagged**:
  - Unauthorized financial/payment issue
  - Missing/insufficient context that makes the proposed judgment unreliable

---

### G-1111
**Customer Message**: `Yo @115821 @AmazonHelp, why the hell isn't there a drop down option to navigate to Amazon Family. I have to google it every time. Super annoying?`

**Context**:
```text
*Empty Context*
```

- **Proposed Intent**: OTHER
- **Proposed Confidence**: LOW
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 3
- **Reasons Flagged**:
  - Missing/insufficient context that makes the proposed judgment unreliable

---

### G-1113
**Customer Message**: `@AmazonHelp Can you at least confirm that it’s actually locked out and that an account specialist will be reaching out because I’m not getting an account lockout message.`

**Context**:
```text
[221187] @AmazonHelp Hi, I called into customer care just now to correct an incorrect shipping address, and then the rep told me my account was compromised and locked me out. I can’t change my PW, or login and I can’t correct the shipping address. Help???\n[AmazonHelp] @221187 I'm sorry to hear about the trouble you're experiencing with your account, Julian! We want to help here the best we can. Have you received an email from our Account Specialist on how to regain access to your account? Be sure to also check your junk and spam folder. ^HC\n[221187] @AmazonHelp No email. Rep said I should’ve received one and that’s all she can say. I was literally logged into my account providing her with the order # to correct info and then got logged out.\n[AmazonHelp] @221187 Our Account Specialists will reach out to update you via e-mail within two business days of your contact with us. For the fastest resolution, please keep an eye on the e-mail linked to your account, and respond with any requested information or questions. ^JR
```

- **Proposed Intent**: OTHER
- **Proposed Confidence**: LOW
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 4
- **Reasons Flagged**:
  - Security/account compromise issue
  - Potentially incorrect AUTO-HANDLE decision

---

### G-1114
**Customer Message**: `Hey @AmazonHelp!
Second delayed parcel in a row with Prime, and the best you can say is "sorry"?
Should I read it as "next time please order from sellers directly"?`

**Context**:
```text
*Empty Context*
```

- **Proposed Intent**: OTHER
- **Proposed Confidence**: LOW
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 3
- **Reasons Flagged**:
  - Missing/insufficient context that makes the proposed judgment unreliable

---

### G-1119
**Customer Message**: `Pretty sure you guys are going to be getting a lot of these complaints so I'm going to try and get ahead of the pack. Not great customer service @AmazonHelp @1404 @115821 https://t.co/CgKfQTrAnW`

**Context**:
```text
*Empty Context*
```

- **Proposed Intent**: OTHER
- **Proposed Confidence**: MEDIUM
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 3
- **Reasons Flagged**:
  - Missing/insufficient context that makes the proposed judgment unreliable

---

### G-1121
**Customer Message**: `But now they are refusing.Neither returning my product nor returning my money. @120781 @115850 @115821 @4031 @115851 (3) https://t.co/JF8eu3hHsr`

**Context**:
```text
*Empty Context*
```

- **Proposed Intent**: OTHER
- **Proposed Confidence**: LOW
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 3
- **Reasons Flagged**:
  - Unauthorized financial/payment issue
  - Missing/insufficient context that makes the proposed judgment unreliable

---

### G-1122
**Customer Message**: `@AmazonHelp someone hacked my account using a different email.. i cant access that account`

**Context**:
```text
[340464] @AmazonHelp my account email got changed and your customer service cant understand my accent so it was a 10 min covo of her saying "what"\n[AmazonHelp] @340464 I'm sorry to hear this! Please use the link to contact in so we can look into this with you: https://t.co/U6GqMB4j9d ^GL
```

- **Proposed Intent**: AccountAndPayment
- **Proposed Confidence**: MEDIUM
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: ESCALATE
- **Proposed Reply Quality**: 4
- **Reasons Flagged**:
  - Security/account compromise issue

---

### G-1123
**Customer Message**: `@AmazonHelp Intelcom. I never heard of them before and read bad reviews on them that are coming true in my situation. When I ordered before, I never had this issue with UPS or Canada Post.`

**Context**:
```text
[816926] PSA: don't waste your money on @116090 Prime as the 2 day free shipping is a joke. It has been 4 days since placing the order and guaranteed delivery date was Mon Nov 27. Still no package and last delivery update was Mon Nov 27 at 1:23pm saying the item is "out for delivery"\n[AmazonHelp] @816926 Oh no! I'm sorry about the delay of your package. We'd like to assist you with this. Who was the carrier for this package? ^GP
```

- **Proposed Intent**: OTHER
- **Proposed Confidence**: LOW
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 4
- **Reasons Flagged**:
  - Legal/safety/injury/threat issue
  - Potentially incorrect AUTO-HANDLE decision

---

### G-1127
**Customer Message**: `@115850 pls add DTH recharge also in Amazon Pay !!`

**Context**:
```text
*Empty Context*
```

- **Proposed Intent**: OTHER
- **Proposed Confidence**: LOW
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 3
- **Reasons Flagged**:
  - Unauthorized financial/payment issue
  - Missing/insufficient context that makes the proposed judgment unreliable

---

### G-1128
**Customer Message**: `@AmazonHelp @517197 And where is the first of two tweets (1/2) ????`

**Context**:
```text
[517197] @115850 . Following order 171-6263504-0846758 was placed yesterday on prime, needed it urgent. Hvnt rcvd d prdct and it is mrkd delivered.\n[AmazonHelp] @517197 Please don't provide your order details, we consider it personal information. Our Twitter page is visible to public. (2/2) ^AS
```

- **Proposed Intent**: DeliveryStatus
- **Proposed Confidence**: MEDIUM
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 4
- **Reasons Flagged**:
  - Potentially incorrect intent based on the customer message/context

---

### G-1130
**Customer Message**: `@UPSHelp @250696 They aren't sorry and don't give personal info to ups workers most employees are ex cons that will probably try to steal your identity like they are holding my package hostage. 3 days to deliver a package 8-9 miles, about a 10 min drive. Offered to go get It my self`

**Context**:
```text
[250696] Thanks @AmazonHelp for sending me a box full of garbage that @UPSHelp thinks they picked up for return but is still sitting at my door.\n[UPSHelp] @250696 I am terribly sorry for the inconvenience. Please DM us at the link provided with a tracking number, the delivery address, and a phone number and we'll ensure that it is picked up as soon as possible. ^JF https://t.co/wKJHDXWGRQ
```

- **Proposed Intent**: DeliveryStatus
- **Proposed Confidence**: MEDIUM
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 3
- **Reasons Flagged**:
  - Explicit manager/supervisor/human escalation or repeated unresolved support issue
  - Potentially incorrect AUTO-HANDLE decision

---

### G-1132
**Customer Message**: `Amazon keeps fucking cancelling my order. Doesn’t even tell me why`

**Context**:
```text
*Empty Context*
```

- **Proposed Intent**: OTHER
- **Proposed Confidence**: LOW
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 3
- **Reasons Flagged**:
  - Missing/insufficient context that makes the proposed judgment unreliable

---

### G-1133
**Customer Message**: `@AmazonHelp Sur colis Privé : Votre colis a été expédié par votre webmarchand, mais n a pas encore été pris en charge par Colis Privé`

**Context**:
```text
[672198] @2600 encore un colis "prime" qui ne va pas arriver, grâce à colis Privé ... on en parle ou pas ? Colis partis le 09/11\n[AmazonHelp] @672198 Bonjour, je suis désolé d'apprendre cela. Que dit le suivi de votre colis s'il vous plaît ? ^AR
```

- **Proposed Intent**: AccountAndPayment
- **Proposed Confidence**: MEDIUM
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: ESCALATE
- **Proposed Reply Quality**: 4
- **Reasons Flagged**:
  - Unauthorized financial/payment issue

---

### G-1135
**Customer Message**: `@AmazonHelp Already contacted,they are saying it's technical glitch,need to wait for few hours,in the starting only you are failing to deliver recharge services @116329`

**Context**:
```text
[348604] @115850 @117128 Not able to recharge my phone number with Rs.448 recharge,everytime I am recharging using Amazon it is giving that recharge failed,have tried it 5 or 6 times but transaction failing again and again,sort this out.\n[AmazonHelp] @348604 That's unusual. We'd like to check this for you. Kindly contact us here: https://t.co/vlvfJr4nN9 ^SY
```

- **Proposed Intent**: OTHER
- **Proposed Confidence**: LOW
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 4
- **Reasons Flagged**:
  - Unauthorized financial/payment issue

---

### G-1136
**Customer Message**: `Amazon customer care service from excellent to pathetic. Not able to handle pressure? @115850`

**Context**:
```text
*Empty Context*
```

- **Proposed Intent**: OTHER
- **Proposed Confidence**: LOW
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 3
- **Reasons Flagged**:
  - Missing/insufficient context that makes the proposed judgment unreliable

---

### G-1138
**Customer Message**: `Why are all of the kindle oasis 9th edition 2017 covers no longer available @115830 @AmazonHelp`

**Context**:
```text
*Empty Context*
```

- **Proposed Intent**: DigitalServices
- **Proposed Confidence**: MEDIUM
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 3
- **Reasons Flagged**:
  - Missing/insufficient context that makes the proposed judgment unreliable

---

### G-1139
**Customer Message**: `@117795 have ruined the start of my week!`

**Context**:
```text
*Empty Context*
```

- **Proposed Intent**: DamagedOrDefective
- **Proposed Confidence**: MEDIUM
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 3
- **Reasons Flagged**:
  - Missing/insufficient context that makes the proposed judgment unreliable

---

### G-1142
**Customer Message**: `Hey @115821, shouldn't two day shipping come in two days instead of four?`

**Context**:
```text
*Empty Context*
```

- **Proposed Intent**: OTHER
- **Proposed Confidence**: LOW
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 3
- **Reasons Flagged**:
  - Missing/insufficient context that makes the proposed judgment unreliable

---

### G-1143
**Customer Message**: `@115821 I applied £40 of vouchers to my account yesterday on my phone and they are not showing up! Please help. @33224 paid for them.`

**Context**:
```text
*Empty Context*
```

- **Proposed Intent**: OTHER
- **Proposed Confidence**: LOW
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 3
- **Reasons Flagged**:
  - Unauthorized financial/payment issue
  - Missing/insufficient context that makes the proposed judgment unreliable

---

### G-1148
**Customer Message**: `Has anyone had a package returned to @115821 because @118706 refused to deliver it? 😐`

**Context**:
```text
*Empty Context*
```

- **Proposed Intent**: DeliveryStatus
- **Proposed Confidence**: MEDIUM
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 3
- **Reasons Flagged**:
  - Missing/insufficient context that makes the proposed judgment unreliable

---

### G-1149
**Customer Message**: `@AmazonHelp What's the latest time a Prime delivery will come during the day in the UK? Waiting on order 026-7088681-3921926`

**Context**:
```text
*Empty Context*
```

- **Proposed Intent**: DeliveryStatus
- **Proposed Confidence**: MEDIUM
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 3
- **Reasons Flagged**:
  - Missing/insufficient context that makes the proposed judgment unreliable

---

### G-1151
**Customer Message**: `@AmazonHelp You have a bug here that sends you to other places when you select a category, instead of letting you see that category you selected. Example Coffe machines when I go to TVs https://t.co/ISwJZgZrQ3`

**Context**:
```text
*Empty Context*
```

- **Proposed Intent**: OTHER
- **Proposed Confidence**: LOW
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 3
- **Reasons Flagged**:
  - Missing/insufficient context that makes the proposed judgment unreliable

---

### G-1152
**Customer Message**: `Wow @115821 just closed my prime membership!! Can’t get account reinstated and lost all media content! #awfulCustomerService #Annoyed #googlehereicome`

**Context**:
```text
*Empty Context*
```

- **Proposed Intent**: OTHER
- **Proposed Confidence**: LOW
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 3
- **Reasons Flagged**:
  - Missing/insufficient context that makes the proposed judgment unreliable

---

### G-1155
**Customer Message**: `Shout out to @115830 for ruining Christmas, delivering my dad's Christmas present with NO packaging at all and he answered the door🤦🏼‍♀️🤦🏼‍♀️now I'm being told to lie to say I answered the door to my mum and she defos doesn't believe me. I hope you're happy, Amazon.`

**Context**:
```text
*Empty Context*
```

- **Proposed Intent**: OTHER
- **Proposed Confidence**: LOW
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 3
- **Reasons Flagged**:
  - Missing/insufficient context that makes the proposed judgment unreliable

---

### G-1156
**Customer Message**: `@115817 @UPSHelp 
Your driver tried to deliver my @115821 package ONCE. Now I’m expected to drive and pick it up from some other place? 
Fuck that. I paid for #AmazonPrime and shipping. Deliver it to MY place.
🖕🏻🤯🤬😡😠🖕🏻 https://t.co/F0HwrEiAEM`

**Context**:
```text
*Empty Context*
```

- **Proposed Intent**: DeliveryStatus
- **Proposed Confidence**: MEDIUM
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 3
- **Reasons Flagged**:
  - Unauthorized financial/payment issue
  - Missing/insufficient context that makes the proposed judgment unreliable

---

### G-1157
**Customer Message**: `@AmazonHelp what the hell is this??? I was in and the guy didn’t even knock😤 and my parcel has been water damaged😠 https://t.co/3qMkj1wxKl`

**Context**:
```text
*Empty Context*
```

- **Proposed Intent**: DamagedOrDefective
- **Proposed Confidence**: MEDIUM
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 3
- **Reasons Flagged**:
  - Legal/safety/injury/threat issue
  - Potentially incorrect AUTO-HANDLE decision
  - Missing/insufficient context that makes the proposed judgment unreliable

---

### G-1161
**Customer Message**: `@115850 
I have played #AmazonRechargesQuiz ,it is 1st Dec today, where should i see the winners list`

**Context**:
```text
*Empty Context*
```

- **Proposed Intent**: OTHER
- **Proposed Confidence**: LOW
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 3
- **Reasons Flagged**:
  - Unauthorized financial/payment issue
  - Missing/insufficient context that makes the proposed judgment unreliable

---

### G-1162
**Customer Message**: `@115821 where the hell is my order? It was supposed to be here about 1 week ago , and i still havent recieved it. #upset .`

**Context**:
```text
*Empty Context*
```

- **Proposed Intent**: OTHER
- **Proposed Confidence**: LOW
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 3
- **Reasons Flagged**:
  - Missing/insufficient context that makes the proposed judgment unreliable

---

### G-1164
**Customer Message**: `.@AmazonHelp not happy 😡 Paying for prime too. https://t.co/Zt5OrqLXkB`

**Context**:
```text
*Empty Context*
```

- **Proposed Intent**: OTHER
- **Proposed Confidence**: LOW
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 3
- **Reasons Flagged**:
  - Missing/insufficient context that makes the proposed judgment unreliable

---

### G-1165
**Customer Message**: `@AmazonHelp Hi, I want to try a sample “Das Reboot” on kindle but the sample only goes as far as the table of contents, can you help?`

**Context**:
```text
*Empty Context*
```

- **Proposed Intent**: DigitalServices
- **Proposed Confidence**: MEDIUM
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 3
- **Reasons Flagged**:
  - Missing/insufficient context that makes the proposed judgment unreliable

---

### G-1166
**Customer Message**: `@115821 you all got me fucked up, you’re telling me you can ship me a package that I didn’t even want with free shipping but you’re going to take half my refund for shipping back 🖕🏼🖕🏼🖕🏼🖕🏼🖕🏼`

**Context**:
```text
*Empty Context*
```

- **Proposed Intent**: DeliveryStatus
- **Proposed Confidence**: MEDIUM
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 3
- **Reasons Flagged**:
  - Missing/insufficient context that makes the proposed judgment unreliable

---

### G-1167
**Customer Message**: `@AmazonHelp Hi, is this completely out of stock now? I was going to order it to come tomorrow, but it now says its unavailable on the app. https://t.co/mfDaoZpdnO`

**Context**:
```text
*Empty Context*
```

- **Proposed Intent**: DigitalServices
- **Proposed Confidence**: MEDIUM
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 3
- **Reasons Flagged**:
  - Missing/insufficient context that makes the proposed judgment unreliable

---

### G-1169
**Customer Message**: `@115850 Wow!! I am happy with Amazon India because reason is I got delivery in less than 17 hours.`

**Context**:
```text
*Empty Context*
```

- **Proposed Intent**: DeliveryStatus
- **Proposed Confidence**: MEDIUM
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 3
- **Reasons Flagged**:
  - Missing/insufficient context that makes the proposed judgment unreliable

---

### G-1170
**Customer Message**: `@115850 I can't find Applewatch Series 3 on your portal. Isn't it available? When is it going to be available?`

**Context**:
```text
*Empty Context*
```

- **Proposed Intent**: OTHER
- **Proposed Confidence**: LOW
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 3
- **Reasons Flagged**:
  - Missing/insufficient context that makes the proposed judgment unreliable

---

### G-1172
**Customer Message**: `@410950 @383281 @115850 Request @115850 not to engage with third persons. If her friend has a problem, he/she will handle. Why this idiot is interfering in that. Like to thank Amazon for asking for aadhar card. Because these ppl may be fraudsters.`

**Context**:
```text
[410950] .@115850 my friend ordered a product, it says "delivered, handed over to the customer", but it wasn't delivered to him. Now your customer care is saying it's mandatory for him to have an Aadhaar card to get this matter investigated? Under what ruling is it mandatory?!
```

- **Proposed Intent**: OTHER
- **Proposed Confidence**: LOW
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: ESCALATE
- **Proposed Reply Quality**: 3
- **Reasons Flagged**:
  - Potentially incorrect ESCALATE decision

---

### G-1174
**Customer Message**: `@115850 yet to receive the package..... really upset wit your amazon agent. 
@AmazonHelp @115821 https://t.co/f41n9Pxk5J`

**Context**:
```text
*Empty Context*
```

- **Proposed Intent**: DeliveryStatus
- **Proposed Confidence**: MEDIUM
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 3
- **Reasons Flagged**:
  - Explicit manager/supervisor/human escalation or repeated unresolved support issue
  - Potentially incorrect AUTO-HANDLE decision
  - Missing/insufficient context that makes the proposed judgment unreliable

---

### G-1175
**Customer Message**: `@115830 trying to leave a review for a seller who sent me these instead of a pair of tights but told I can’t as it contains adult content? https://t.co/Cj4LM8UmJU`

**Context**:
```text
*Empty Context*
```

- **Proposed Intent**: OTHER
- **Proposed Confidence**: LOW
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 3
- **Reasons Flagged**:
  - Missing/insufficient context that makes the proposed judgment unreliable

---

### G-1176
**Customer Message**: `@115830 great care &amp; consideration taken with my parcel I see, can only hope the contents are not ruined! #Shocking #ParcelLeftInPuddle https://t.co/0EFCyQsEWF`

**Context**:
```text
*Empty Context*
```

- **Proposed Intent**: DamagedOrDefective
- **Proposed Confidence**: MEDIUM
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 3
- **Reasons Flagged**:
  - Missing/insufficient context that makes the proposed judgment unreliable

---

### G-1179
**Customer Message**: `I have well over 1000 @115821 orders — for the first time they sent me the wrong item. @23564 motion sensor instead of the multipurpose sensor`

**Context**:
```text
*Empty Context*
```

- **Proposed Intent**: WrongItem
- **Proposed Confidence**: MEDIUM
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 3
- **Reasons Flagged**:
  - Missing/insufficient context that makes the proposed judgment unreliable

---

### G-1181
**Customer Message**: `@115830 cardboard packaging doesn't work when the delivery vehicle doesn't keep the rain out. My parcel was wrapped in wet brown mush!`

**Context**:
```text
*Empty Context*
```

- **Proposed Intent**: DeliveryStatus
- **Proposed Confidence**: MEDIUM
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 3
- **Reasons Flagged**:
  - Missing/insufficient context that makes the proposed judgment unreliable

---

### G-1182
**Customer Message**: `@115830 I just had 18 password assistance code emails in 10 minutes would this be someone trying to access my account?`

**Context**:
```text
*Empty Context*
```

- **Proposed Intent**: AccountAndPayment
- **Proposed Confidence**: MEDIUM
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: ESCALATE
- **Proposed Reply Quality**: 3
- **Reasons Flagged**:
  - Security/account compromise issue
  - Missing/insufficient context that makes the proposed judgment unreliable

---

### G-1184
**Customer Message**: `@115850 hey need u r help.
Iam unable to login to my account.
Forgot password is asking Gmail I'd which I don't know.i know mobile no.`

**Context**:
```text
*Empty Context*
```

- **Proposed Intent**: AccountAndPayment
- **Proposed Confidence**: MEDIUM
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: ESCALATE
- **Proposed Reply Quality**: 3
- **Reasons Flagged**:
  - Security/account compromise issue
  - Missing/insufficient context that makes the proposed judgment unreliable

---

### G-1189
**Customer Message**: `@115850 while ordering ,got the msg of delivery on 17th Nov ,later got the date of 21 Nov inspite of expedited delivery option...... kindly expedite, urgent package.
Order No : 406-6299669-6690762`

**Context**:
```text
*Empty Context*
```

- **Proposed Intent**: DeliveryStatus
- **Proposed Confidence**: HIGH
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 3
- **Reasons Flagged**:
  - Missing/insufficient context that makes the proposed judgment unreliable

---

### G-1190
**Customer Message**: `@AmazonHelp Hi!  I am about to place an order that includes 3 books.  The "BUT3GET30" coupon code for 30% off books is not working.  Can you help?`

**Context**:
```text
*Empty Context*
```

- **Proposed Intent**: OTHER
- **Proposed Confidence**: MEDIUM
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 3
- **Reasons Flagged**:
  - Missing/insufficient context that makes the proposed judgment unreliable

---

### G-1191
**Customer Message**: `@AmazonHelp I could, but because the items were shipped in 8 boxes instead of 1, I’d have to leave the same feedback 8 times, which is a pretty big waste of time/energy for me. Your system makes this harder than it has to be.`

**Context**:
```text
[258924] My @115821 Prime monthly delivery arrived this month in 8 separate comically oversized boxes, instead of the usual 1 box with all items in it. Is that sort of waste the new normal?\n[AmazonHelp] @258924 Thanks for highlighting this to us, Amy, minimizing waste is part of our mission as a company. You can leave this feedback directly with us via the following link: https://t.co/TH7UAFZey5.^SM
```

- **Proposed Intent**: DeliveryStatus
- **Proposed Confidence**: MEDIUM
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 4
- **Reasons Flagged**:
  - Unauthorized financial/payment issue
  - Potentially incorrect intent based on the customer message/context

---

### G-1194
**Customer Message**: `Worst call experience @AmazonHelp .. 22mins later and no information —my order won’t be delivered 😞`

**Context**:
```text
*Empty Context*
```

- **Proposed Intent**: OTHER
- **Proposed Confidence**: LOW
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 3
- **Reasons Flagged**:
  - Missing/insufficient context that makes the proposed judgment unreliable

---

### G-1197
**Customer Message**: `@AmazonHelp is there anyone sensible that I could speak with to sort out a refund? You deliberately did not have a free number to call u on`

**Context**:
```text
*Empty Context*
```

- **Proposed Intent**: RefundsAndReturns
- **Proposed Confidence**: MEDIUM
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 3
- **Reasons Flagged**:
  - Missing/insufficient context that makes the proposed judgment unreliable

---

### G-1198
**Customer Message**: `@115850 Amazon order #405-7259538-2338702 Why blue Dart has sent my item to Sitamarhi City instead of Gopalganj City.Are they out of mind.`

**Context**:
```text
*Empty Context*
```

- **Proposed Intent**: OTHER
- **Proposed Confidence**: LOW
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 3
- **Reasons Flagged**:
  - Missing/insufficient context that makes the proposed judgment unreliable

---

### G-1199
**Customer Message**: `@10827 @115850 @118702 @115821 Returned a product purchased from Amazon 30 Days ago and Still waiting for refund to get initiated.`

**Context**:
```text
*Empty Context*
```

- **Proposed Intent**: RefundsAndReturns
- **Proposed Confidence**: MEDIUM
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 3
- **Reasons Flagged**:
  - Missing/insufficient context that makes the proposed judgment unreliable

---


## Priority 2 — REVIEW IF TIME

### G-1000
**Customer Message**: `@AmazonHelp Please don't play around. I have been promised by Amazon many times for refund but fact is it is not honoring.`

**Context**:
```text
[183033] No refund of my money since one month, name mismatch in cheque and bank a/c @AmazonHelp   order no #403-8295304-4660353\n[183033] @AmazonHelp Still awaiting my refund @AmazonHelp\n[AmazonHelp] @183033 I see that we've sent you a correspondence. Kindly check the same here: https://t.co/ubzNHWZvL2 ^SG\n[183033] @AmazonHelp It has been 58 days now. No refund till now.\n[AmazonHelp] @183033 Please respond to our reply sent to you from our escalations team. We will get back to you with the resolution. ^GU\n[183033] @AmazonHelp I have done it all. Please check with your end.\n[AmazonHelp] @183033 However, since you've responded to the email sent by the Soial Media team you'd be receiving an update soon. 2/2 ^EM\n[183033] @AmazonHelp What is the update? Please tell me, does it take 55 days for processing the refund?\n[AmazonHelp] @183033 I'm sorry for the stretch. Please refer to our correspondence here: https://t.co/8DAc10S7ww ^AP\n[183033] @AmazonHelp Very poor service from Amazon. Still awaiting for my refund.. More than 60days now...\n[AmazonHelp] @183033 I'm sorry it is longer than expected. We're working on it and will get back to you soon. ^VH\n[183033] @AmazonHelp What is the update of my refund?still I have not got my money back. Even after so many promises have been made to me for same.\n[AmazonHelp] @183033 An email has already been sent with a reply. Kindly check it from the link shared here: https://t.co/NTkrxpsbHJ ^HR
```

- **Proposed Intent**: RefundsAndReturns
- **Proposed Confidence**: MEDIUM
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 4
- **Reasons Flagged**:
  - MEDIUM confidence

---

### G-1001
**Customer Message**: `@AmazonHelp Thanks for the prompt response.  Here's your link-&gt;
WD My Passport 1TB Portable External Hard Drive (Blue) https://t.co/AU9qOeLQiP`

**Context**:
```text
[196041] Hey @115850 I'm a big fan of your "lightning section". 

No offense ...but not this :( https://t.co/ybm7usONAR\n[AmazonHelp] @196041 Thanks for flagging this. Could you please help us with the link to the product so that we can check this for you? ^VN\n[196041] @AmazonHelp Whoa! I can c that d lightning deal ended sooner wd only 3% claim in past 1hr. Thr's no waitlist too.  Smthing's not right. Here's the deal: https://t.co/I9GgNidL8o\n[AmazonHelp] @196041 That's odd. We'd like to check this. Could you please help us with the product page link? ^HD
```

- **Proposed Intent**: OTHER
- **Proposed Confidence**: MEDIUM
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 4
- **Reasons Flagged**:
  - MEDIUM confidence
  - OTHER where the message appears to contain an actual support issue

---

### G-1003
**Customer Message**: `@AmazonHelp The last two packages were supposed to be delivered by AMZL US.`

**Context**:
```text
[223979] @AmazonHelp What's with the late deliveries lately?\n[AmazonHelp] @223979 I'm sorry your orders are taking longer than expected to arrive! We always strive to meet the delivery date shown at checkout and confirmed via e-mail. Do you have a recent order shown here that we missed the delivery date: https://t.co/Y5jpI9gRhE? ^BN\n[223979] @AmazonHelp I had an order that was supposed to be delivered tonight and one earlier in the week that was not only late, but delivered to the wrong address.\n[AmazonHelp] @223979 Oh my! I'm so sorry for this poor experience! Have you noticed a trend with the carrier for each package or were they different each time? You can find that here: https://t.co/Y5jpI9gRhE ^HS
```

- **Proposed Intent**: OTHER
- **Proposed Confidence**: LOW
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 4
- **Reasons Flagged**:
  - LOW confidence
  - OTHER where the message appears to contain an actual support issue

---

### G-1006
**Customer Message**: `@AmazonHelp See...you all lie now.  Plain and simple.  I've been a Prime Member for 7 years and up until this year 2 days meant 2 days.  You don't get to show a delivery date 2 days from date of order and than change after order.`

**Context**:
```text
[245184] Anyone else that's a Prime member feel like they are getting screwed by .@115821 on the 2 day shipping? Seems to me that @115821 has changed 2 day shipping into 4-5 day shipping.\n[AmazonHelp] @245184 I'm so sorry for the disappointment! Selecting Two-Day shipping will reduce the transit time to two business days after we've shipped your order, but it won't impact how long it takes us to obtain the item or prepare it for shipment: https://t.co/wNIe9aPWSf. ^SD
```

- **Proposed Intent**: DeliveryStatus
- **Proposed Confidence**: MEDIUM
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 4
- **Reasons Flagged**:
  - MEDIUM confidence

---

### G-1009
**Customer Message**: `@AmazonHelp I have already reported. Read previous tweet.`

**Context**:
```text
[416958] @115850 does your 11 oct falls on 11 nov? Called your customer care. Haven’t received order yet. Shame https://t.co/O7tIYg0i3M\n[416958] @115850 Still not received. Should i go to court? https://t.co/lsqqPa1r5c\n[AmazonHelp] @416958 Sorry for the hassle. Please report this to our support team here: https://t.co/vlvfJr4nN9 and we'll check this. ^HN
```

- **Proposed Intent**: OTHER
- **Proposed Confidence**: LOW
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 4
- **Reasons Flagged**:
  - LOW confidence
  - OTHER where the message appears to contain an actual support issue

---

### G-1010
**Customer Message**: `@AmazonHelp how kind!! she is the happiest little kitty and is easily pleased! 😁`

**Context**:
```text
[815673] #specialdelivery @173744 @113376 #CatsofTwitter #catsofinstagram https://t.co/JzTjmX7W2k\n[AmazonHelp] @815673 So furrtastic! We'd like to send our own special delivery meow. What kind of toys does your fluffer like? 😉 ^AL
```

- **Proposed Intent**: OTHER
- **Proposed Confidence**: LOW
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 4
- **Reasons Flagged**:
  - LOW confidence
  - OTHER where the message appears to contain an actual support issue

---

### G-1015
**Customer Message**: `@AmazonHelp Ups`

**Context**:
```text
[221306] @115821 i had guaranteed delivery this past Tuesday still hasn’t arrived and keeps being pushed back\n[AmazonHelp] @221306 I'm sorry to hear that you have not received you order! Who is the carrier? You can find that information here: https://t.co/Y5jpI9gRhE ^SW
```

- **Proposed Intent**: DeliveryStatus
- **Proposed Confidence**: MEDIUM
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 4
- **Reasons Flagged**:
  - MEDIUM confidence

---

### G-1016
**Customer Message**: `@AmazonHelp That link led me to Amazon UK but I will find the appropriate page for my country. Thank you.`

**Context**:
```text
[400233] @AmazonHelp What can be done if I received a damaged box inside the Amazon packaging? This is the fourth time it has happened.\n[AmazonHelp] @400233 Sorry to hear your order was damaged. Is the outer packaging also damaged? Was the item fulfilled by Amazon or? ^NV\n[400233] @AmazonHelp The outer packaging was good. There weren't any dents on the box and the tape was secure. The item came from Look out Toys.\n[AmazonHelp] @400233 If the order was fulfilled by the 3rd Party Seller, have you tried contacting them: https://t.co/T7J2pBdzfa? ^JJ\n[400233] @AmazonHelp No, but I will surely do that now. What if they don't respond?\n[AmazonHelp] @400233 Sellers have up to 3 business days. In the unlikely event you don't get a response, go here: https://t.co/VPhfhQmOgJ. ^MC
```

- **Proposed Intent**: OTHER
- **Proposed Confidence**: MEDIUM
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 4
- **Reasons Flagged**:
  - MEDIUM confidence
  - OTHER where the message appears to contain an actual support issue

---

### G-1018
**Customer Message**: `@AmazonHelp Then let you know what it says yes? 

We have had 2 emails with delivery dates and then another today say it would be delivered today`

**Context**:
```text
[422142] @AmazonHelp hi I would like to find out where my package is as it said it would deliver today?
```

- **Proposed Intent**: DeliveryStatus
- **Proposed Confidence**: MEDIUM
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 3
- **Reasons Flagged**:
  - MEDIUM confidence

---

### G-1019
**Customer Message**: `@AmazonHelp Whats the status??`

**Context**:
```text
[AmazonHelp] @463473 In that case, please share your details here: https://t.co/beaaDm0muc &amp; we'll have a closer look into it. ^RS\n[463473] @AmazonHelp You can contact me on 7065138342\n[AmazonHelp] @463473 Please don't provide your details, we consider it to be personal information. Our page's visible to the public. (2/2)^GU
```

- **Proposed Intent**: OTHER
- **Proposed Confidence**: LOW
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 4
- **Reasons Flagged**:
  - LOW confidence
  - OTHER where the message appears to contain an actual support issue

---

### G-1020
**Customer Message**: `@AmazonHelp Link is not working as it is showing
We're sorry. The Web address you entered is not a functioning page on our site.`

**Context**:
```text
[317328] @115850 @171328 Please help me for this..... Very poor service as pick up date was 3rd oct 17 now 10 days passed no pick up by came. wht shld i do??? https://t.co/Ru2UxES5aQ\n[AmazonHelp] @317328 here: https://t.co/00q4Sqj9zL for assistance? (2/2) ^KA
```

- **Proposed Intent**: OTHER
- **Proposed Confidence**: LOW
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 4
- **Reasons Flagged**:
  - LOW confidence
  - OTHER where the message appears to contain an actual support issue

---

### G-1021
**Customer Message**: `@AmazonHelp Great response by Amazon.... compensation of 500 INR...no legal action against seller &amp; brand #JeffBezos https://t.co/JmwhiGX814`

**Context**:
```text
[119704] @115850 : what type of product are you selling, we could have died.product was in use and then a blast
Order no - 407-2808023-6902735 https://t.co/a8t07gJDuh\n[AmazonHelp] @119704 Please don't provide your order details as we consider it personal information. Our twitter page is visible to public. ^SQ\n[119703] @AmazonHelp @119704  https://t.co/rUjHdeMm9G\n[AmazonHelp] @119703 However, you need to adhere to guidelines here: https://t.co/jimvgYJFRD to post review. (2/2) ^SV\n[119703] @AmazonHelp Do u think it's just normal happening???this is real happened with me...do you still think it's not worth to show quality of product\n[AmazonHelp] @119703 Be assured, we've shared your comments with internal teams for review and to improve our services. (2/2) ^SV\n[119703] @AmazonHelp You are not understanding my situation n anger...it ruined my festival as my wife is still shocked as she was cooking...\n[119703] @AmazonHelp Because of Amazon I purchased a product which blasted on day one...n u people asking me to keep cool...where is Surya flames #suryaflam1\n[AmazonHelp] @119703 Apologies for the situation, Anurag. Please share your details here: https://t.co/GIJyeYqKE0 I'll reach &amp; assist. ^SV\n[119703] @AmazonHelp Order id-407-2808023-6902735
Mails already done\n[AmazonHelp] @119703 Please don't provide your order details, we consider it to be personal information. Our page is visible to the public.^SF\n[119703] @AmazonHelp U people not even understanding the situation...there was fire on stove n if cylinder got fired what worst could happened...\n[AmazonHelp] @119703 I'm sure our team would reach out to you soon. (2/2) ^VM\n[119703] @AmazonHelp Stop asking non sense. it's been mid of the day providing hell of details but no response yet. Not even Surya Flames responded #JeffBezos\n[AmazonHelp] @119703 email correspondence from our team. Kindly check the same and revert. 2/2 ^MM\n[119703] @AmazonHelp One word for Amazon... Pathetic...\n[AmazonHelp] @119703 Please share your details in the above link Anurag and we'll check this for you. ^HN\n[119703] @AmazonHelp Already shared...\n[AmazonHelp] @119703 As you've shared your details, we'll work on it and get back to you at the earliest. ^HN
```

- **Proposed Intent**: OTHER
- **Proposed Confidence**: MEDIUM
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 4
- **Reasons Flagged**:
  - MEDIUM confidence
  - OTHER where the message appears to contain an actual support issue

---

### G-1023
**Customer Message**: `@AmazonHelp If seller is @ mistake y should i get the refund left shoe is of 6 sz n rgt shoe is of 7, which is vendor mistake n he has correct it.`

**Context**:
```text
[181629] @115850 purchased puma shoes bt gt defective prdct but now ur team gving me refund instead of rplcmnt https://t.co/FHFd2HWPfU\n[181629] @115850 Without prpr investigation n solution simply asking me to get the refuns were as vendor is @ fault,y not asking vendor for his mistake\n[AmazonHelp] @181629 I’m extremely sorry about this experience, Rajkumar.  If the item is now out of stock with the original seller or if the same size is not available, we aren't able to create replacement. So we will process a refund after the item is returned to Amazon. ^MK
```

- **Proposed Intent**: RefundsAndReturns
- **Proposed Confidence**: MEDIUM
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 4
- **Reasons Flagged**:
  - MEDIUM confidence

---

### G-1025
**Customer Message**: `@AmazonHelp My order was finally delivered, and I very much appreciate the help I received from Luis A. and Brian (or Bryan?). Thank you, both!`

**Context**:
```text
[293375] @115821 and @AmazonHelp - Where is my package??? Your Amazon Logistics driver is lying. S/he is violating mail delivery statutes. #Amazon\n[AmazonHelp] @293375 I'm sorry to hear you haven't received the package. Please try these steps, and keep us posted: https://t.co/Qu21lrUAho ^BH\n[293375] @AmazonHelp I have already attempted all of those steps. Your #AmazonFlex drivers are lying about delivery attempts &amp; tampering with mail delivery.\n[AmazonHelp] @293375 We'd like to investigate this with you. When you have a moment, please fill in your info here: https://t.co/OqMIQB9DMn ^TG
```

- **Proposed Intent**: OTHER
- **Proposed Confidence**: MEDIUM
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 4
- **Reasons Flagged**:
  - MEDIUM confidence
  - OTHER where the message appears to contain an actual support issue

---

### G-1029
**Customer Message**: `@AmazonHelp Your callback service is not working. This is not what I expected from you -.- There's no other way to verbally have a conversation on this`

**Context**:
```text
[124856] @115850 The package that was supposed to be delivered on the 14th but never showed up, so we cancelled the order, suddenly turned up today\n[AmazonHelp] @124856 That's odd. We'd like to look into it. Kindly share your details here:  https://t.co/2t6DQoUmNZ we'll get 1/2 ^AP
```

- **Proposed Intent**: OTHER
- **Proposed Confidence**: LOW
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 4
- **Reasons Flagged**:
  - LOW confidence
  - OTHER where the message appears to contain an actual support issue

---

### G-1030
**Customer Message**: `@AmazonHelp Like I need a reason- self confessed bookworm over here 😂🙌🏼 I mainly got it for the backlight as I read at night but don’t want to wake my partner up by putting the light on 📚`

**Context**:
```text
[148588] So I may have just gone a bit nuts with @115830 Black Friday deals and bought a new Kindle Paperwhite + protective case and a Fire TV Stick🙊 bye bye student loan!! 😂\n[AmazonHelp] @148588 You do you! 🙉😁 ^DA\n[148588] @AmazonHelp I’m trying to use the excuse that I needed a new kindle anyway 🙈💛\n[AmazonHelp] @148588 We'll back up that statement! Our Paperwhite device gives you plenty of reasons to get lost in a good book. ^MJ
```

- **Proposed Intent**: OTHER
- **Proposed Confidence**: LOW
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 4
- **Reasons Flagged**:
  - LOW confidence
  - OTHER where the message appears to contain an actual support issue

---

### G-1031
**Customer Message**: `@AmazonHelp Non le SAV qui devait me recontacter ne l'a pas fait.`

**Context**:
```text
[136727] Ok... Le SAV d'@120533 contacté par Chat qui arrête de répondre en pleine conversation... Décidément pas de bol avec eux en ce moment.😔\n[AmazonHelp] @136727 Merci de nous tenir informé de la situation, nous restons à votre disposition en cas de besoin.\n[136727] @AmazonHelp Pas de problème. J'attends des nouvelles de votre collègue et de Colis Privé qui doit se renseigner (ça commence à être long avec eux).\n[136727] @AmazonHelp Donc j'ai eu une réponse de Colis Privé, et comme je m'en doutais ils ne livrent plus dans ma ville. Erreur Amazon selon eux.\n[AmazonHelp] @136727 Je suis désolée d'apprendre cela. Avez-vous reçu une réponse de la part de notre SAV ? ^SB
```

- **Proposed Intent**: OTHER
- **Proposed Confidence**: LOW
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 4
- **Reasons Flagged**:
  - LOW confidence
  - OTHER where the message appears to contain an actual support issue

---

### G-1033
**Customer Message**: `@AmazonHelp Sì, la data di consegna era ieri. Ed oggi ancora nulla! Sul sito il tracking è rimasto a lunedì 16:20, poi nessun aggiornamento.`

**Context**:
```text
[404401] Cara @120540 se affidi i tuoi pacchi #prime a @300933 rischi grosso! Faccio prima ad andare in libreria!\n[AmazonHelp] @404401 Ciao Marco, hai riscontrato un ritardo nella consegna del tuo ordine? Qual è la data di consegna prevista? ^MZ
```

- **Proposed Intent**: DeliveryStatus
- **Proposed Confidence**: MEDIUM
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 4
- **Reasons Flagged**:
  - MEDIUM confidence

---

### G-1038
**Customer Message**: `@AmazonHelp Not going to read instructions`

**Context**:
```text
[506083] @115821 shipping is a joke. Fourth package they have lost in the last month ! Why leave a package in the open !?\n[AmazonHelp] @506083 This isn't the experience we want you to have! Without giving account info, please let us know more about what's going on. ^BH
```

- **Proposed Intent**: OTHER
- **Proposed Confidence**: LOW
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 4
- **Reasons Flagged**:
  - LOW confidence
  - OTHER where the message appears to contain an actual support issue

---

### G-1040
**Customer Message**: `@AmazonHelp Status is “on the way”`

**Context**:
```text
[807034] @AmazonHelp how can I report an undelivered package with no tracking updates or news from the shipping company?\n[AmazonHelp] @807034 Greetings! Who is the carrier and what is the current status of your package listed here:  https://t.co/Y5jpI9gRhE ? ^TL
```

- **Proposed Intent**: OTHER
- **Proposed Confidence**: LOW
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 4
- **Reasons Flagged**:
  - LOW confidence
  - OTHER where the message appears to contain an actual support issue

---

### G-1041
**Customer Message**: `@AmazonHelp Initially amazon sent me a totally wrong item 

I raised a request for exchange, But in exchange, again they sent me wrong item 
First you sent me some other shoes and in exchange you sent me a shoes of different size.

This is really annoying`

**Context**:
```text
[143735] @115850 @AmazonHelp shame on your service if you can't deliver a correct item worth Rs.500 in 2 tries
1stly you sent a wrong item and now you sent a different size in EXCHANGE.
Worst app to order from..!

#cheaters
#fraudsters\n[AmazonHelp] @143735 That's very unusual. I understand your previous experience with us was unpleasant and we apologize for it. We'd like to make this right for you. Kindly drop your details here: https://t.co/beaaDm0muc and we’ll contact you soon. ^BV
```

- **Proposed Intent**: WrongItem
- **Proposed Confidence**: MEDIUM
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 4
- **Reasons Flagged**:
  - MEDIUM confidence

---

### G-1046
**Customer Message**: `@AmazonHelp Thanks for reply, I have dropped the details`

**Context**:
```text
[342212] Tricked me to load balance in Amazon pay promising extra cashback with save and subscribe orders and it was converted to COD @115850\n[AmazonHelp] @342212 Sorry to know that, we'd like a closer look. Please drop in your details here: https://t.co/GIJyeYqKE0 ^MS
```

- **Proposed Intent**: OTHER
- **Proposed Confidence**: MEDIUM
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 4
- **Reasons Flagged**:
  - MEDIUM confidence
  - OTHER where the message appears to contain an actual support issue

---

### G-1052
**Customer Message**: `I just hope @115821 gets my package here on time tomorrow 😭`

**Context**:
```text
[314389] Tried on my costume all together and 🔥
```

- **Proposed Intent**: DeliveryStatus
- **Proposed Confidence**: MEDIUM
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 3
- **Reasons Flagged**:
  - MEDIUM confidence

---

### G-1055
**Customer Message**: `@AmazonHelp Or at least I hope it's coming. The tracking status page is offering a date range saying to reach out to Amazon if I don't get it this week.`

**Context**:
```text
[467882] When you pay extra for @AmazonHelp Prime next day shipping, and now that item is coming later than the rest of your order.
```

- **Proposed Intent**: DeliveryStatus
- **Proposed Confidence**: MEDIUM
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 3
- **Reasons Flagged**:
  - MEDIUM confidence

---

### G-1057
**Customer Message**: `@AmazonHelp Thank you so much for your support. How i will return my mobile. Please help me. Today is the last date to return my mobile.`

**Context**:
```text
[138642] Many times i have told that mobile is not supporting the JIO sim and i am using only JIO sim. I don't have any other issue with this mobile. IT is difficult for me to continue with this mobile. Today is the last date after that i will unable to return @115821 @AmazonHelp\n[AmazonHelp] @138642 I get your concern. As mentioned earlier, we have sent you a correspondence with regards to your concern. For further assistance, please reply to the correspondence which you have received. We'll assist you further. ^JS
```

- **Proposed Intent**: RefundsAndReturns
- **Proposed Confidence**: MEDIUM
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 4
- **Reasons Flagged**:
  - MEDIUM confidence

---

### G-1058
**Customer Message**: `@AmazonHelp Package says USPS.`

**Context**:
```text
[290618] ?????? Not happy at fucking all. https://t.co/HYFe4ORzvg\n[698680] @290618 uh oh :/ 
either the package was lost/mixed up or worse somehow "stolen"
not good on amazon's part... they say its delivered and its not there? wtf?\n[290618] @698680 This is the fourth fuck up @115821 has made in the past month. Misplaced orders, shitty customer service, and response times that make me want to fucking die.\n[AmazonHelp] @290618 We're terribly sorry about that! We'd love to get this sorted for you. Could you please let us know which carrier was supposed to have delivered your games? We'd love to help further but we need a little more info. Thanks in advance! ^JD
```

- **Proposed Intent**: DeliveryStatus
- **Proposed Confidence**: MEDIUM
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 4
- **Reasons Flagged**:
  - MEDIUM confidence

---

### G-1059
**Customer Message**: `@AmazonHelp Filled out AGAIN. I'm not spending hours on this again. You guys can either figure this out or I'll take my business elsewhere. As it is, I'll be returning the $200 order if I ever receive it and buying a $1300 TV we were planning to purchase with you from Best Buy.`

**Context**:
```text
[185912] Hey @AmazonHelp remember 2 months ago when you promised me AMZL would no longer be handling my deliveries after things were continuously delivered to wrong place and delayed? Well today they delayed a $200 delivery. Beginning to transfer all my regular orders to other companies.\n[AmazonHelp] @185912 Hello, I am sorry to hear you are having troubles with this particular carrier. Please fill in this link provided and we will reach out to you as soon as possible:https://t.co/mk7tow11c4 ^CR\n[185912] @AmazonHelp Been there, done that. I spent hours dealing with this in September. You outright lied telling me AMZL, which is YOUR CARRIER, would not ever be delivering to me again and, yet, here I sit wasting even more of my time.\n[AmazonHelp] @185912 I'm sorry to hear that, as we can't see your account here on social media we would ask you to fill out that form once again so a member of our team can look into this for you.^MA
```

- **Proposed Intent**: OTHER
- **Proposed Confidence**: LOW
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 4
- **Reasons Flagged**:
  - LOW confidence
  - OTHER where the message appears to contain an actual support issue

---

### G-1063
**Customer Message**: `@AmazonHelp It hasn’t been that long, 10 months! It’s not even a year old.....`

**Context**:
```text
[200062] @115830 can I return a Bluetooth speaker that has stopped working only 10 months after purchasing? 🙏🏼🙏🏼\n[AmazonHelp] @200062 Hey, can you link us to the speaker you purchased? You can find it here: https://t.co/aaDyEz1VgE ^LB\n[200062] @AmazonHelp It was purchased December 2016\n[AmazonHelp] @200062 If you click on the item name, it should take you to the product page. When doing so, the link should be at the top. ^MH\n[200062] @AmazonHelp Is this correct??\n[AmazonHelp] @200062 Got it! If it was purchased near the holiday season, there may be a warranty. Have you contacted Sumvision customer service? ^MJ\n[200062] @AmazonHelp Excellent 😊 I have tweeted them but as of yet no reply. So it’s down to them now is it?\n[AmazonHelp] @200062 Because it's been so long since you've purchased, we recommend you contact the manufacturer for further assistance- yes. ^HC
```

- **Proposed Intent**: OTHER
- **Proposed Confidence**: LOW
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 4
- **Reasons Flagged**:
  - LOW confidence
  - OTHER where the message appears to contain an actual support issue

---

### G-1066
**Customer Message**: `@AmazonHelp Then atleast train your customer service and inform them about the new offers.
Also start a dedicated toll free number for customer service.`

**Context**:
```text
[198855] 1/2
@AmazonHelp 
I have orderd a product of 16000 rupees through amazon pay. The cashback should be added within 5 day as ur t&amp;c but ur...\n[AmazonHelp] @198855 Could you please tell us which cashback you are referring to? ^AG\n[198855] @AmazonHelp 15%cashback through amazon pay. From 4 to 8 october.\n[AmazonHelp] @198855 Thanks for the details, cashback will be credited within 5 days from date of shipping. 1/2 ^PS
```

- **Proposed Intent**: OTHER
- **Proposed Confidence**: LOW
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 4
- **Reasons Flagged**:
  - LOW confidence
  - OTHER where the message appears to contain an actual support issue

---

### G-1068
**Customer Message**: `@115821 I was supposed to get my package yesterday but now it won’t be here till tomorrow and I was trying out the prime deal because my children swear by it but I would of be better of paying for overnight... I already canceled my Prime for the year`

**Context**:
```text
[627407] @115821 your service failure has me canceling my Prime account...what a joke
```

- **Proposed Intent**: DeliveryStatus
- **Proposed Confidence**: MEDIUM
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 3
- **Reasons Flagged**:
  - MEDIUM confidence

---

### G-1070
**Customer Message**: `@AmazonHelp You message is not helpful. Really disappointed with the service.`

**Context**:
```text
[220855] @115850 why prices on product doesn’t match with listing price? Clear case of cheating... https://t.co/YSqGJQTOCh\n[AmazonHelp] @220855 a different batch or different M.R.P.s being used by manufacturers in different regions. Appreciate your understanding. (3/3) ^SD\n[220855] @AmazonHelp That means consumer has to pay extra even if its an issue from vendor. Aside i agreed to pay delivery charges but that doesn’t mean product product should be sold more than MRP.\n[AmazonHelp] @220855 AS informed earlier, M.R.P. of the product delivered is different from the M.R.P. given on the website due to various reasons including time lag in updating prices post changes in M.R.P, prices used by manufacturers in different regions. ^VH
```

- **Proposed Intent**: OTHER
- **Proposed Confidence**: LOW
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 4
- **Reasons Flagged**:
  - LOW confidence
  - OTHER where the message appears to contain an actual support issue

---

### G-1075
**Customer Message**: `@125690 @AmazonHelp Dang did you dirty too huh`

**Context**:
```text
[125690] @AmazonHelp no update on my one day shipping... do you refund the fee when I don't get my package in one day?\n[AmazonHelp] @125690 One-Day shipping refers to the time in transit once an order ships. Did we miss the delivery date in the confirmation e-mail? ^GG\n[125690] @AmazonHelp Yup. At 11:15 am there was a delay that happened at 4 pm... usps doesn't even show it has the package. https://t.co/8lYSbuqjDJ\n[AmazonHelp] @125690 I'm sorry for the delay! Please keep us posted, carriers have until 8PM to deliver. If you order doesn't arrive, let us know. ^AG\n[125690] @AmazonHelp Cool. First and last time I pay extra to get something the next day. I better get the fee back. https://t.co/dWBZGawQ2d
```

- **Proposed Intent**: OTHER
- **Proposed Confidence**: LOW
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 4
- **Reasons Flagged**:
  - LOW confidence
  - OTHER where the message appears to contain an actual support issue

---

### G-1076
**Customer Message**: `@AmazonHelp Still no reply as yet. Can you update me, as saying ‘out for delivery’ since 7.38am this morning? @115830 https://t.co/siH6BxQMNN`

**Context**:
```text
[340707] What is the point in being a prime member and preordering something to be delivered on the day of release only to be told it will take another 1-2 working day @115821? @115830 @AmazonHelp https://t.co/XyrsUCCQVR\n[AmazonHelp] @340707 Hi Gareth - Unforeseen circumstances can occur. I'm sorry your order didn't arrive by the original delivery estimate. We can take a look at your options with you here: https://t.co/qy3J24VGxb ^AF\n[340707] @AmazonHelp So what are the unforeseen circumstances that will cause up to a 2 day delay? Thanks.
```

- **Proposed Intent**: DeliveryStatus
- **Proposed Confidence**: MEDIUM
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 4
- **Reasons Flagged**:
  - MEDIUM confidence

---

### G-1078
**Customer Message**: `@AmazonHelp already mailed. you guys are offering me a refund so in a way my exchanged phone is gone and this phone too.`

**Context**:
```text
[194782] @115850 Worst experience with Amazon. Bought a mobile with exchange and it turned out to be a defective piece. No option for replacement\n[AmazonHelp] @194782 I'm sorry to know about the damage. Please report this to our support team here: https://t.co/vlvfJr4nN9. ^HA
```

- **Proposed Intent**: RefundsAndReturns
- **Proposed Confidence**: MEDIUM
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 4
- **Reasons Flagged**:
  - MEDIUM confidence

---

### G-1079
**Customer Message**: `@AmazonHelp This is so romantic.. Let's rebuild our relationship, either help me locate the book or a refund, whatever it is, don't make me leave u. 💖`

**Context**:
```text
[407748] Listen if sum1else accepted my gift &amp; they are so shameless that they don't return it &amp; my money is wasted I am leaving u fr gud. @115850\n[AmazonHelp] @407748 I'm sorry about the situation. Please reach out to us here: https://t.co/vlvfJr4nN9 we'd like to help. ^SG\n[407748] @AmazonHelp I don't wanna get angry @ you. But it will break my heart and affect our relationship. And I love you, don't do this to me. 💔😓\n[AmazonHelp] @407748 message on the letter I had written earlier, our destiny shall be re-written. (2/2)^GD
```

- **Proposed Intent**: RefundsAndReturns
- **Proposed Confidence**: MEDIUM
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 4
- **Reasons Flagged**:
  - MEDIUM confidence

---

### G-1089
**Customer Message**: `@AmazonHelp So there is no app ??`

**Context**:
```text
[116935] Last chance! Eligible Citi cardmembers, get a 4-month free trial when you sign up for Amazon Music Unlimited! Learn more https://t.co/Q9RAd7hMve https://t.co/gGj00GzYVb\n[707040] @116935 Any idea of coming to India sooner??? #waiting  #primemusic\n[AmazonHelp] @707040 Could you kindly let us know if you're using an of the Echo devices? ^JS\n[707040] @AmazonHelp Nope.just a prime membership, I could get it on a phone right?
```

- **Proposed Intent**: DigitalServices
- **Proposed Confidence**: MEDIUM
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 4
- **Reasons Flagged**:
  - MEDIUM confidence

---

### G-1094
**Customer Message**: `@AmazonHelp Here it is https://t.co/o2EFtHtGQC`

**Context**:
```text
[412696] @AmazonHelp hi my pre-ordered Xbox one X says delivery today on the app BUT then get an email to sats it's 14th Nov?? Which is it??\n[AmazonHelp] @412696 Hi, what is the latest tracking scan? ^TS\n[412696] @AmazonHelp It's at the Amazon bham hub that's roughly 8 miles from me but no updated activity since 4am so I don't know if it's coming today etc 😔😔\n[AmazonHelp] @412696 Hi Paul what does the latest scan on it say from 4 a.m.? ^AT
```

- **Proposed Intent**: OTHER
- **Proposed Confidence**: LOW
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 4
- **Reasons Flagged**:
  - LOW confidence
  - OTHER where the message appears to contain an actual support issue

---

### G-1095
**Customer Message**: `@AmazonHelp No ! I did NOT receive any email since 10 days !!! .. why cant u give me a precise answer..instead of shitting around !!`

**Context**:
```text
[128308] .@12379, gives a tough fight to Fire TV Stick by participating in the #CutTheCord challenge. Watch now. https://t.co/VfVJg2nHNV\n[121657] @128308 @12379 What about screen mirroring lags and data leaks !!!\n[AmazonHelp] @121657 Sorry you're upset with our product. Could you let us know more about this, we'd like to check it out? ^HA\n[121657] @AmazonHelp How many times? I raised a complaint on 15th sep!  Are u guys sleeping???\n[AmazonHelp] @121657 correspondence with further issues/query on this and we'll be happy to take it over from there. 2/2 ^AB\n[121657] @AmazonHelp Updates please.. almost a month now !!!\n[AmazonHelp] @121657 Could you share the update provided by our team, without sharing the order detail. ^HR\n[121657] @AmazonHelp no updates shared !!!\n[AmazonHelp] @121657 Are you referring to the issue regarding your Fire TV? Just to clarify. ^CB\n[121657] @AmazonHelp Yes sir ! And u ppl seem to sleeping on that since a month now !!\n[AmazonHelp] @121657 Apologies for this ordeal. Please share your details here: https://t.co/GIJyeYqKE0 and I'll get in touch with you. ^HD\n[121657] @AmazonHelp I have shared the details multiple times..u ppl shud be ashamed of urself for even askin me for this !\n[AmazonHelp] @121657 If you've shared your details, you must have received a correspondence from our team. Request you to revert to the same. ^SQ\n[121657] @AmazonHelp I shared a sceenshot of mail chain ..which tells that i dint get any reply since 10 days.. ppl r seeing herevhow pathetic amazon help is. !\n[AmazonHelp] @121657 I'm sorry the issue is pending since a long time. May I know if the issue is pending 1/2 ^SH\n[121657] @AmazonHelp Amazon.in\n[AmazonHelp] @121657 Kindly check your spam folders as well and do keep us posted. 2/2 ^MM
```

- **Proposed Intent**: OTHER
- **Proposed Confidence**: LOW
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 4
- **Reasons Flagged**:
  - LOW confidence
  - OTHER where the message appears to contain an actual support issue

---

### G-1097
**Customer Message**: `@AmazonHelp Amazon. It was a sporting goods item that came in just in an Amazon box, not its manufacturer packaging so I was suspicious from the start but gave the time for it to break in &amp; it has not.`

**Context**:
```text
[632162] @115821 pretty sure Amazon is selling certain fake products and when customers realize the products they ordered are fake, Amazon says, "sorry but you're past the refund/return time frame."\n[AmazonHelp] @632162 if any item you receive doesn't follow the policy stated here: https://t.co/Vu2CtLBEzl (2/2) ^LR\n[632162] @AmazonHelp I've already contacted CS &amp; my only response was, "sorry you're passed the return time." 20% of the product's reviews complain of it being fake and they go back a couple of years so clearly Amazon is knowingly selling fake products.\n[AmazonHelp] @632162 Was this item shipped and sold by Amazon or a third-party seller?  ^DD
```

- **Proposed Intent**: OTHER
- **Proposed Confidence**: LOW
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 4
- **Reasons Flagged**:
  - LOW confidence
  - OTHER where the message appears to contain an actual support issue

---

### G-1099
**Customer Message**: `@AmazonHelp You see, I've searched and low for quality products. But my options are just amazingly limited by my foot size. Please help me.`

**Context**:
```text
[168354] @115850 @118702 why do I never get size 12 clogs below 1000? Ik i have huge feet but its really disheartening to see the options I have😣\n[AmazonHelp] @168354 time to time to see if this item has become available. (3/3) ^VM
```

- **Proposed Intent**: OTHER
- **Proposed Confidence**: LOW
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 4
- **Reasons Flagged**:
  - LOW confidence
  - OTHER where the message appears to contain an actual support issue

---

### G-1100
**Customer Message**: `@AmazonHelp Hier bahnt sich der nächste Fall an. Zustellung heute, aber das Paket ist noch nicht einmal versandt worden. Das Problem scheint sich zur Regel zu entwickeln 😡 https://t.co/Xg4G1iRpBG`

**Context**:
```text
[471572] @116316 Was ist los bei Amazon Logistics in Bochum? Pakete an Amazon Locker verzögern sich um Tage. Unbefriedigend! Besser DHL/Hermes? https://t.co/NOkQRFyGnI\n[AmazonHelp] @471572 Deine Verärgerung kann ich verstehen. Allerdings bitte ich dich hier um etwas Geduld, bis das angegebene Datum erreicht ist.\n[471572] @AmazonHelp Ich will nur verstehen, was da klemmt. Sachen werden laut Status gestern um 10:38 ausgeliefert und sind heute um 19:45 noch nicht im Locker.\n[AmazonHelp] @471572 Über Twitter haben wir leider keinen Einblick in deine Bestellung. Die Kollegen prüfen das gerne: https://t.co/ohyvGrpvrY ^SI\n[471572] @AmazonHelp Nächstes Paket verzögert mit unbekanntem Lieferdatum. Hotline kann nicht helfen, hat keinen Kontakt zu Amazon Logistics. Geld wird aber abgebucht. WTF??? Wofür zahlt man Prime-Aufschlag???\n[AmazonHelp] @471572 Wir schauen uns das genauer an. Melde dich bitte hier, bei uns im Amazon.de Social Media Team: https://t.co/br7bhrDkeG ^DS\n[471572] @AmazonHelp Pakete sind mit bis zu zwei Tagen Verspätung angekommen und sehen so aus. Was genau stimmt bei Amazon Logistics nicht?! https://t.co/jUBsaDb54O\n[AmazonHelp] @471572 Das würden wir gerne herausfinden, melde dich bitte dazu über den Link von ^DS. Gruß ^TR
```

- **Proposed Intent**: OTHER
- **Proposed Confidence**: LOW
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 4
- **Reasons Flagged**:
  - LOW confidence
  - OTHER where the message appears to contain an actual support issue

---

### G-1104
**Customer Message**: `@AmazonHelp When you guys say 2-3 days is it normally 20-30 days? I still haven't gotten my refund.`

**Context**:
```text
[181433] I’m tired of fighting with @115850. Clearly it’s @115821’s step child no one gives a fuck about.\n[181433] @115850 @115821 @AmazonHelp is like a pacifier. It’s not the real thing, but it’ll keep the customers calm for a while until they realise it’s shit.\n[AmazonHelp] @181433 Interesting conjecture! As intimated earlier, please reply to our email with further query on this and we'll be happy to help. ^AB\n[181433] @AmazonHelp I’ve done it all. Spoken to 5 reps. Responded to mails. Nothing has changed in 7 days.\n[AmazonHelp] @181433 What we meant was for you to reply to the email sent by the Social Media team. Once you do, please let us know. Thank you. ^PN\n[181433] @AmazonHelp I did reply previously and that is how Nikhil got in touch with me on Sunday. Have responded to Nikhil's mail as well now. I'm tired now.\n[AmazonHelp] @181433 We've responded to you via DM, Kindly check. ^AP\n[181433] @AmazonHelp Haven't gotten anything now. Already filled in the link provided to me at 1:05PM today.\n[AmazonHelp] @181433 We'd appreciate your patience while we work on this. We'll reach out to you soon. ^KJ
```

- **Proposed Intent**: RefundsAndReturns
- **Proposed Confidence**: MEDIUM
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 4
- **Reasons Flagged**:
  - MEDIUM confidence

---

### G-1106
**Customer Message**: `@AmazonHelp (1) No and that’s where my troubles lie, I don’t know when the item will be delivered, it’s in KY now, and if the rebuy item sells out -`

**Context**:
```text
[489037] @AmazonHelp I was told at one point that all I needed to do was drop off my return at UPS to receive my refund, is that valid info?\n[AmazonHelp] @489037 When you're refunded for a return can depend on different variables. Please click here for info: https://t.co/KmT0xZeVbr ^LR\n[489037] @AmazonHelp Can someone check about mine cause I was told I was eligible for an instant refund?\n[AmazonHelp] @489037 We're not able to look up account information via Twitter. How long has it been since you contacted us for the return? ^JP\n[489037] @AmazonHelp Can someone help? item I need to rebuy is close to selling out and I picked a gift card refund so it would be quicker.\n[AmazonHelp] @489037 We're still here for you! When you contacted us via phone/chat, what info or insight was provided regarding the refund? ^JE\n[489037] @AmazonHelp (3) I’ll have hundreds of dollars sitting in a gift card I’m really scared.\n[AmazonHelp] @489037 It doesn't sound like Instant Refund is set up. Has the gift card refund been issued: https://t.co/BldLIi2na6? (1/2)
```

- **Proposed Intent**: OTHER
- **Proposed Confidence**: LOW
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 4
- **Reasons Flagged**:
  - LOW confidence
  - OTHER where the message appears to contain an actual support issue

---

### G-1110
**Customer Message**: `@AmazonHelp USPS`

**Context**:
```text
[784684] @115821 it says my package was delivered at 4:44 pm but it's not here. Can u help me?\n[AmazonHelp] @784684 We'd love to assist! Could you provide us with the carrier? If you are unaware, you can locate that info here: https://t.co/Y5jpI9gRhE ^AR
```

- **Proposed Intent**: DeliveryStatus
- **Proposed Confidence**: MEDIUM
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 4
- **Reasons Flagged**:
  - MEDIUM confidence

---

### G-1112
**Customer Message**: `@AmazonHelp Nope. Never. He's had the card for years, not moved, and only worked together briefly. Also the billing address is totally incorrect`

**Context**:
```text
[634953] Hi @AmazonHelp and @74936 care to explain how a colleagues credit card details ended up on my Amazon account? https://t.co/KkKTNyt2EN\n[634953] @AmazonHelp @74936 If it helps I've checked my order history and there's nothing from my colleague on there, and I can also use the card for my other addresses https://t.co/7ZQKVMpgj4\n[AmazonHelp] @634953 Have you and your colleague ever used the same pc maybe and he could have added his card to your account by accident? ^KM
```

- **Proposed Intent**: WrongItem
- **Proposed Confidence**: MEDIUM
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 4
- **Reasons Flagged**:
  - MEDIUM confidence

---

### G-1115
**Customer Message**: `@AmazonHelp Phone  bought  is not good or it doesn't have fame alloverworld the phone is getting fame n here Amazon is delivering defective product`

**Context**:
```text
[431099] @115821 my no.  9659519713 n email address kangsabanikbalram9@gmail.... kindly check my account details..and Give me solution ...shit websit\n[AmazonHelp] @431099 We do not have access to your account on social media. Please tell us what went wrong, we'd like to help you. (1/2)^BS
```

- **Proposed Intent**: DamagedOrDefective
- **Proposed Confidence**: MEDIUM
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 4
- **Reasons Flagged**:
  - MEDIUM confidence

---

### G-1116
**Customer Message**: `@AmazonHelp Have not. This is my old account. All my payment info &amp; address is in there. This happened after the 'Halloween Shop' update.`

**Context**:
```text
[302632] @AmazonHelp It seems my Prime membership was randomly cancelled and my account was cleaned out of all activity. What is this?o_0\n[AmazonHelp] @302632 We're sorry to hear that! Have you recently created a new account under a different e-mail address? ^WM
```

- **Proposed Intent**: OTHER
- **Proposed Confidence**: LOW
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 4
- **Reasons Flagged**:
  - LOW confidence
  - OTHER where the message appears to contain an actual support issue

---

### G-1117
**Customer Message**: `@AmazonHelp How can I reply when no option showing in that email`

**Context**:
```text
[343708] @115850 if you can't provide the services then you should stop the business in India.Sham on you.\n[AmazonHelp] @343708 Just to confirm, have you dropped in your details using the link provided by ^BA ? We'd like to have a look into it. ^AB\n[343708] @AmazonHelp But I m still waiting for response and resolution\n[AmazonHelp] @343708 An email has already been sent with a reply. Kindly check it from the link shared here: https://t.co/NTkrxpsbHJ ^KA\n[343708] @AmazonHelp I m not satisfied with that email .you are saying pl order again .how I will get the same offer which I got earlier.kindly confirm\n[AmazonHelp] @343708 I get your concern, please reply to the email correspondence and we'll get back to you at the earliest. ^PS\n[343708] @AmazonHelp There is no reply option showing. Can you share the reply link ?\n[AmazonHelp] @343708 reply once you open the email sent by our team using your registered email ID. 2/2 ^RS\n[343708] @AmazonHelp ?????\n[AmazonHelp] @343708 You'll be able to find a reply option to our email on the website. If the same issue persists, let us know. ^RS\n[343708] @AmazonHelp Yes same issue\n[AmazonHelp] @343708 Reply to the email from the account and we will assist you accordingly. (2/2)^HR\n[343708] @AmazonHelp No option of reply showing\n[AmazonHelp] @343708 assist you with further information unless we receive a correspondence for the email. (2/2)^HR
```

- **Proposed Intent**: OTHER
- **Proposed Confidence**: LOW
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 4
- **Reasons Flagged**:
  - LOW confidence
  - OTHER where the message appears to contain an actual support issue

---

### G-1118
**Customer Message**: `@AmazonHelp it was actually delivered this time. but it's always your drivers when i don't get my packages. i've already been through this with y'all.`

**Context**:
```text
[191894] wow. so @115821 calls to say the access pad for my bldg ≠ working. he was pushing # first b/c whatever staff noted my code put it as #xxxx\n[191894] @115821 mind you, the other part of his screen just says xxxx. and? THE INSTRUCTIONS ON THE ACCESS PAD SAY XXXX.

him: we can only use our screen.\n[191894] @115821 i told him it's okay to use his brain. he repeated that he can only use what's on [apparently jus the one part of] his screen.

why are ppl?\n[191894] @115821 i just realized something else:

the instructions on the access pad have the number to the management office, too, so he dialed that one.\n[AmazonHelp] @191894 I'm so sorry your order wasn't delivered! What's the carrier and latest tracking scan here: https://t.co/PCtircFm5C? ^JN
```

- **Proposed Intent**: OTHER
- **Proposed Confidence**: LOW
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 4
- **Reasons Flagged**:
  - LOW confidence
  - OTHER where the message appears to contain an actual support issue

---

### G-1120
**Customer Message**: `@AmazonHelp Excellent. This is the same to same reply read out by CC.
Excellent job.
This kind of replies are comfortable for u ,but not for customers. 
We are purchasing products in e-commerce website, But not shares in share market.`

**Context**:
```text
[148070] @115850 I have ordered phone yesterday. 
Price reduced even before it's delivery. 
Talked to CC, but not helpful at all.
CC told that phone prices changes every second like stock market. LOL\n[AmazonHelp] @148070 Pricing and offers are decision of the sellers. The constantly changing marketplace and our efforts to offer you the lowest price, may result in fluctuations in our prices over time. ^VH
```

- **Proposed Intent**: OTHER
- **Proposed Confidence**: LOW
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 4
- **Reasons Flagged**:
  - LOW confidence
  - OTHER where the message appears to contain an actual support issue

---

### G-1124
**Customer Message**: `@AmazonHelp Thanks for your attempt to help, was able to resolve it on my own, wish the customer service had more out side the box thinking`

**Context**:
```text
[500897] @115821 after a almost a dozen emails, At least 4 phone calls, and 2 click to chats, I have given up on your customer service, stole my $$\n[AmazonHelp] @500897 I'm sorry for the frustration! Can you tell us a bit more? What information or options have been provided when contacting us? ^ST
```

- **Proposed Intent**: OTHER
- **Proposed Confidence**: MEDIUM
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 4
- **Reasons Flagged**:
  - MEDIUM confidence
  - OTHER where the message appears to contain an actual support issue

---

### G-1125
**Customer Message**: `@115940 @hulu_support @AmazonHelp`

**Context**:
```text
[140318] @115940 y’all never load on my firestick even with good wifi connection. what the hell
```

- **Proposed Intent**: OTHER
- **Proposed Confidence**: LOW
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 3
- **Reasons Flagged**:
  - LOW confidence
  - OTHER where the message appears to contain an actual support issue

---

### G-1126
**Customer Message**: `@AmazonHelp Instead of the competition because of your “reliable process” but i have been left to wait and dissapointed way to many times.`

**Context**:
```text
[451318] @115821 @AmazonHelp I wish your customer service would stay as good as it used to be. Your customer service is horrendous as of late!\n[AmazonHelp] @451318 I'm sorry for your poor experience. Without providing personal or account details, will you give some details on what happened? ^LL\n[451318] @AmazonHelp Its a combination of things. Packages with prime guaranteed to get here dont get here, Rude people on the chat, rude supervisors...\n[AmazonHelp] @451318 That's certainly not the experience we want for our customers. When you last spoke with us, what info/options were provided? ^NS
```

- **Proposed Intent**: OTHER
- **Proposed Confidence**: LOW
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 4
- **Reasons Flagged**:
  - LOW confidence
  - OTHER where the message appears to contain an actual support issue

---

### G-1129
**Customer Message**: `@AmazonHelp That's what I am reporting, its a bug in your system, where #developer team needs to be engaged! I am not bothered with reviews!`

**Context**:
```text
[242502] @115850 @AmazonHelp Hi, why I am not able to post reviews for the product which I bought? https://t.co/r81ccxzU99\n[AmazonHelp] @242502 Request you to follow the guidelines to post a successful review. ^RW\n[242502] @AmazonHelp Guideline says I should not be directly or indirectly associated with product as in biased comment, which am satisfying. Then why not allow?\n[AmazonHelp] @242502 Reviews are system approved, service related discrepancies will not be taken. ^MJ
```

- **Proposed Intent**: OTHER
- **Proposed Confidence**: LOW
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 4
- **Reasons Flagged**:
  - LOW confidence
  - OTHER where the message appears to contain an actual support issue

---

### G-1131
**Customer Message**: `@AmazonHelp (looks impatiently at watch)
(looks impatiently at calendar)

This Twitter account appears to be some form of placebo.`

**Context**:
```text
[227732] Hey, @AmazonHelp:
Someone is stalking me on your platform using the name of a stalking victim who committed suicide.
https://t.co/uMorv2gy9u https://t.co/DkstOgXNLw\n[AmazonHelp] @227732 Hey Tim. Please forward your details - https://t.co/tkLCr7DNil we'd like to investigate further. ^TP\n[227732] @AmazonHelp Done.
```

- **Proposed Intent**: OTHER
- **Proposed Confidence**: LOW
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 4
- **Reasons Flagged**:
  - LOW confidence
  - OTHER where the message appears to contain an actual support issue

---

### G-1134
**Customer Message**: `@AmazonHelp I have emailed the customer service line due to I do not wanting all my info on a social media site . Thank you`

**Context**:
```text
[301076] SERIOUSLY @115821 !? I put a sign that says do not know place package on porch . YOU WOKE MY KIDS ! Learn to read !!  #learntoread 😡😡😡\n[AmazonHelp] @301076 I'm sorry for this! Who was the carrier for your order? We'd like to help! ^KJ\n[301076] @AmazonHelp Carrier
AMZL US\n[AmazonHelp] @301076 Please provide as much information as possible here: https://t.co/8ZjW0Jro6O ^ZW
```

- **Proposed Intent**: OTHER
- **Proposed Confidence**: MEDIUM
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 4
- **Reasons Flagged**:
  - MEDIUM confidence
  - OTHER where the message appears to contain an actual support issue

---

### G-1137
**Customer Message**: `@AmazonHelp I also don’t understand why my refund will take 5-7 days? When I buy an item it comes out of my account almost straight away &amp; certainly by the following day.`

**Context**:
```text
[803928] Absolute nightmare with my order @115830 and now emails are going back and forth with no resolution 😡\n[803928] @115830 I emailed again today &amp; received a reply that my money would be returned. I don’t want my money back - I want the items I ordered. One of the items was ordered on Black Friday at a reduced price and it is now back to the original price - I now need to reorder &amp; pay more!\n[AmazonHelp] @803928 Thank you for letting us know. Were any of the items sold by a third-party seller? If so, we are unable to issue a replacement, as it is not considered our item. ^SB
```

- **Proposed Intent**: RefundsAndReturns
- **Proposed Confidence**: MEDIUM
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 4
- **Reasons Flagged**:
  - MEDIUM confidence

---

### G-1140
**Customer Message**: `@164818 @AmazonHelp last week @115830 sent me the wrong version of a game because they had increased the price after i'd bought it,. Good luck with this`

**Context**:
```text
[164818] Preordered this the second it was announced, and @115821 screw me in the final few days 😩 @117331 @116543 @115787 @115788 https://t.co/BCSHQUPUow\n[AmazonHelp] @164818 Hi James, have you been able to double-check your payment details are up to date? ^TS\n[164818] @AmazonHelp It's all correct and up to date, I have used the same card recently elsewhere, and previously on Amazon to order without hassle.\n[AmazonHelp] @164818 Sorry to see that, have you received an email with more info about the delay? ^JJ\n[164818] @AmazonHelp No emails, and it has only been updated with this today, despite being preordered in September\n[AmazonHelp] @164818 We only try to take payment before we dispatch the item. ^AT\n[164818] @AmazonHelp I've not received an email, nor has my bank flagged anything. It's been rectified so dispatch today as planned should still stand!
```

- **Proposed Intent**: OTHER
- **Proposed Confidence**: LOW
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 4
- **Reasons Flagged**:
  - LOW confidence
  - OTHER where the message appears to contain an actual support issue

---

### G-1141
**Customer Message**: `@AmazonHelp And please keep your doubts to yourself.  Admit that you messed up! Instead of putting ifs and buts.`

**Context**:
```text
[120613] Dearest @115850 this is not expected from you guys. This package was supposed to reach me by Fri. Havent yet got an update! https://t.co/QvgTdMpWUi\n[AmazonHelp] @120613 I'm sorry for the delay with your order. Please reach out to our support team here: https://t.co/2t6DQoUmNZ for assistance.^RW\n[120613] @AmazonHelp I did call the customer service. But, they were unable to provide any update!\n[AmazonHelp] @120613 I'd like to look into the issue and assist you with it. Please provide your details here: https://t.co/FOWMWAwwM3 1/2 ^SH\n[120613] @AmazonHelp I did provide details and was promised a call back in 7 hours. Well, 24 has passed. This is ugly customer service.\n[AmazonHelp] @120613 Sorry about that. Could you please check if you've received an email in response to the details you shared earlier? ^NR\n[120613] @AmazonHelp I did recieve an email indicating the package is being returned to the fulfillment centre. What type of nonsense is this?\n[AmazonHelp] @120613 If you've provided the details earlier in the link, you should've received an email from the social media team. ^NR\n[120613] @AmazonHelp Ok, so you are now foubting whether i provided details or not. Thank you for your wonderful service. Such wonderful new lows.\n[120613] @AmazonHelp Maybe when you guys do the marketing gimmicks you should put these stuff up. So I buy something and it doesn't even reach me. Wow!
```

- **Proposed Intent**: OTHER
- **Proposed Confidence**: LOW
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 4
- **Reasons Flagged**:
  - LOW confidence
  - OTHER where the message appears to contain an actual support issue

---

### G-1144
**Customer Message**: `@AmazonHelp 24 hours later, the product MRP is unchanged. You continue to mislead/cheat customers with false info on your site.`

**Context**:
```text
[382177] @115850 Isn’t this cheating? Note MRP. https://t.co/cVyuOzkfgh\n[AmazonHelp] @382177 Prices offered varies from location to seller. You can learn more about it here: https://t.co/7NfAIkxIqJ ^RW\n[382177] @AmazonHelp I am talking about MRP! Not the price.\n[AmazonHelp] @382177 listed on the product shared by our sellers. For further information please refer to the link here: https://t.co/LdvZH5j1Ah ^MJ\n[382177] @AmazonHelp So you basically say that you are not responsible for a FALSE and incorrect information used to Lure a customer?\n[AmazonHelp] @382177 Request you to visit the following link for more information : https://t.co/yQb39uNRsX [2/2]^SK\n[382177] @AmazonHelp You are now saying that you do not own responsibility if someone CHEATS me or indulges in unfair trade practices on your website. @4031\n[AmazonHelp] @382177 I understand your concern. I'll pass on your feedback internally. For more info on this, kindly follow the link shared earlier. ^ST
```

- **Proposed Intent**: OTHER
- **Proposed Confidence**: LOW
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 4
- **Reasons Flagged**:
  - LOW confidence
  - OTHER where the message appears to contain an actual support issue

---

### G-1145
**Customer Message**: `@AmazonHelp Can y’all just replace the order 🙄. Your rep said it wasn’t in stock anymore but it is. Why is this so difficult`

**Context**:
```text
[240102] @115817 scanned my package on 11/26 and hasn’t scanned it again and claims I need to call amazon back for the package they lost\n[UPSHelp] @240102 Per our agreement with Amazon, they require that the all investigations are initiated with them. Due to this you will need to contact the shipper. I definitely apologize for any inconvenience this has caused. ^SK\n[240102] @UPSHelp So basically I have to start a dispute with amazon (who did nothing wrong) to figure out what happened to the package that was lost while in ups possession? 🤦🏿‍♂️\n[AmazonHelp] @240102 I'm sorry to hear your order was lost Laron. We'd like to help look into available options with you at this link here: https://t.co/hApLpMlfHN ^VS\n[240102] @AmazonHelp I just spoke with your customer service and was told my order is it in Houston. Didn’t look like it to me. I was also told that the order can’t be replace but it also still in stock @115817 has yet to provide amazon with confirmation of the status of this package https://t.co/2gRu3reNS3\n[AmazonHelp] @240102 Thank you for providing us with these details. When you spoke with us, did we provide any additional information or options regarding this specific shipment? ^BV\n[240102] @AmazonHelp They tried to convince me that the order was in Houston. After getting past that hurdle, I was told the order can’t be replaced because it was not in stock. I was then told that I would be given a gift card. The rep is to call ups to determine the status\n[AmazonHelp] @240102 I understand the inconvenience and frustration a late shipment can cause! Although not ideal, I'm glad to hear we were able to create a refund for you. ^BV\n[240102] @AmazonHelp I haven’t got the email notification for that refund but thanks\n[AmazonHelp] @240102 You can check the payment method that was refunded and the status of your refund here: https://t.co/NCq7DulfLb Let us know if this helps! ^SC
```

- **Proposed Intent**: CustomerServiceEscalation
- **Proposed Confidence**: MEDIUM
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: ESCALATE
- **Proposed Reply Quality**: 4
- **Reasons Flagged**:
  - MEDIUM confidence

---

### G-1146
**Customer Message**: `@AmazonHelp Ya lo hicimos, incluso hablamos al banco para verificar la información y es la misma.`

**Context**:
```text
[286522] @116875 Hola Amazon! Llevo dos semanas tratando de tratando de realizar una compra y no e podido, además de que tardan en responderme\n[AmazonHelp] @286522 Hola Monse, ¿recibes algún tipo de mensaje de error al intentar realizar tu compra? ^LG\n[286522] @AmazonHelp No han podido validar un num de tel y dirección del titular de la tarjeta y ya mandaron por correo la información y no recibimos respuesta\n[AmazonHelp] @286522 ¿Cuándo enviaste la información solicitada? ^JQ\n[286522] @AmazonHelp La primera vez hice el pedido de una cuenta fue el 27 de sept y hasta el 5 de oct me dijeron que no se podía validar la info de la tarjeta\n[286522] @AmazonHelp El día de ayer volví a intentar a realizar la compra desde otra cuenta, y mandaron el mismo mensaje de validar la información\n[AmazonHelp] @286522 Te recomiendo confirmar que los datos enviados concuerden con la información registrada en tu banco. ^JQ
```

- **Proposed Intent**: OTHER
- **Proposed Confidence**: LOW
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 4
- **Reasons Flagged**:
  - LOW confidence
  - OTHER where the message appears to contain an actual support issue

---

### G-1147
**Customer Message**: `@AmazonHelp I don't need your sorry.. I need my my refund asap. @1840`

**Context**:
```text
[183033] No refund of my money since one month, name mismatch in cheque and bank a/c @AmazonHelp   order no #403-8295304-4660353\n[183033] @AmazonHelp Still awaiting my refund @AmazonHelp\n[AmazonHelp] @183033 I see that we've sent you a correspondence. Kindly check the same here: https://t.co/ubzNHWZvL2 ^SG\n[183033] @AmazonHelp It has been 58 days now. No refund till now.\n[AmazonHelp] @183033 Please respond to our reply sent to you from our escalations team. We will get back to you with the resolution. ^GU\n[183033] @AmazonHelp I have done it all. Please check with your end.\n[AmazonHelp] @183033 However, since you've responded to the email sent by the Soial Media team you'd be receiving an update soon. 2/2 ^EM\n[183033] @AmazonHelp What is the update? Please tell me, does it take 55 days for processing the refund?\n[AmazonHelp] @183033 I'm sorry for the stretch. Please refer to our correspondence here: https://t.co/8DAc10S7ww ^AP\n[183033] @AmazonHelp Very poor service from Amazon. Still awaiting for my refund.. More than 60days now...\n[AmazonHelp] @183033 I'm sorry it is longer than expected. We're working on it and will get back to you soon. ^VH\n[183033] @AmazonHelp What is the update of my refund?still I have not got my money back. Even after so many promises have been made to me for same.\n[AmazonHelp] @183033 An email has already been sent with a reply. Kindly check it from the link shared here: https://t.co/NTkrxpsbHJ ^HR\n[183033] @AmazonHelp Please don't play around. I have been promised by Amazon many times for refund but fact is it is not honoring.\n[AmazonHelp] @183033 We are working on it. We will reach out to soon with an update.

Rahul | Amazon Customer Service\n[183033] @AmazonHelp Please stop fooling around. Really  disappointed, there is zero accountability. Every time many promises made to me and failed honoring that\n[AmazonHelp] @183033 Apologies for the unpleasant experience. We wouldn't be able to access your account on Twitter. Kindly reply to the email you received from our team for further assistance. ^BV\n[183033] @AmazonHelp I am done with unprofessional Amazon service, for my refund i.e only Rs 600 I have do this much circus and follow up, I don't think so.\n[AmazonHelp] @183033 We haven't received your reply. Please reply to the email from Social Media Team and we'll get back to you at the earliest. ^PS\n[183033] @AmazonHelp I have done it many times. I am not interested doing it again and again. You have all details with you. Don't trouble me.\n[AmazonHelp] @183033 We are working on it. We will check and connect with you accordingly. ^RW\n[183033] @AmazonHelp Shame on you Amazon and your service team. Worst experience ever. Three months now, no refund!\n[AmazonHelp] @183033 We have already sent you a correspondence regarding the refund. Kindly check the same here: https://t.co/DTSNmGldJf. ^JS\n[183033] @AmazonHelp Crap. Stop lying! @1840 #SureshPrabhu\n[AmazonHelp] @183033 Apologies for the confusion. Kindly drop in your details here: https://t.co/beaaDm0muc and we'll reach out to you with an update. Also, please ensure you enter the details of the account through which the order was placed. Appreciate your understanding. ^EM\n[183033] @AmazonHelp I have done it many times and again this time as well. Please check! @1840\n[AmazonHelp] @183033 We've emailed a correspondence to you. Kindly check it here: https://t.co/sC1mf2vwg9 and reply to it for further assistance. ^SF\n[183033] @AmazonHelp I didn't receive any correspondence. Please email it to me.\n[AmazonHelp] @183033 We've sent you a communication. Please use the same account to log in and check for the same. ^RW\n[183033] @AmazonHelp Here it is https://t.co/ab5rchgdaP\n[AmazonHelp] @183033 Kindly reply to the correspondence, we'll reach out to you. 
Also, please don't provide your order details, as we consider it to be personal information. Our Twitter page is visible to the public. ^AP\n[183033] @AmazonHelp There is some understanding problem. When I am clearly telling you people that all this exercise I have done it many times. I am not going to do again and again. Hope I am clear!! You have my no Pl call me. @1840\n[AmazonHelp] @183033 I'm sorry for the inconvenience regarding your refund. We'll get in touch with you soon. ^AM
```

- **Proposed Intent**: RefundsAndReturns
- **Proposed Confidence**: MEDIUM
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 4
- **Reasons Flagged**:
  - MEDIUM confidence

---

### G-1150
**Customer Message**: `@AmazonHelp Can you contact the courier to see where it is?`

**Context**:
```text
[412761] Can you please tell me if my replacement package is actually going to get delivered today!? @AmazonHelp\n[AmazonHelp] @412761 Hello, John! We aren't able to see order information on Twitter. Is the tracking on time? https://t.co/Y5jpI9gRhE ^RM\n[412761] @AmazonHelp 1. My name ain’t John. 2. It still says by 9PM tonight but it was supposed to be delivered yesterday and wasn’t! So a replacement was sent\n[AmazonHelp] @412761 I'm sorry for the wait, Josh. Which carrier is assigned for delivery? Please let us know if it's not delivered by 9:00p.m. ^MV
```

- **Proposed Intent**: CourierFeedback
- **Proposed Confidence**: MEDIUM
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 4
- **Reasons Flagged**:
  - MEDIUM confidence

---

### G-1153
**Customer Message**: `@AmazonHelp I am leaving tomorrow tomorrow morning. I need the solution ASAP.`

**Context**:
```text
[505131] @115850 @AmazonHelp I hd placed an one-day delivery order. It hasnt arrived yet and the delivery boy has swchd off his phn. Ur srvc sucks! https://t.co/WU4JYZ5wCy\n[AmazonHelp] @505131 Sorry for the hassle. Please report this to our support team here: https://t.co/vlvfJr4nN9 and we'll check this. 1/2^HN
```

- **Proposed Intent**: OTHER
- **Proposed Confidence**: LOW
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 4
- **Reasons Flagged**:
  - LOW confidence
  - OTHER where the message appears to contain an actual support issue

---

### G-1154
**Customer Message**: `@AmazonHelp Ordered 4 Nov with 5 Nov delivery still not despatched and no new date great birthday present that will be!`

**Context**:
```text
[506978] @115830 so much for next day delivery - I am on day 2 and still my parcel has not been despatched despite chatting twice with your team?\n[AmazonHelp] @506978 Hi, sorry to hear that, what is the estimated delivery date of your order: https://t.co/aaDyEz1VgE? ^JJ
```

- **Proposed Intent**: DeliveryStatus
- **Proposed Confidence**: MEDIUM
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 4
- **Reasons Flagged**:
  - MEDIUM confidence

---

### G-1158
**Customer Message**: `@AmazonHelp What's your phone number?`

**Context**:
```text
[AmazonHelp] @161464 Letting you down is never our intent! To escalate carrier feedback &amp; explore further options, please call us once more. ^MV
```

- **Proposed Intent**: OTHER
- **Proposed Confidence**: LOW
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 4
- **Reasons Flagged**:
  - LOW confidence
  - OTHER where the message appears to contain an actual support issue

---

### G-1159
**Customer Message**: `@AmazonHelp Received notification that the package was lost.`

**Context**:
```text
[164806] Conflicting messages regarding the delivery of a package I waited for all day. What gives, @115821? #AmazonPrime https://t.co/kOWdjYeGvP\n[AmazonHelp] @164806 I am unable to view your account details via Twitter. Contact us by phone or chat using:  https://t.co/hApLpMlfHN  ^CH
```

- **Proposed Intent**: DeliveryStatus
- **Proposed Confidence**: MEDIUM
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 4
- **Reasons Flagged**:
  - MEDIUM confidence

---

### G-1160
**Customer Message**: `@AmazonHelp Yep, the delivery driver claims he can't get to my door. It's never been a problem in the past`

**Context**:
```text
[663012] Hey @115821 it's good to know when you guarantee next day delivery, you really mean it will be here when you feel like it. Your service has declined over my last few deliveries\n[AmazonHelp] @663012 Hello, Chris! Sorry to hear about this! Have we missed a delivery date that was provided at check out? Please let us know details without giving account or personal information! ^MW
```

- **Proposed Intent**: DeliveryStatus
- **Proposed Confidence**: MEDIUM
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 4
- **Reasons Flagged**:
  - MEDIUM confidence

---

### G-1163
**Customer Message**: `@AmazonHelp I've responded, my email confirmation displays the correct product but when I click the product link it takes me to a different item!`

**Context**:
```text
[737053] @AmazonHelp Placed an order for a necklace on the Black Friday deals, on my orders one minute it's the correct item, the next it's a completely different item. If the wrong item arrives I'll be incredibly annoyed, messed me about already this week.\n[AmazonHelp] @737053 Oh, no! We'd like to discuss this with you via phone or chat to get to the bottom of this. Please reach out to us here: https://t.co/JzP7hlA23B. ^DG
```

- **Proposed Intent**: WrongItem
- **Proposed Confidence**: MEDIUM
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 4
- **Reasons Flagged**:
  - MEDIUM confidence

---

### G-1168
**Customer Message**: `@601204 @AmazonHelp This is why I don't pre order with them there service is shocking I ordered something for my son's birthday it was in stock yet I never got it took 3 weeks to arrive and when it did it was the wrong item`

**Context**:
```text
[601204] @115830 guys, your customer service is diabolical.\n[AmazonHelp] @601204 Oh no, that doesn't sound good, what happened? ^AS\n[601204] @AmazonHelp You send me this instead of my Xbox https://t.co/mCCqMojSzf
```

- **Proposed Intent**: WrongItem
- **Proposed Confidence**: MEDIUM
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 4
- **Reasons Flagged**:
  - MEDIUM confidence

---

### G-1171
**Customer Message**: `@AmazonHelp This is the current status of a pre order item should have been here Tuesday...., you did this with my Xbox X, what is it with Amazon and pre orders...shocking tbh, and we pay for prime..😳 https://t.co/lj8MB5pzVt`

**Context**:
```text
[526095] Anyone care to have a wild stab in the dark as to who’s 2 days late with a pre order.....go on ....I dare you....😡😡\n[AmazonHelp] @526095 I'm so sorry that your item hasn't arrived! That's not the experience we want for you! What is the current status for this delivery &amp; the original delivery dated given? You can check here: https://t.co/aaDyEz1VgE Keep us posted on this! We want to make sure it arrives!^FR
```

- **Proposed Intent**: OTHER
- **Proposed Confidence**: LOW
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 4
- **Reasons Flagged**:
  - LOW confidence
  - OTHER where the message appears to contain an actual support issue

---

### G-1173
**Customer Message**: `@AmazonHelp It’s a shame this is happening to a senior citizen who was given these gifts from family. Next time we will not purchase your gift cards.`

**Context**:
```text
[393949] @115821 my aunts account was hacked &amp; her gift card credits stolen. No satisfaction from customer service.\n[AmazonHelp] @393949 Sorry to hear this happened to your aunt, Paige. What options where provided she contacted us? Happy to help further. ^BT\n[393949] @AmazonHelp She was told to contact the IT dept, but then they sent her back to customer service. She lost $300 in amazon gift cards credit.\n[AmazonHelp] @393949 Has your aunt received any e-mail correspondence from one of our Account Specialists? Let us know. ^JS\n[393949] @AmazonHelp This has been ongoing since June. Last contact was 10/22 with account specialists. Just getting the run around. Very disheartening\n[AmazonHelp] @393949 I'm terribly sorry for the trouble, Paige. For the best resolution, please respond to the e-mail with the requested info. ^FD
```

- **Proposed Intent**: OTHER
- **Proposed Confidence**: LOW
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 4
- **Reasons Flagged**:
  - LOW confidence
  - OTHER where the message appears to contain an actual support issue

---

### G-1177
**Customer Message**: `@AmazonHelp Thank you for your help. I contacted the customer service and was told that the payment was not processed yet due to which the order wasn't dispatched.`

**Context**:
```text
[229455] Hey @AmazonHelp, my order was supposed to be delivered today as One-day delivery, but it hasn't even been dispatched yet! Please assist.\n[AmazonHelp] @229455 I'm sorry for the inconvenience, please contact us here https://t.co/vlvfJr4nN9, our support team would assist you accordingly. ^MD\n[229455] @AmazonHelp Have done that already, but no response. Just started with #AmazonPrime and it doesn't look good.\n[AmazonHelp] @229455 Just to check, could you confirm whether you have an account with https://t.co/nUUp5MLhYl or Amazon.in? ^MD\n[229455] @AmazonHelp I have an account with both https://t.co/jHgynw6B5Y and Amazon.in. The order that I am talking about is placed on https://t.co/jHgynw6B5Y\n[229455] @AmazonHelp I have DM'd the order number to you already.\n[AmazonHelp] @229455 We don't have access to account information via Twitter. It's not uncommon for items to be dispatched and delivered the same day. If your order doesn't arrive by 21:00, please reach out to us here: https://t.co/JzP7hlA23B ^VS
```

- **Proposed Intent**: OTHER
- **Proposed Confidence**: MEDIUM
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 4
- **Reasons Flagged**:
  - MEDIUM confidence
  - OTHER where the message appears to contain an actual support issue

---

### G-1178
**Customer Message**: `@AmazonHelp My apologies it was not USPS it was lasership!!`

**Context**:
```text
[412746] @AmazonHelp what is happening to amazin guaranteed delivery?!!! Second time this month my order is delayed?!!! Get the USPS up the speed!!!\n[AmazonHelp] @412746 I'm so sorry for the delay! What's the current tracking and new delivery date shown here: https://t.co/Y5jpI9gRhE? ^AG
```

- **Proposed Intent**: OTHER
- **Proposed Confidence**: LOW
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 4
- **Reasons Flagged**:
  - LOW confidence
  - OTHER where the message appears to contain an actual support issue

---

### G-1180
**Customer Message**: `@AmazonHelp De Volta Para o Futuro!`

**Context**:
```text
[144616] E hoje chegou a caixa da @117086 com meus pedidos feitos na quinta passada! Tudo excelente e muito bem embalado Eficiência é isso aí!\n[AmazonHelp] @144616 Olá, Cacio! Agradecemos seus comentários. Me diga, quais produtos você comprou?. 🤔📦 ^NB\n[144616] @AmazonHelp Comprei algumas HQs: Batman Ano Zero, duas edições do Tio Patinhas da coleção do Don Rosa e a primeira edição recente em quadrinhos de De Volta Para O Futuro\n[AmazonHelp] @144616 Escolha maravilhosa! 🤗 Qual delas vai ler primeiro? ^AZ
```

- **Proposed Intent**: OTHER
- **Proposed Confidence**: LOW
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 4
- **Reasons Flagged**:
  - LOW confidence
  - OTHER where the message appears to contain an actual support issue

---

### G-1183
**Customer Message**: `@AmazonHelp If you know  product I bought is good is market as performance n quality and it's I just purchased out product n don't have value in market`

**Context**:
```text
[431099] @115821 my no.  9659519713 n email address kangsabanikbalram9@gmail.... kindly check my account details..and Give me solution ...shit websit\n[AmazonHelp] @431099 We do not have access to your account on social media. Please tell us what went wrong, we'd like to help you. (1/2)^BS\n[431099] @AmazonHelp Hi, This is the worst ever website for shopping ....I bought OnePlus 5 which cost approx 27000 with exchange on phone .\n[AmazonHelp] @431099 I get your disappointment. The buyback promotion is from our partners, the exchange price keeps fluctuating. (1/2)^BS
```

- **Proposed Intent**: OTHER
- **Proposed Confidence**: LOW
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 4
- **Reasons Flagged**:
  - LOW confidence
  - OTHER where the message appears to contain an actual support issue

---

### G-1185
**Customer Message**: `@AmazonHelp Promised email with new codes and now being told there’s nothing you can do other than a refund.`

**Context**:
```text
[115830] What’s your favourite time of year? ❄️ #TheOneToWatch https://t.co/uTOT8O9eTr https://t.co/NZE01NtoCh\n[255992] @115830 My favourite time is when I can get 2 parcels from the locker - delivered Thu and access codes still don’t work and no new ones given. ;o(\n[AmazonHelp] @255992 Hi, we completely understand your frustration with this issue. If you are able to contact us via this link: https://t.co/JzP7hlA23B. We would like to try get to the bottom of this. ^JC.
```

- **Proposed Intent**: RefundsAndReturns
- **Proposed Confidence**: MEDIUM
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 4
- **Reasons Flagged**:
  - MEDIUM confidence

---

### G-1186
**Customer Message**: `@AmazonHelp Thanks, will be returning the devices due to the terrible support.`

**Context**:
```text
[193221] Pretty appauling customer service from @AmazonHelp today, this is after lying to me last week, this close to returning the devices\n[AmazonHelp] @193221 We'd like to help! Without posting account info, can you tell us more about the what happened? ^GR\n[193221] @AmazonHelp How can I return my devices for a refund since your team cannot help me.\n[AmazonHelp] @193221 I'm sorry, we don't have access to accounts via Twitter. You can view return options with us here: https://t.co/6vY5HnbY6I ^KP
```

- **Proposed Intent**: OTHER
- **Proposed Confidence**: MEDIUM
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 4
- **Reasons Flagged**:
  - MEDIUM confidence
  - OTHER where the message appears to contain an actual support issue

---

### G-1187
**Customer Message**: `@AmazonHelp I ordered that product at 15th October for my brother’s Diwali gift u guys ruined it.`

**Context**:
```text
[438502] Fake service didn’t received product and it’s showing delivered @115850 @115851\n[AmazonHelp] @438502 Sorry for the incorrect tracking update. Please contact us here: https://t.co/vlvfJr4nN9 and we'll help you with this. ^SQ
```

- **Proposed Intent**: DamagedOrDefective
- **Proposed Confidence**: MEDIUM
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 4
- **Reasons Flagged**:
  - MEDIUM confidence

---

### G-1188
**Customer Message**: `@AmazonHelp Yeahhh, my package was supposed to come in yesterday but got delayed and the site said it would arrive by 8pm today and it's already 11:00pm =\`

**Context**:
```text
[719308] Ancient proverb: The more time-sensitive your order is, the more likely it is to get messed up, delayed, and not arrive on time. 🤔 @115821 @115817\n[AmazonHelp] @719308 I'm so sorry for any trouble this may have caused! Did we miss the estimated delivery date for an order: https://t.co/Y5jpI9gRhE? ^EB
```

- **Proposed Intent**: DeliveryStatus
- **Proposed Confidence**: MEDIUM
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 4
- **Reasons Flagged**:
  - MEDIUM confidence

---

### G-1192
**Customer Message**: `@AmazonHelp VENDIDO POR AMAZON  Y ENVIADO X AMAZON! https://t.co/iyOmArc06b`

**Context**:
```text
[256153] @116928 Una semana que hice un pedido de un simple vinilo y no me lo envian, no tengo tiempo para esperar en el 2017, cada momento vale, y ese vinilo tiene que llegar a paris para que una amiga me lo pueda traer a argentina, 1 vinilo es, no pedi una pizza en otra galaxia, mal!\n[AmazonHelp] @256153 Hola, Fede. Lamentamos el inconveniente, ¿podrías indicarnos si el producto es vendido y gestionado por Amazon o por un vendedor externo? ^VL
```

- **Proposed Intent**: OTHER
- **Proposed Confidence**: LOW
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 4
- **Reasons Flagged**:
  - LOW confidence
  - OTHER where the message appears to contain an actual support issue

---

### G-1193
**Customer Message**: `@AmazonHelp haha there are a few incorrect things in this documentary. All band names, peoples' names, etc. the Blackhearts documentary.`

**Context**:
```text
[399056] verg vigonus https://t.co/3x7Ed2lsWq\n[399056] @116618 can I be your subtitle consultant, cause DANG\n[AmazonHelp] @399056 Can you tell us what is wrong with the subtitle and link us to the episode? ^AF
```

- **Proposed Intent**: WrongItem
- **Proposed Confidence**: MEDIUM
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 4
- **Reasons Flagged**:
  - MEDIUM confidence

---

### G-1195
**Customer Message**: `@AmazonHelp 24 h review then a refund + £5 credit for my inconvenience. Hopefully sorted by the very helpful Asma on chat. Thanks!`

**Context**:
```text
[512744] Today I opened a very carefully wrapped package from @115830 that contained absolutely nothing... just an empty packet 😞 https://t.co/KYtfGoo3wz\n[AmazonHelp] @512744 Oh no! Sorry for that, Nette! Please contact us here: https://t.co/JzP7hlA23B so we can look into this issue for you! ^AD\n[512744] @AmazonHelp I'm doing online chat with one of your colleagues as we speak... 😏\n[AmazonHelp] @512744 Please keep us posted on the resolution! We want to make sure we take care of the issue! ^AD
```

- **Proposed Intent**: RefundsAndReturns
- **Proposed Confidence**: MEDIUM
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 4
- **Reasons Flagged**:
  - MEDIUM confidence

---

### G-1196
**Customer Message**: `@AmazonHelp Ah, die schaltet die DHL dann erst frei. Würde sich oben besser machen als rechts.

Hm, das könnte einiges erklären. Ich prüfe das.`

**Context**:
```text
[790732] @116316 fragt bei Bestellung ausdr. nach Packstation, verschickt aber mit Hermes. Geht natürlich zurück. Nachsendung: Wieder Packstation, wieder Hermes. Dritter Versuch nun mit Entschuldigungsgutschein: Wieder Packstation, wieder Hermes. @124285 #neverendingcomedy\n[AmazonHelp] @790732 Hier ist es möglich, dass die Packstationsadresse nicht korrekt hinterlegt ist und/oder vom System nicht erkannt wird. Bitte lasse das mal von unseren Kollegen im Kundenservice prüfen: https://t.co/ohyvGrpvrY ^SK\n[790732] @AmazonHelp Drei mal bereits den Kundenservice kontaktiert. Der sieht und bestätigt den Fehler im System, kann aber nichts dran ändern.\n[AmazonHelp] @790732 Hast du die Packstation so hinterlegt, wie es hier erklärt wird? https://t.co/VxRkMn0E28 Liebe Grüße ^TA\n[790732] @AmazonHelp Dort wo alle DHL Packstationen nicht wählbar sind? (Warum?) https://t.co/uqQzcgToij\n[AmazonHelp] @790732 Hast du denn rechts die DHL Postnummer schon eingegeben? Liebe Grüße ^TA
```

- **Proposed Intent**: OTHER
- **Proposed Confidence**: LOW
- **Proposed Resolution Support**: YES
- **Proposed Auto-Handle**: AUTO-HANDLE
- **Proposed Reply Quality**: 4
- **Reasons Flagged**:
  - LOW confidence
  - OTHER where the message appears to contain an actual support issue

---

