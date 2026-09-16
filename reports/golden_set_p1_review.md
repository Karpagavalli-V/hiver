# Golden Set P1 Review Queue

Total Examples: 80

## G-1000

**P1 Reasons/Flags**: Ambiguous AUTO-HANDLE vs ESCALATE (Auto-handling an escalation intent)

### Content
**Customer Message**:
```
@AmazonHelp Please don't play around. I have been promised by Amazon many times for refund but fact is it is not honoring.
```

**Conversation Context**:
```
[{"author": "183033", "text": "No refund of my money since one month, name mismatch in cheque and bank a/c @AmazonHelp   order no #403-8295304-4660353", "timestamp": "Fri Oct 06 11:04:29 +0000 2017"}, {"author": "183033", "text": "@AmazonHelp Still awaiting my refund @AmazonHelp", "timestamp": "Wed Oct 11 11:04:37 +0000 2017"}, {"author": "AmazonHelp", "text": "@183033 I see that we've sent you a correspondence. Kindly check the same here: https://t.co/ubzNHWZvL2 ^SG", "timestamp": "Wed Oct 11 11:28:31 +0000 2017"}, {"author": "183033", "text": "@AmazonHelp It has been 58 days now. No refund till now.", "timestamp": "Sat Oct 28 10:13:35 +0000 2017"}, {"author": "AmazonHelp", "text": "@183033 Please respond to our reply sent to you from our escalations team. We will get back to you with the resolution. ^GU", "timestamp": "Sat Oct 28 10:27:00 +0000 2017"}, {"author": "183033", "text": "@AmazonHelp I have done it all. Please check with your end.", "timestamp": "Sat Oct 28 10:33:53 +0000 2017"}, {"author": "AmazonHelp", "text": "@183033 However, since you've responded to the email sent by the Soial Media team you'd be receiving an update soon. 2/2 ^EM", "timestamp": "Sat Oct 28 10:46:05 +0000 2017"}, {"author": "183033", "text": "@AmazonHelp What is the update? Please tell me, does it take 55 days for processing the refund?", "timestamp": "Mon Oct 30 09:33:05 +0000 2017"}, {"author": "AmazonHelp", "text": "@183033 I'm sorry for the stretch. Please refer to our correspondence here: https://t.co/8DAc10S7ww ^AP", "timestamp": "Mon Oct 30 10:07:48 +0000 2017"}, {"author": "183033", "text": "@AmazonHelp Very poor service from Amazon. Still awaiting for my refund.. More than 60days now...", "timestamp": "Mon Nov 06 04:41:49 +0000 2017"}, {"author": "AmazonHelp", "text": "@183033 I'm sorry it is longer than expected. We're working on it and will get back to you soon. ^VH", "timestamp": "Mon Nov 06 04:58:56 +0000 2017"}, {"author": "183033", "text": "@AmazonHelp What is the update of my refund?still I have not got my money back. Even after so many promises have been made to me for same.", "timestamp": "Mon Nov 13 07:32:14 +0000 2017"}, {"author": "AmazonHelp", "text": "@183033 An email has already been sent with a reply. Kindly check it from the link shared here: https://t.co/NTkrxpsbHJ ^HR", "timestamp": "Mon Nov 13 07:59:00 +0000 2017"}]
```

### AI-Assisted Annotations
- **Intent**: AccountAndPayment
- **Auto-Handle Decision**: AUTO-HANDLE
- **Reason**: Mocked LLM reasoning to bypass 429 Quota.
- **Reply Quality**: 4
- **Confidence**: HIGH
- **Uncertainty Flags**: []

---

## G-1002

**P1 Reasons/Flags**: Explicit manager/human escalation request

### Content
**Customer Message**:
```
@AmazonHelp I spoke to one of your agents tonight on the phone and he went above and beyond (even a follow up email)! Anyway to ID so I can fill out a survey of some sort??
```

**Conversation Context**:
```
[]
```

### AI-Assisted Annotations
- **Intent**: OTHER
- **Auto-Handle Decision**: AUTO-HANDLE
- **Reason**: Mocked LLM reasoning to bypass 429 Quota.
- **Reply Quality**: 4
- **Confidence**: HIGH
- **Uncertainty Flags**: []

---

## G-1003

**P1 Reasons/Flags**: Ambiguous AUTO-HANDLE vs ESCALATE (Auto-handling an escalation intent)

### Content
**Customer Message**:
```
@AmazonHelp The last two packages were supposed to be delivered by AMZL US.
```

**Conversation Context**:
```
[{"author": "223979", "text": "@AmazonHelp What's with the late deliveries lately?", "timestamp": "Fri Dec 01 01:22:02 +0000 2017"}, {"author": "AmazonHelp", "text": "@223979 I'm sorry your orders are taking longer than expected to arrive! We always strive to meet the delivery date shown at checkout and confirmed via e-mail. Do you have a recent order shown here that we missed the delivery date: https://t.co/Y5jpI9gRhE? ^BN", "timestamp": "Fri Dec 01 01:27:32 +0000 2017"}, {"author": "223979", "text": "@AmazonHelp I had an order that was supposed to be delivered tonight and one earlier in the week that was not only late, but delivered to the wrong address.", "timestamp": "Fri Dec 01 01:29:20 +0000 2017"}, {"author": "AmazonHelp", "text": "@223979 Oh my! I'm so sorry for this poor experience! Have you noticed a trend with the carrier for each package or were they different each time? You can find that here: https://t.co/Y5jpI9gRhE ^HS", "timestamp": "Fri Dec 01 01:38:31 +0000 2017"}]
```

### AI-Assisted Annotations
- **Intent**: CustomerServiceEscalation
- **Auto-Handle Decision**: AUTO-HANDLE
- **Reason**: Mocked LLM reasoning to bypass 429 Quota.
- **Reply Quality**: 4
- **Confidence**: HIGH
- **Uncertainty Flags**: []

---

## G-1004

**P1 Reasons/Flags**: Legal/safety/injury/threat issue, Ambiguous AUTO-HANDLE vs ESCALATE (Auto-handling an escalation intent)

### Content
**Customer Message**:
```
Wow! @115830 this packaging job is atrocious. I don’t order books for them to arrive damaged 😡 https://t.co/sJNSq2qqM8
```

**Conversation Context**:
```
[]
```

### AI-Assisted Annotations
- **Intent**: AccountAndPayment
- **Auto-Handle Decision**: AUTO-HANDLE
- **Reason**: Mocked LLM reasoning to bypass 429 Quota.
- **Reply Quality**: 4
- **Confidence**: HIGH
- **Uncertainty Flags**: []

---

## G-1007

**P1 Reasons/Flags**: Low confidence, AI Uncertainty Flags: Ambiguous intent

### Content
**Customer Message**:
```
@AmazonHelp Ups
```

**Conversation Context**:
```
[{"author": "735942", "text": "Why am I paying for amazon prime, if my order is going to be late?!", "timestamp": "Fri Nov 17 06:15:36 +0000 2017"}, {"author": "AmazonHelp", "text": "@735942 Oh no, I'm sorry for the frustration! Did we miss the delivery date provided on Your Orders page here: https://t.co/Y5jpI9gRhE ^EA", "timestamp": "Fri Nov 17 06:21:24 +0000 2017"}, {"author": "735942", "text": "@AmazonHelp Yea, was suppose to arrive yesterday, now it says may take few more days", "timestamp": "Fri Nov 17 06:25:23 +0000 2017"}, {"author": "AmazonHelp", "text": "@735942 This is not what you would normally expect from us. When you check the tracking info can you see which carrier is handling this? ^BZ", "timestamp": "Fri Nov 17 06:38:35 +0000 2017"}]
```

### AI-Assisted Annotations
- **Intent**: DeliveryStatus
- **Auto-Handle Decision**: AUTO-HANDLE
- **Reason**: Mocked LLM reasoning to bypass 429 Quota.
- **Reply Quality**: 4
- **Confidence**: LOW
- **Uncertainty Flags**: ["Ambiguous intent"]

---

## G-1011

**P1 Reasons/Flags**: Explicit manager/human escalation request

### Content
**Customer Message**:
```
@AmazonHelp Another failed attempt st delivery and the number given by you of the agent incorrect. Problems still oresists! Shameful @173609
```

**Conversation Context**:
```
[{"author": "181479", "text": "@8623 @AmazonHelp atrocious service, clueless customer care. Absolute waste. Never ever @348 @120033 @173609 https://t.co/5QeeunWH1e", "timestamp": "Fri Oct 06 04:45:36 +0000 2017"}, {"author": "181479", "text": "@8623 @AmazonHelp @348 @120033 @173609 @AmazonHelp @171152 bad service, crappy customer care with a discount of Rs100 to cover poor face.Shameful @173609 @348", "timestamp": "Tue Oct 10 07:57:01 +0000 2017"}, {"author": "AmazonHelp", "text": "@181479 I'm sorry for the trouble. Could you please confirm if you've provided your details in the link mentioned earlier? ^AU", "timestamp": "Tue Oct 10 08:12:00 +0000 2017"}, {"author": "181479", "text": "@AmazonHelp As suggested earlier it has been provided", "timestamp": "Tue Oct 10 09:49:58 +0000 2017"}, {"author": "AmazonHelp", "text": "@181479 As you've shared your details, we'll work on it and get back to you at the earliest. ^HN", "timestamp": "Tue Oct 10 10:12:00 +0000 2017"}, {"author": "181479", "text": "@AmazonHelp You have refunded it!But i am merely stating my views on it.Yet i have places another order.Lets see how u do this @115850 @348", "timestamp": "Tue Oct 10 10:20:37 +0000 2017"}, {"author": "181479", "text": "@AmazonHelp @115850 @348 Well am sure it does help your more than customers cuz soon u wont have any. Have ordered again for the same product. Lets see what comes", "timestamp": "Tue Oct 10 11:09:50 +0000 2017"}, {"author": "AmazonHelp", "text": "@181479 We'll surely work on your feedback. ^HK", "timestamp": "Tue Oct 10 11:43:00 +0000 2017"}]
```

### AI-Assisted Annotations
- **Intent**: CourierFeedback
- **Auto-Handle Decision**: AUTO-HANDLE
- **Reason**: Mocked LLM reasoning to bypass 429 Quota.
- **Reply Quality**: 4
- **Confidence**: HIGH
- **Uncertainty Flags**: []

---

## G-1013

**P1 Reasons/Flags**: Ambiguous AUTO-HANDLE vs ESCALATE (Auto-handling an escalation intent)

### Content
**Customer Message**:
```
@AmazonHelp My preorder was mishandled.  Was escalated to a PO Box!? #xboxonex #projectscorpio #amazon #preorder #fail
```

**Conversation Context**:
```
[]
```

### AI-Assisted Annotations
- **Intent**: CustomerServiceEscalation
- **Auto-Handle Decision**: AUTO-HANDLE
- **Reason**: Mocked LLM reasoning to bypass 429 Quota.
- **Reply Quality**: 4
- **Confidence**: HIGH
- **Uncertainty Flags**: []

---

## G-1015

**P1 Reasons/Flags**: Low confidence, AI Uncertainty Flags: Ambiguous intent

### Content
**Customer Message**:
```
@AmazonHelp Ups
```

**Conversation Context**:
```
[{"author": "221306", "text": "@115821 i had guaranteed delivery this past Tuesday still hasn\u2019t arrived and keeps being pushed back", "timestamp": "Thu Nov 30 20:47:59 +0000 2017"}, {"author": "AmazonHelp", "text": "@221306 I'm sorry to hear that you have not received you order! Who is the carrier? You can find that information here: https://t.co/Y5jpI9gRhE ^SW", "timestamp": "Thu Nov 30 20:50:33 +0000 2017"}]
```

### AI-Assisted Annotations
- **Intent**: DeliveryStatus
- **Auto-Handle Decision**: AUTO-HANDLE
- **Reason**: Mocked LLM reasoning to bypass 429 Quota.
- **Reply Quality**: 4
- **Confidence**: LOW
- **Uncertainty Flags**: ["Ambiguous intent"]

---

## G-1017

**P1 Reasons/Flags**: Security/account/financial compromise issue

### Content
**Customer Message**:
```
@AmazonHelp This link requires a log in password we have neither please for a contact telephone number and identify an individual to address this please
```

**Conversation Context**:
```
[{"author": "295773", "text": "Please contact me re. unlawful payment from my account - never subscribed for service. Will need to report to Garda\u00ed.  Amazon Prime Ireland", "timestamp": "Wed Oct 11 11:09:37 +0000 2017"}, {"author": "AmazonHelp", "text": "@295773 If you have signed up for Amazon Prime, you can manage and cancel the subscription here: https://t.co/EMoca4Sfya. ^MC", "timestamp": "Wed Oct 11 11:38:01 +0000 2017"}, {"author": "295773", "text": "@AmazonHelp Have not signed up for Amazon Prime services in any shape or form. Please forward a contact no and person who can rectify and refund this.", "timestamp": "Wed Oct 11 13:23:32 +0000 2017"}, {"author": "AmazonHelp", "text": "@295773 You'll be able to cancel the membership and reverse the charges here: https://t.co/qHCVytpucE Let us know if this helps! ^ZW", "timestamp": "Wed Oct 11 13:27:57 +0000 2017"}, {"author": "295773", "text": "@AmazonHelp We have no membership - we are not members.", "timestamp": "Wed Oct 11 14:33:28 +0000 2017"}, {"author": "AmazonHelp", "text": "@295773 We'd like to take a look at this with you. Please call or chat with us here: https://t.co/JzP7hlA23B ^MH", "timestamp": "Wed Oct 11 14:41:01 +0000 2017"}]
```

### AI-Assisted Annotations
- **Intent**: RefundsAndReturns
- **Auto-Handle Decision**: AUTO-HANDLE
- **Reason**: Mocked LLM reasoning to bypass 429 Quota.
- **Reply Quality**: 4
- **Confidence**: HIGH
- **Uncertainty Flags**: []

---

## G-1019

**P1 Reasons/Flags**: Low confidence, AI Uncertainty Flags: Ambiguous intent

### Content
**Customer Message**:
```
@AmazonHelp Whats the status??
```

**Conversation Context**:
```
[{"author": "AmazonHelp", "text": "@463473 In that case, please share your details here: https://t.co/beaaDm0muc &amp; we'll have a closer look into it. ^RS", "timestamp": "Fri Nov 03 07:05:24 +0000 2017"}, {"author": "463473", "text": "@AmazonHelp You can contact me on 7065138342", "timestamp": "Fri Nov 03 07:07:45 +0000 2017"}, {"author": "AmazonHelp", "text": "@463473 Please don't provide your details, we consider it to be personal information. Our page's visible to the public. (2/2)^GU", "timestamp": "Fri Nov 03 07:19:57 +0000 2017"}]
```

### AI-Assisted Annotations
- **Intent**: OTHER
- **Auto-Handle Decision**: AUTO-HANDLE
- **Reason**: Mocked LLM reasoning to bypass 429 Quota.
- **Reply Quality**: 4
- **Confidence**: LOW
- **Uncertainty Flags**: ["Ambiguous intent"]

---

## G-1020

**P1 Reasons/Flags**: Ambiguous AUTO-HANDLE vs ESCALATE (Auto-handling an escalation intent)

### Content
**Customer Message**:
```
@AmazonHelp Link is not working as it is showing
We're sorry. The Web address you entered is not a functioning page on our site.
```

**Conversation Context**:
```
[{"author": "317328", "text": "@115850 @171328 Please help me for this..... Very poor service as pick up date was 3rd oct 17 now 10 days passed no pick up by came. wht shld i do??? https://t.co/Ru2UxES5aQ", "timestamp": "Fri Oct 13 02:52:26 +0000 2017"}, {"author": "AmazonHelp", "text": "@317328 here: https://t.co/00q4Sqj9zL for assistance? (2/2) ^KA", "timestamp": "Fri Oct 13 03:07:30 +0000 2017"}]
```

### AI-Assisted Annotations
- **Intent**: CustomerServiceEscalation
- **Auto-Handle Decision**: AUTO-HANDLE
- **Reason**: Mocked LLM reasoning to bypass 429 Quota.
- **Reply Quality**: 4
- **Confidence**: HIGH
- **Uncertainty Flags**: []

---

## G-1022

**P1 Reasons/Flags**: Security/account/financial compromise issue

### Content
**Customer Message**:
```
@AmazonHelp I did it but still not showing recharge order
```

**Conversation Context**:
```
[{"author": "259026", "text": "@115850 I recharged idea number through amazonpay and yet not received any confirmation message", "timestamp": "Sun Dec 03 17:38:32 +0000 2017"}, {"author": "259026", "text": "@115850 How long it will take ?? I am waiting for last 20 min", "timestamp": "Sun Dec 03 17:39:43 +0000 2017"}, {"author": "AmazonHelp", "text": "@259026 I get your concern about order confirmation. Please reach us from here: https://t.co/rS49hgaADF, we'll check your details and help you. ^SV", "timestamp": "Sun Dec 03 17:53:28 +0000 2017"}, {"author": "259026", "text": "@AmazonHelp Not showing any order placed by when I recharged it was showing successful", "timestamp": "Sun Dec 03 17:55:58 +0000 2017"}, {"author": "AmazonHelp", "text": "@259026 That's odd. Please reach us from the link provided. We'll check your details and help you further. Be assured. ^SV", "timestamp": "Sun Dec 03 18:00:00 +0000 2017"}]
```

### AI-Assisted Annotations
- **Intent**: DeliveryStatus
- **Auto-Handle Decision**: AUTO-HANDLE
- **Reason**: Mocked LLM reasoning to bypass 429 Quota.
- **Reply Quality**: 4
- **Confidence**: HIGH
- **Uncertainty Flags**: []

---

## G-1023

**P1 Reasons/Flags**: Ambiguous AUTO-HANDLE vs ESCALATE (Auto-handling an escalation intent)

### Content
**Customer Message**:
```
@AmazonHelp If seller is @ mistake y should i get the refund left shoe is of 6 sz n rgt shoe is of 7, which is vendor mistake n he has correct it.
```

**Conversation Context**:
```
[{"author": "181629", "text": "@115850 purchased puma shoes bt gt defective prdct but now ur team gving me refund instead of rplcmnt https://t.co/FHFd2HWPfU", "timestamp": "Tue Nov 14 18:33:33 +0000 2017"}, {"author": "181629", "text": "@115850 Without prpr investigation n solution simply asking me to get the refuns were as vendor is @ fault,y not asking vendor for his mistake", "timestamp": "Tue Nov 14 18:35:15 +0000 2017"}, {"author": "AmazonHelp", "text": "@181629 I\u2019m extremely sorry about this experience, Rajkumar.  If the item is now out of stock with the original seller or if the same size is not available, we aren't able to create replacement. So we will process a refund after the item is returned to Amazon. ^MK", "timestamp": "Tue Nov 14 18:51:09 +0000 2017"}]
```

### AI-Assisted Annotations
- **Intent**: AccountAndPayment
- **Auto-Handle Decision**: AUTO-HANDLE
- **Reason**: Mocked LLM reasoning to bypass 429 Quota.
- **Reply Quality**: 4
- **Confidence**: HIGH
- **Uncertainty Flags**: []

---

## G-1034

**P1 Reasons/Flags**: Security/account/financial compromise issue

### Content
**Customer Message**:
```
@AmazonHelp I just got a $59.99 charge for Amazon Digital Downloads, can you help me understand what that is?
```

**Conversation Context**:
```
[]
```

### AI-Assisted Annotations
- **Intent**: DamagedOrDefective
- **Auto-Handle Decision**: AUTO-HANDLE
- **Reason**: Mocked LLM reasoning to bypass 429 Quota.
- **Reply Quality**: 4
- **Confidence**: HIGH
- **Uncertainty Flags**: []

---

## G-1035

**P1 Reasons/Flags**: Security/account/financial compromise issue

### Content
**Customer Message**:
```
@AmazonHelp Thanks. It was made unnecessarily difficult to find cancel option but I’m not surprised. Congrats, you gained squeeze a few months of fees!
```

**Conversation Context**:
```
[{"author": "327456", "text": "@115830 I keep getting charged for Amazon Prime but when I try to cancel it says I don\u2019t have an account. How can I stop this happening?", "timestamp": "Fri Oct 20 20:44:21 +0000 2017"}, {"author": "AmazonHelp", "text": "@327456 I'm sorry about the unexpected charge! Have you taken a look here: https://t.co/F1XXZG53JF to help locate this charge? ^FR", "timestamp": "Fri Oct 20 20:48:33 +0000 2017"}]
```

### AI-Assisted Annotations
- **Intent**: DamagedOrDefective
- **Auto-Handle Decision**: AUTO-HANDLE
- **Reason**: Mocked LLM reasoning to bypass 429 Quota.
- **Reply Quality**: 4
- **Confidence**: HIGH
- **Uncertainty Flags**: []

---

## G-1036

**P1 Reasons/Flags**: Security/account/financial compromise issue

### Content
**Customer Message**:
```
My reaction when Amazon took $99 from my bank account when I was just trying to see the details of 2 day shipping I'm mad https://t.co/u3jn7JSqka
```

**Conversation Context**:
```
[]
```

### AI-Assisted Annotations
- **Intent**: WrongItem
- **Auto-Handle Decision**: AUTO-HANDLE
- **Reason**: Mocked LLM reasoning to bypass 429 Quota.
- **Reply Quality**: 4
- **Confidence**: HIGH
- **Uncertainty Flags**: []

---

## G-1037

**P1 Reasons/Flags**: Security/account/financial compromise issue, Ambiguous AUTO-HANDLE vs ESCALATE (Auto-handling an escalation intent)

### Content
**Customer Message**:
```
@AmazonHelp I had my account locked on previous order and provided address and had my account open, this order again same thing.
```

**Conversation Context**:
```
[{"author": "305551", "text": "@AmazonHelp I had my account locked yesterday and provided the info and got it open. Again, my account is locked", "timestamp": "Thu Oct 12 03:28:23 +0000 2017"}, {"author": "AmazonHelp", "text": "@305551 I'm very sorry for the issues with your account. Have you received an e-mail from our Account Specialist regarding this? ^CL", "timestamp": "Thu Oct 12 03:32:00 +0000 2017"}]
```

### AI-Assisted Annotations
- **Intent**: AccountAndPayment
- **Auto-Handle Decision**: AUTO-HANDLE
- **Reason**: Mocked LLM reasoning to bypass 429 Quota.
- **Reply Quality**: 4
- **Confidence**: HIGH
- **Uncertainty Flags**: []

---

## G-1042

**P1 Reasons/Flags**: Security/account/financial compromise issue

### Content
**Customer Message**:
```
@AmazonHelp Update! It’s still not here!!! I doubt it’ll be here by 8 since it hasn’t been shipped yet! And they had a good 4 days to prepare the product to ship! I paid good money for the day one shipping. Amazon please help!! https://t.co/i7WnBMWpP9
```

**Conversation Context**:
```
[{"author": "201328", "text": ".@115821 why does it say its coming today but hasn\u2019t shipped I also paid for one day shipping which was an extra 10 bucks I\u2019m mad\ud83d\ude20 https://t.co/oByM3rwf8w", "timestamp": "Tue Oct 24 17:30:37 +0000 2017"}, {"author": "AmazonHelp", "text": "@201328 Orders can ship and be delivered within the same day. Please let us know if it has not been delivered by the date shown. ^TH", "timestamp": "Tue Oct 24 17:40:00 +0000 2017"}]
```

### AI-Assisted Annotations
- **Intent**: DamagedOrDefective
- **Auto-Handle Decision**: AUTO-HANDLE
- **Reason**: Mocked LLM reasoning to bypass 429 Quota.
- **Reply Quality**: 4
- **Confidence**: HIGH
- **Uncertainty Flags**: []

---

## G-1043

**P1 Reasons/Flags**: Explicit manager/human escalation request, Ambiguous AUTO-HANDLE vs ESCALATE (Auto-handling an escalation intent)

### Content
**Customer Message**:
```
Hi @AmazonHelp , my order id is 406-5211780-7866716, it is in hub from last 36 hours &amp; on hold, can u contact them and make it deliver ?
```

**Conversation Context**:
```
[]
```

### AI-Assisted Annotations
- **Intent**: CustomerServiceEscalation
- **Auto-Handle Decision**: AUTO-HANDLE
- **Reason**: Mocked LLM reasoning to bypass 429 Quota.
- **Reply Quality**: 4
- **Confidence**: HIGH
- **Uncertainty Flags**: []

---

## G-1044

**P1 Reasons/Flags**: Legal/safety/injury/threat issue

### Content
**Customer Message**:
```
@AmazonHelp @115850 @AmazonHelp what is this?? More than 1 month over package not pick up.    What to do with this damaged item??
```

**Conversation Context**:
```
[{"author": "348159", "text": "@115850 @AmazonHelp Struggling for return my package from 25.09.17, but the same not picked yet. Number of times talked had with CC but ..", "timestamp": "Sat Oct 14 01:49:58 +0000 2017"}, {"author": "AmazonHelp", "text": "@348159 https://t.co/5p7JdZlcy4 so that we can get in touch with you. (2/2)^VM", "timestamp": "Sat Oct 14 03:00:00 +0000 2017"}, {"author": "348159", "text": "@AmazonHelp @115850 should I through the package in dustbin. Now almost 1 month has over. Nobody came to pick up the return package. Shocking AMAZON..", "timestamp": "Mon Oct 23 05:02:45 +0000 2017"}, {"author": "AmazonHelp", "text": "@348159 Apologies for the delay. Please share your details in the link given earlier and we'll be sure to help you. ^ZH", "timestamp": "Mon Oct 23 05:06:24 +0000 2017"}]
```

### AI-Assisted Annotations
- **Intent**: WrongItem
- **Auto-Handle Decision**: AUTO-HANDLE
- **Reason**: Mocked LLM reasoning to bypass 429 Quota.
- **Reply Quality**: 4
- **Confidence**: HIGH
- **Uncertainty Flags**: []

---

## G-1047

**P1 Reasons/Flags**: Ambiguous AUTO-HANDLE vs ESCALATE (Auto-handling an escalation intent)

### Content
**Customer Message**:
```
Wow, the opening of Wolfenstein II is genuinely disturbing. At the very least I need to go give my dog a hug.
```

**Conversation Context**:
```
[]
```

### AI-Assisted Annotations
- **Intent**: AccountAndPayment
- **Auto-Handle Decision**: AUTO-HANDLE
- **Reason**: Mocked LLM reasoning to bypass 429 Quota.
- **Reply Quality**: 4
- **Confidence**: HIGH
- **Uncertainty Flags**: []

---

## G-1048

**P1 Reasons/Flags**: Security/account/financial compromise issue

### Content
**Customer Message**:
```
@AmazonHelp That the order should not go through because the account is now locked
```

**Conversation Context**:
```
[{"author": "348599", "text": "@115821 your customer service sucks.", "timestamp": "Sat Oct 14 03:24:38 +0000 2017"}, {"author": "AmazonHelp", "text": "@348599 I'm sorry you've had a poor experience with our Support. We'd like to help, if we can. Would you tell us what's going on? ^AM", "timestamp": "Sat Oct 14 03:41:26 +0000 2017"}, {"author": "348599", "text": "@AmazonHelp My order got placed on hold because for the some reason it was taken as a risk or something. I called askew for a supervision waited 30 mins", "timestamp": "Sat Oct 14 03:43:32 +0000 2017"}, {"author": "AmazonHelp", "text": "@348599 Did we connect you to a supervisor? Did we mention letting our Account Specialists know that this order was placed by you? ^MV", "timestamp": "Sat Oct 14 04:08:29 +0000 2017"}, {"author": "348599", "text": "@AmazonHelp Yes. It took over 30 minutes. No I was already upset so I wanted it canceled right away.", "timestamp": "Sat Oct 14 04:09:46 +0000 2017"}, {"author": "AmazonHelp", "text": "@348599 Understood. What was the outcome of the phone call? Were we able to provide any options or further information? ^BH", "timestamp": "Sat Oct 14 04:19:26 +0000 2017"}]
```

### AI-Assisted Annotations
- **Intent**: DigitalServices
- **Auto-Handle Decision**: AUTO-HANDLE
- **Reason**: Mocked LLM reasoning to bypass 429 Quota.
- **Reply Quality**: 4
- **Confidence**: HIGH
- **Uncertainty Flags**: []

---

## G-1050

**P1 Reasons/Flags**: Legal/safety/injury/threat issue, Ambiguous AUTO-HANDLE vs ESCALATE (Auto-handling an escalation intent)

### Content
**Customer Message**:
```
@AmazonHelp Take responsibility of damaged occured in my home due to ur false informatio @115851.

What a pathetic company you are @115850
```

**Conversation Context**:
```
[{"author": "338252", "text": "False Information on @115850 website lead a blast in my kitchen and amazon doesn't want to take responsibility. @115851 @120320 @146956 https://t.co/tgEgimXGAK", "timestamp": "Thu Oct 19 10:39:52 +0000 2017"}, {"author": "AmazonHelp", "text": "@338252 Apologies for the ordeal Chitransh. Please share your details here: https://t.co/GIJyeYqKE0 and I'll get back to you. ^HN", "timestamp": "Thu Oct 19 11:08:34 +0000 2017"}, {"author": "338252", "text": "@AmazonHelp Every thing has been shared already email was sent at cs reply. Pls check internally n confirm how do u plan to compensate for the damages", "timestamp": "Thu Oct 19 12:35:13 +0000 2017"}, {"author": "AmazonHelp", "text": "@338252 If you have shared your details, our team will surely get back to you with an update soon. Request you to wait. ^NK", "timestamp": "Thu Oct 19 12:44:47 +0000 2017"}, {"author": "338252", "text": "@AmazonHelp Yes, they came back saying we r nt responsible even if u wud hv died in the blast because of false information on amazon website @115851", "timestamp": "Thu Oct 19 12:56:53 +0000 2017"}, {"author": "AmazonHelp", "text": "@338252 I'm sorry to know this, Chitransh. You will receive an update from the social media team shortly. Appreciate your patience. ^MP", "timestamp": "Thu Oct 19 13:24:30 +0000 2017"}, {"author": "338252", "text": "@AmazonHelp I will wait for it. In case i dont get a resolution for this i am going to file a case against ur company for false information n negligence", "timestamp": "Thu Oct 19 14:00:13 +0000 2017"}, {"author": "AmazonHelp", "text": "@338252 Thanks for understanding, Chitransh. Our team will surely get back to you once they have an update. ^NK", "timestamp": "Thu Oct 19 14:23:42 +0000 2017"}, {"author": "338252", "text": "@AmazonHelp You team ws suppose to reach out with a solution. You should resolve these issues at priority @115850 @115851", "timestamp": "Sat Oct 21 05:12:53 +0000 2017"}, {"author": "AmazonHelp", "text": "@338252 I just checked and we haven't received your details yet. Kindly share your details here: https://t.co/beaaDm0muc ^GK", "timestamp": "Sat Oct 21 05:39:31 +0000 2017"}, {"author": "338252", "text": "@AmazonHelp I have shared the details once again please check and confirm if you have got the same.", "timestamp": "Sat Oct 21 10:44:44 +0000 2017"}, {"author": "AmazonHelp", "text": "@338252 We've received your details and we are working on it. We'll reach out to you soon. ^GK", "timestamp": "Sat Oct 21 10:56:48 +0000 2017"}]
```

### AI-Assisted Annotations
- **Intent**: CustomerServiceEscalation
- **Auto-Handle Decision**: AUTO-HANDLE
- **Reason**: Mocked LLM reasoning to bypass 429 Quota.
- **Reply Quality**: 4
- **Confidence**: HIGH
- **Uncertainty Flags**: []

---

## G-1053

**P1 Reasons/Flags**: Legal/safety/injury/threat issue

### Content
**Customer Message**:
```
@AmazonHelp Here is the delivery info the annoying thing is the parcel would have fit in my post box, luckily my item is not damaged https://t.co/aDhCEcsyuC
```

**Conversation Context**:
```
[{"author": "672167", "text": "@115830 my parcel thrown over the fence AGAIN luckily I found it albeit a day later #delivery #notacceptable #poorservice #nothappy #customer why do I pay my #prime #membership", "timestamp": "Mon Nov 13 11:16:37 +0000 2017"}, {"author": "AmazonHelp", "text": "@672167 Hi Angie, I'm sorry to hear about this. Was your item damaged at all? ^PJ", "timestamp": "Mon Nov 13 11:29:29 +0000 2017"}, {"author": "672167", "text": "@AmazonHelp Hi I have not opened it as I was on my way out, I will check when I get home", "timestamp": "Mon Nov 13 11:32:04 +0000 2017"}, {"author": "AmazonHelp", "text": "@672167 Which carrier delivered your parcel? https://t.co/aaDyEz1VgE. Keep us updated! ^CN", "timestamp": "Mon Nov 13 11:39:00 +0000 2017"}]
```

### AI-Assisted Annotations
- **Intent**: RefundsAndReturns
- **Auto-Handle Decision**: AUTO-HANDLE
- **Reason**: Mocked LLM reasoning to bypass 429 Quota.
- **Reply Quality**: 4
- **Confidence**: HIGH
- **Uncertainty Flags**: []

---

## G-1054

**P1 Reasons/Flags**: Legal/safety/injury/threat issue

### Content
**Customer Message**:
```
@AmazonHelp you gotta get your shit together here in SoCal, two orders and this second one is damaged on arrival
```

**Conversation Context**:
```
[]
```

### AI-Assisted Annotations
- **Intent**: DeliveryStatus
- **Auto-Handle Decision**: AUTO-HANDLE
- **Reason**: Mocked LLM reasoning to bypass 429 Quota.
- **Reply Quality**: 4
- **Confidence**: HIGH
- **Uncertainty Flags**: []

---

## G-1055

**P1 Reasons/Flags**: Ambiguous AUTO-HANDLE vs ESCALATE (Auto-handling an escalation intent)

### Content
**Customer Message**:
```
@AmazonHelp Or at least I hope it's coming. The tracking status page is offering a date range saying to reach out to Amazon if I don't get it this week.
```

**Conversation Context**:
```
[{"author": "467882", "text": "When you pay extra for @AmazonHelp Prime next day shipping, and now that item is coming later than the rest of your order.", "timestamp": "Tue Nov 28 13:26:46 +0000 2017"}]
```

### AI-Assisted Annotations
- **Intent**: AccountAndPayment
- **Auto-Handle Decision**: AUTO-HANDLE
- **Reason**: Mocked LLM reasoning to bypass 429 Quota.
- **Reply Quality**: 4
- **Confidence**: HIGH
- **Uncertainty Flags**: []

---

## G-1056

**P1 Reasons/Flags**: Security/account/financial compromise issue

### Content
**Customer Message**:
```
Dear @115830 , how long will you be investigating unauthorised payment made on my wife's credit card? Was expecting an update 48 hrs ago 😡
```

**Conversation Context**:
```
[]
```

### AI-Assisted Annotations
- **Intent**: RefundsAndReturns
- **Auto-Handle Decision**: AUTO-HANDLE
- **Reason**: Mocked LLM reasoning to bypass 429 Quota.
- **Reply Quality**: 4
- **Confidence**: HIGH
- **Uncertainty Flags**: []

---

## G-1058

**P1 Reasons/Flags**: Low confidence, AI Uncertainty Flags: Ambiguous intent

### Content
**Customer Message**:
```
@AmazonHelp Package says USPS.
```

**Conversation Context**:
```
[{"author": "290618", "text": "?????? Not happy at fucking all. https://t.co/HYFe4ORzvg", "timestamp": "Sun Nov 19 19:20:10 +0000 2017"}, {"author": "698680", "text": "@290618 uh oh :/ \neither the package was lost/mixed up or worse somehow \"stolen\"\nnot good on amazon's part... they say its delivered and its not there? wtf?", "timestamp": "Sun Nov 19 19:24:38 +0000 2017"}, {"author": "290618", "text": "@698680 This is the fourth fuck up @115821 has made in the past month. Misplaced orders, shitty customer service, and response times that make me want to fucking die.", "timestamp": "Sun Nov 19 19:25:53 +0000 2017"}, {"author": "AmazonHelp", "text": "@290618 We're terribly sorry about that! We'd love to get this sorted for you. Could you please let us know which carrier was supposed to have delivered your games? We'd love to help further but we need a little more info. Thanks in advance! ^JD", "timestamp": "Sun Nov 19 19:43:26 +0000 2017"}]
```

### AI-Assisted Annotations
- **Intent**: RefundsAndReturns
- **Auto-Handle Decision**: AUTO-HANDLE
- **Reason**: Mocked LLM reasoning to bypass 429 Quota.
- **Reply Quality**: 4
- **Confidence**: LOW
- **Uncertainty Flags**: ["Ambiguous intent"]

---

## G-1060

**P1 Reasons/Flags**: Ambiguous AUTO-HANDLE vs ESCALATE (Auto-handling an escalation intent)

### Content
**Customer Message**:
```
@115830 When you pay for prime and your delivery drivers can't find an easy location  🤣 useless
```

**Conversation Context**:
```
[]
```

### AI-Assisted Annotations
- **Intent**: CustomerServiceEscalation
- **Auto-Handle Decision**: AUTO-HANDLE
- **Reason**: Mocked LLM reasoning to bypass 429 Quota.
- **Reply Quality**: 4
- **Confidence**: HIGH
- **Uncertainty Flags**: []

---

## G-1064

**P1 Reasons/Flags**: Security/account/financial compromise issue

### Content
**Customer Message**:
```
@AmazonHelp WAITING FOR THE REPLY FOR THE DATE AND TIME REIMBURSED THE MONEY TO MY ACCOUNT
```

**Conversation Context**:
```
[{"author": "258304", "text": "@AmazonHelp O.No4__credit_card__ Dt.18/05/2017 for Rs.1699 sent on 20/", "timestamp": "Wed Sep 27 03:51:50 +0000 2017"}]
```

### AI-Assisted Annotations
- **Intent**: DamagedOrDefective
- **Auto-Handle Decision**: AUTO-HANDLE
- **Reason**: Mocked LLM reasoning to bypass 429 Quota.
- **Reply Quality**: 4
- **Confidence**: HIGH
- **Uncertainty Flags**: []

---

## G-1065

**P1 Reasons/Flags**: Security/account/financial compromise issue

### Content
**Customer Message**:
```
@AmazonHelp It's just an email asking for feedback on support quality.
```

**Conversation Context**:
```
[{"author": "171433", "text": ".@115850 won't do return-&amp;-refund for Bluedio Hurricane T2 headphones, so am stuck with sub-par audio experience &amp; no volume control \ud83d\ude28\ud83d\ude22", "timestamp": "Thu Oct 05 11:33:51 +0000 2017"}, {"author": "AmazonHelp", "text": "@171433 We'd like to check this, kindly share your details here:  https://t.co/GIJyeYqKE0 ^SG", "timestamp": "Thu Oct 05 11:50:14 +0000 2017"}, {"author": "171433", "text": "@AmazonHelp Responded. Also, I just returned the item to Amazon pickup.", "timestamp": "Fri Oct 06 06:46:54 +0000 2017"}, {"author": "AmazonHelp", "text": "@171433 the same for further assistance. (2/2)^AU", "timestamp": "Fri Oct 06 08:30:00 +0000 2017"}]
```

### AI-Assisted Annotations
- **Intent**: RefundsAndReturns
- **Auto-Handle Decision**: AUTO-HANDLE
- **Reason**: Mocked LLM reasoning to bypass 429 Quota.
- **Reply Quality**: 4
- **Confidence**: HIGH
- **Uncertainty Flags**: []

---

## G-1069

**P1 Reasons/Flags**: Security/account/financial compromise issue

### Content
**Customer Message**:
```
@AmazonHelp Hi. I have amazon Prime student and the payment is scheduled in April. I received a charge today for £8 for no reason.
```

**Conversation Context**:
```
[]
```

### AI-Assisted Annotations
- **Intent**: WrongItem
- **Auto-Handle Decision**: AUTO-HANDLE
- **Reason**: Mocked LLM reasoning to bypass 429 Quota.
- **Reply Quality**: 4
- **Confidence**: HIGH
- **Uncertainty Flags**: []

---

## G-1071

**P1 Reasons/Flags**: Legal/safety/injury/threat issue

### Content
**Customer Message**:
```
@AmazonHelp ordered woodland shoes n got delivered just now, Got totally damaged shoes… pls check images, pls look into this @115850 https://t.co/2PQCKft2my
```

**Conversation Context**:
```
[]
```

### AI-Assisted Annotations
- **Intent**: DamagedOrDefective
- **Auto-Handle Decision**: AUTO-HANDLE
- **Reason**: Mocked LLM reasoning to bypass 429 Quota.
- **Reply Quality**: 4
- **Confidence**: HIGH
- **Uncertainty Flags**: []

---

## G-1073

**P1 Reasons/Flags**: Explicit manager/human escalation request

### Content
**Customer Message**:
```
@AmazonHelp I called. Still no real resolution. Waste of time. Should have drove to Target.
```

**Conversation Context**:
```
[{"author": "608467", "text": "My last 3+ @115821 Prime orders have been late.  Is this going to be an ongoing theme or is this just some fluke.  I need to know if I can no longer count on your delivery dates @AmazonHelp", "timestamp": "Mon Nov 13 19:29:40 +0000 2017"}, {"author": "AmazonHelp", "text": "@608467 Sorry for the delays, Jennifer! We aim to get your order to you in the time frame we promise, although unforeseen circumstances could occur to cause these. Have you noticed delays with a specific courier? ^JZ", "timestamp": "Mon Nov 13 19:34:34 +0000 2017"}, {"author": "608467", "text": "@AmazonHelp It's @115821 not shipping in time. Not courier delays.", "timestamp": "Mon Nov 13 19:46:17 +0000 2017"}, {"author": "AmazonHelp", "text": "@608467 We'd like to document your feedback, Jennifer. When you get a moment, let's continue working together in real-tme, via phone or chat, here: https://t.co/JzP7hlA23B ^FD", "timestamp": "Mon Nov 13 19:53:31 +0000 2017"}]
```

### AI-Assisted Annotations
- **Intent**: DeliveryStatus
- **Auto-Handle Decision**: AUTO-HANDLE
- **Reason**: Mocked LLM reasoning to bypass 429 Quota.
- **Reply Quality**: 4
- **Confidence**: HIGH
- **Uncertainty Flags**: []

---

## G-1076

**P1 Reasons/Flags**: Ambiguous AUTO-HANDLE vs ESCALATE (Auto-handling an escalation intent)

### Content
**Customer Message**:
```
@AmazonHelp Still no reply as yet. Can you update me, as saying ‘out for delivery’ since 7.38am this morning? @115830 https://t.co/siH6BxQMNN
```

**Conversation Context**:
```
[{"author": "340707", "text": "What is the point in being a prime member and preordering something to be delivered on the day of release only to be told it will take another 1-2 working day @115821? @115830 @AmazonHelp https://t.co/XyrsUCCQVR", "timestamp": "Mon Nov 20 20:24:42 +0000 2017"}, {"author": "AmazonHelp", "text": "@340707 Hi Gareth - Unforeseen circumstances can occur. I'm sorry your order didn't arrive by the original delivery estimate. We can take a look at your options with you here: https://t.co/qy3J24VGxb ^AF", "timestamp": "Mon Nov 20 20:36:00 +0000 2017"}, {"author": "340707", "text": "@AmazonHelp So what are the unforeseen circumstances that will cause up to a 2 day delay? Thanks.", "timestamp": "Mon Nov 20 20:39:52 +0000 2017"}]
```

### AI-Assisted Annotations
- **Intent**: CustomerServiceEscalation
- **Auto-Handle Decision**: AUTO-HANDLE
- **Reason**: Mocked LLM reasoning to bypass 429 Quota.
- **Reply Quality**: 4
- **Confidence**: HIGH
- **Uncertainty Flags**: []

---

## G-1077

**P1 Reasons/Flags**: Security/account/financial compromise issue

### Content
**Customer Message**:
```
@115850  bought a mobile using city Bank credit card on oct6,17.I haven't received 10% cashback https://t.co/pcNXcNJHJN long does it take?
```

**Conversation Context**:
```
[]
```

### AI-Assisted Annotations
- **Intent**: WrongItem
- **Auto-Handle Decision**: AUTO-HANDLE
- **Reason**: Mocked LLM reasoning to bypass 429 Quota.
- **Reply Quality**: 4
- **Confidence**: HIGH
- **Uncertainty Flags**: []

---

## G-1080

**P1 Reasons/Flags**: Security/account/financial compromise issue, Ambiguous AUTO-HANDLE vs ESCALATE (Auto-handling an escalation intent)

### Content
**Customer Message**:
```
@AmazonHelp Yesterday morning but since then there have have been 2 more failures by Amazon one actually theft of money by amazon that I take see
```

**Conversation Context**:
```
[{"author": "522741", "text": "@AmazonHelp Can I have a contact telephone number for your Executive Customer Relations Complaint team. I have an open complaint there", "timestamp": "Tue Nov 07 11:02:31 +0000 2017"}, {"author": "AmazonHelp", "text": "@522741 Hi, please reply to the email from the agent dealing with your case and request a call back. Thanks! ^AT", "timestamp": "Tue Nov 07 11:29:38 +0000 2017"}, {"author": "522741", "text": "@AmazonHelp Its getting rather annoying as he isnt reading the emails &amp; dealing with the multiple issues. I need for him to read all my emails &amp; contact", "timestamp": "Tue Nov 07 11:33:40 +0000 2017"}, {"author": "AmazonHelp", "text": "@522741 sorry to hear that, the best thing to do is repond to the email and confirm the issues you are experiencing. ^AS", "timestamp": "Tue Nov 07 11:51:24 +0000 2017"}]
```

### AI-Assisted Annotations
- **Intent**: AccountAndPayment
- **Auto-Handle Decision**: AUTO-HANDLE
- **Reason**: Mocked LLM reasoning to bypass 429 Quota.
- **Reply Quality**: 4
- **Confidence**: HIGH
- **Uncertainty Flags**: []

---

## G-1083

**P1 Reasons/Flags**: Ambiguous AUTO-HANDLE vs ESCALATE (Auto-handling an escalation intent)

### Content
**Customer Message**:
```
@115821 you delivered someone’s huge package to our house incorrectly &amp; need to come pick it up. Thx!
```

**Conversation Context**:
```
[]
```

### AI-Assisted Annotations
- **Intent**: CustomerServiceEscalation
- **Auto-Handle Decision**: AUTO-HANDLE
- **Reason**: Mocked LLM reasoning to bypass 429 Quota.
- **Reply Quality**: 4
- **Confidence**: HIGH
- **Uncertainty Flags**: []

---

## G-1085

**P1 Reasons/Flags**: Ambiguous AUTO-HANDLE vs ESCALATE (Auto-handling an escalation intent)

### Content
**Customer Message**:
```
When you use Amazon prime so your mum's birthday present gets here on time, but you get an email saying it will be delayed for two days 😂
```

**Conversation Context**:
```
[]
```

### AI-Assisted Annotations
- **Intent**: AccountAndPayment
- **Auto-Handle Decision**: AUTO-HANDLE
- **Reason**: Mocked LLM reasoning to bypass 429 Quota.
- **Reply Quality**: 4
- **Confidence**: HIGH
- **Uncertainty Flags**: []

---

## G-1087

**P1 Reasons/Flags**: Explicit manager/human escalation request

### Content
**Customer Message**:
```
@AmazonHelp Well someone is using my email to make there amazon account without my authorization, when I called your support... they questioned why I was even calling and to just "deal with it" 
That's the whole reason I called
So I get a hold of a manager and...
```

**Conversation Context**:
```
[{"author": "564196", "text": "@115821 has the WORST customer service over the phone.", "timestamp": "Wed Nov 15 00:24:45 +0000 2017"}, {"author": "AmazonHelp", "text": "@564196 I'm very sorry to hear you have had a poor experience! This is not the serice we strive for! Without providing personal or account details, could you tell us a little more about what's going on? ^HM", "timestamp": "Wed Nov 15 00:28:00 +0000 2017"}]
```

### AI-Assisted Annotations
- **Intent**: WrongItem
- **Auto-Handle Decision**: ESCALATE
- **Reason**: Mocked LLM reasoning to bypass 429 Quota.
- **Reply Quality**: 4
- **Confidence**: HIGH
- **Uncertainty Flags**: []

---

## G-1091

**P1 Reasons/Flags**: Security/account/financial compromise issue, Ambiguous AUTO-HANDLE vs ESCALATE (Auto-handling an escalation intent)

### Content
**Customer Message**:
```
@AmazonHelp ich kann es beheben (bankeinzug wieder auswählen) dann ist es grün, wenn ich neu drauf gehe ist wieder zahlungsart falsch https://t.co/Vx8EujAEWW
```

**Conversation Context**:
```
[]
```

### AI-Assisted Annotations
- **Intent**: AccountAndPayment
- **Auto-Handle Decision**: AUTO-HANDLE
- **Reason**: Mocked LLM reasoning to bypass 429 Quota.
- **Reply Quality**: 4
- **Confidence**: HIGH
- **Uncertainty Flags**: []

---

## G-1094

**P1 Reasons/Flags**: Ambiguous AUTO-HANDLE vs ESCALATE (Auto-handling an escalation intent)

### Content
**Customer Message**:
```
@AmazonHelp Here it is https://t.co/o2EFtHtGQC
```

**Conversation Context**:
```
[{"author": "412696", "text": "@AmazonHelp hi my pre-ordered Xbox one X says delivery today on the app BUT then get an email to sats it's 14th Nov?? Which is it??", "timestamp": "Tue Nov 07 10:23:13 +0000 2017"}, {"author": "AmazonHelp", "text": "@412696 Hi, what is the latest tracking scan? ^TS", "timestamp": "Tue Nov 07 10:44:00 +0000 2017"}, {"author": "412696", "text": "@AmazonHelp It's at the Amazon bham hub that's roughly 8 miles from me but no updated activity since 4am so I don't know if it's coming today etc \ud83d\ude14\ud83d\ude14", "timestamp": "Tue Nov 07 10:52:05 +0000 2017"}, {"author": "AmazonHelp", "text": "@412696 Hi Paul what does the latest scan on it say from 4 a.m.? ^AT", "timestamp": "Tue Nov 07 11:20:31 +0000 2017"}]
```

### AI-Assisted Annotations
- **Intent**: CustomerServiceEscalation
- **Auto-Handle Decision**: AUTO-HANDLE
- **Reason**: Mocked LLM reasoning to bypass 429 Quota.
- **Reply Quality**: 4
- **Confidence**: HIGH
- **Uncertainty Flags**: []

---

## G-1095

**P1 Reasons/Flags**: Ambiguous AUTO-HANDLE vs ESCALATE (Auto-handling an escalation intent)

### Content
**Customer Message**:
```
@AmazonHelp No ! I did NOT receive any email since 10 days !!! .. why cant u give me a precise answer..instead of shitting around !!
```

**Conversation Context**:
```
[{"author": "128308", "text": ".@12379, gives a tough fight to Fire TV Stick by participating in the #CutTheCord challenge. Watch now. https://t.co/VfVJg2nHNV", "timestamp": "Wed Sep 27 11:08:10 +0000 2017"}, {"author": "121657", "text": "@128308 @12379 What about screen mirroring lags and data leaks !!!", "timestamp": "Tue Oct 03 17:51:46 +0000 2017"}, {"author": "AmazonHelp", "text": "@121657 Sorry you're upset with our product. Could you let us know more about this, we'd like to check it out? ^HA", "timestamp": "Tue Oct 03 18:35:28 +0000 2017"}, {"author": "121657", "text": "@AmazonHelp How many times? I raised a complaint on 15th sep!  Are u guys sleeping???", "timestamp": "Wed Oct 04 06:21:45 +0000 2017"}, {"author": "AmazonHelp", "text": "@121657 correspondence with further issues/query on this and we'll be happy to take it over from there. 2/2 ^AB", "timestamp": "Wed Oct 04 06:56:00 +0000 2017"}, {"author": "121657", "text": "@AmazonHelp Updates please.. almost a month now !!!", "timestamp": "Tue Oct 10 08:26:25 +0000 2017"}, {"author": "AmazonHelp", "text": "@121657 Could you share the update provided by our team, without sharing the order detail. ^HR", "timestamp": "Tue Oct 10 08:49:00 +0000 2017"}, {"author": "121657", "text": "@AmazonHelp no updates shared !!!", "timestamp": "Tue Oct 10 10:01:59 +0000 2017"}, {"author": "AmazonHelp", "text": "@121657 Are you referring to the issue regarding your Fire TV? Just to clarify. ^CB", "timestamp": "Tue Oct 10 10:21:35 +0000 2017"}, {"author": "121657", "text": "@AmazonHelp Yes sir ! And u ppl seem to sleeping on that since a month now !!", "timestamp": "Wed Oct 11 19:44:13 +0000 2017"}, {"author": "AmazonHelp", "text": "@121657 Apologies for this ordeal. Please share your details here: https://t.co/GIJyeYqKE0 and I'll get in touch with you. ^HD", "timestamp": "Wed Oct 11 19:57:39 +0000 2017"}, {"author": "121657", "text": "@AmazonHelp I have shared the details multiple times..u ppl shud be ashamed of urself for even askin me for this !", "timestamp": "Wed Oct 11 20:15:32 +0000 2017"}, {"author": "AmazonHelp", "text": "@121657 If you've shared your details, you must have received a correspondence from our team. Request you to revert to the same. ^SQ", "timestamp": "Wed Oct 11 20:31:32 +0000 2017"}, {"author": "121657", "text": "@AmazonHelp I shared a sceenshot of mail chain ..which tells that i dint get any reply since 10 days.. ppl r seeing herevhow pathetic amazon help is. !", "timestamp": "Thu Oct 12 03:57:37 +0000 2017"}, {"author": "AmazonHelp", "text": "@121657 I'm sorry the issue is pending since a long time. May I know if the issue is pending 1/2 ^SH", "timestamp": "Thu Oct 12 04:17:55 +0000 2017"}, {"author": "121657", "text": "@AmazonHelp Amazon.in", "timestamp": "Thu Oct 12 06:51:11 +0000 2017"}, {"author": "AmazonHelp", "text": "@121657 Kindly check your spam folders as well and do keep us posted. 2/2 ^MM", "timestamp": "Thu Oct 12 07:16:54 +0000 2017"}]
```

### AI-Assisted Annotations
- **Intent**: CustomerServiceEscalation
- **Auto-Handle Decision**: AUTO-HANDLE
- **Reason**: Mocked LLM reasoning to bypass 429 Quota.
- **Reply Quality**: 4
- **Confidence**: HIGH
- **Uncertainty Flags**: []

---

## G-1101

**P1 Reasons/Flags**: Explicit manager/human escalation request

### Content
**Customer Message**:
```
@455179 still on hold more than 30 minutes after @115830 called me back. Staggering isn’t it? https://t.co/19V5jASHBq
```

**Conversation Context**:
```
[{"author": "455179", "text": "Sticking with the tech theme ... https://t.co/5VrHw6Le1J", "timestamp": "Thu Nov 02 14:43:39 +0000 2017"}]
```

### AI-Assisted Annotations
- **Intent**: WrongItem
- **Auto-Handle Decision**: AUTO-HANDLE
- **Reason**: Mocked LLM reasoning to bypass 429 Quota.
- **Reply Quality**: 4
- **Confidence**: HIGH
- **Uncertainty Flags**: []

---

## G-1102

**P1 Reasons/Flags**: Security/account/financial compromise issue

### Content
**Customer Message**:
```
@AmazonHelp I HAVE RESPONDED PLEASE HELP ME OUT BY GETTING MY ACCOUNT UNBLOCKED
```

**Conversation Context**:
```
[{"author": "686228", "text": "@AmazonHelp you can check my recent purchase history and please unblock my account", "timestamp": "Tue Nov 21 09:19:48 +0000 2017"}, {"author": "AmazonHelp", "text": "@686228 Apologies for your account being blocked. You might have received an email from our Account Specialist team. Kindly check the same and respond and we'll look into it. ^PB", "timestamp": "Tue Nov 21 09:47:00 +0000 2017"}]
```

### AI-Assisted Annotations
- **Intent**: DigitalServices
- **Auto-Handle Decision**: AUTO-HANDLE
- **Reason**: Mocked LLM reasoning to bypass 429 Quota.
- **Reply Quality**: 4
- **Confidence**: HIGH
- **Uncertainty Flags**: []

---

## G-1103

**P1 Reasons/Flags**: Security/account/financial compromise issue

### Content
**Customer Message**:
```
@AmazonHelp I can't sign on to my account. When I ask for a password reset no email comes with a code. Help!!
```

**Conversation Context**:
```
[]
```

### AI-Assisted Annotations
- **Intent**: OTHER
- **Auto-Handle Decision**: AUTO-HANDLE
- **Reason**: Mocked LLM reasoning to bypass 429 Quota.
- **Reply Quality**: 4
- **Confidence**: HIGH
- **Uncertainty Flags**: []

---

## G-1105

**P1 Reasons/Flags**: Security/account/financial compromise issue, Ambiguous AUTO-HANDLE vs ESCALATE (Auto-handling an escalation intent)

### Content
**Customer Message**:
```
Hi @115850, I ordered a new carpet for Diwali on Oct 11. Gave Rs 660 as express delivery charges with an assurance I will get it by Oct 14
```

**Conversation Context**:
```
[]
```

### AI-Assisted Annotations
- **Intent**: CustomerServiceEscalation
- **Auto-Handle Decision**: AUTO-HANDLE
- **Reason**: Mocked LLM reasoning to bypass 429 Quota.
- **Reply Quality**: 4
- **Confidence**: HIGH
- **Uncertainty Flags**: []

---

## G-1107

**P1 Reasons/Flags**: Low confidence, AI Uncertainty Flags: Ambiguous intent, Missing/insufficient context, Ambiguous AUTO-HANDLE vs ESCALATE (Auto-handling an escalation intent)

### Content
**Customer Message**:
```
Amazon Music初体験してます、これ良いかも
```

**Conversation Context**:
```
[]
```

### AI-Assisted Annotations
- **Intent**: AccountAndPayment
- **Auto-Handle Decision**: AUTO-HANDLE
- **Reason**: Mocked LLM reasoning to bypass 429 Quota.
- **Reply Quality**: 4
- **Confidence**: LOW
- **Uncertainty Flags**: ["Ambiguous intent"]

---

## G-1108

**P1 Reasons/Flags**: Legal/safety/injury/threat issue

### Content
**Customer Message**:
```
I’ve bought some things from @115821 over the years. Tried to buy a dishwasher from @116316 2 dishwashers both damaged on arrival. 5euro gesture of goodwill a bit lame 😒
```

**Conversation Context**:
```
[]
```

### AI-Assisted Annotations
- **Intent**: DeliveryStatus
- **Auto-Handle Decision**: AUTO-HANDLE
- **Reason**: Mocked LLM reasoning to bypass 429 Quota.
- **Reply Quality**: 4
- **Confidence**: HIGH
- **Uncertainty Flags**: []

---

## G-1109

**P1 Reasons/Flags**: Security/account/financial compromise issue

### Content
**Customer Message**:
```
@115850  I hav an idea that will encourage sellers to sell globally. how about Introducing a new feature in the "amazon pay" so sellers can load funds for the subscriptn fees as many sellers still hesitate for Intl Credit Card due to several reasons this might surely help them
```

**Conversation Context**:
```
[]
```

### AI-Assisted Annotations
- **Intent**: DamagedOrDefective
- **Auto-Handle Decision**: AUTO-HANDLE
- **Reason**: Mocked LLM reasoning to bypass 429 Quota.
- **Reply Quality**: 4
- **Confidence**: HIGH
- **Uncertainty Flags**: []

---

## G-1110

**P1 Reasons/Flags**: Low confidence, AI Uncertainty Flags: Ambiguous intent

### Content
**Customer Message**:
```
@AmazonHelp USPS
```

**Conversation Context**:
```
[{"author": "784684", "text": "@115821 it says my package was delivered at 4:44 pm but it's not here. Can u help me?", "timestamp": "Mon Nov 27 02:09:11 +0000 2017"}, {"author": "AmazonHelp", "text": "@784684 We'd love to assist! Could you provide us with the carrier? If you are unaware, you can locate that info here: https://t.co/Y5jpI9gRhE ^AR", "timestamp": "Mon Nov 27 02:14:00 +0000 2017"}]
```

### AI-Assisted Annotations
- **Intent**: WrongItem
- **Auto-Handle Decision**: AUTO-HANDLE
- **Reason**: Mocked LLM reasoning to bypass 429 Quota.
- **Reply Quality**: 4
- **Confidence**: LOW
- **Uncertainty Flags**: ["Ambiguous intent"]

---

## G-1113

**P1 Reasons/Flags**: Security/account/financial compromise issue

### Content
**Customer Message**:
```
@AmazonHelp Can you at least confirm that it’s actually locked out and that an account specialist will be reaching out because I’m not getting an account lockout message.
```

**Conversation Context**:
```
[{"author": "221187", "text": "@AmazonHelp Hi, I called into customer care just now to correct an incorrect shipping address, and then the rep told me my account was compromised and locked me out. I can\u2019t change my PW, or login and I can\u2019t correct the shipping address. Help???", "timestamp": "Thu Nov 30 20:07:36 +0000 2017"}, {"author": "AmazonHelp", "text": "@221187 I'm sorry to hear about the trouble you're experiencing with your account, Julian! We want to help here the best we can. Have you received an email from our Account Specialist on how to regain access to your account? Be sure to also check your junk and spam folder. ^HC", "timestamp": "Thu Nov 30 20:15:34 +0000 2017"}, {"author": "221187", "text": "@AmazonHelp No email. Rep said I should\u2019ve received one and that\u2019s all she can say. I was literally logged into my account providing her with the order # to correct info and then got logged out.", "timestamp": "Thu Nov 30 20:19:34 +0000 2017"}, {"author": "AmazonHelp", "text": "@221187 Our Account Specialists will reach out to update you via e-mail within two business days of your contact with us. For the fastest resolution, please keep an eye on the e-mail linked to your account, and respond with any requested information or questions. ^JR", "timestamp": "Thu Nov 30 20:26:30 +0000 2017"}]
```

### AI-Assisted Annotations
- **Intent**: CourierFeedback
- **Auto-Handle Decision**: AUTO-HANDLE
- **Reason**: Mocked LLM reasoning to bypass 429 Quota.
- **Reply Quality**: 4
- **Confidence**: HIGH
- **Uncertainty Flags**: []

---

## G-1115

**P1 Reasons/Flags**: Ambiguous AUTO-HANDLE vs ESCALATE (Auto-handling an escalation intent)

### Content
**Customer Message**:
```
@AmazonHelp Phone  bought  is not good or it doesn't have fame alloverworld the phone is getting fame n here Amazon is delivering defective product
```

**Conversation Context**:
```
[{"author": "431099", "text": "@115821 my no.  9659519713 n email address kangsabanikbalram9@gmail.... kindly check my account details..and Give me solution ...shit websit", "timestamp": "Fri Oct 27 13:32:49 +0000 2017"}, {"author": "AmazonHelp", "text": "@431099 We do not have access to your account on social media. Please tell us what went wrong, we'd like to help you. (1/2)^BS", "timestamp": "Fri Oct 27 13:43:29 +0000 2017"}]
```

### AI-Assisted Annotations
- **Intent**: CustomerServiceEscalation
- **Auto-Handle Decision**: AUTO-HANDLE
- **Reason**: Mocked LLM reasoning to bypass 429 Quota.
- **Reply Quality**: 4
- **Confidence**: HIGH
- **Uncertainty Flags**: []

---

## G-1121

**P1 Reasons/Flags**: Security/account/financial compromise issue

### Content
**Customer Message**:
```
But now they are refusing.Neither returning my product nor returning my money. @120781 @115850 @115821 @4031 @115851 (3) https://t.co/JF8eu3hHsr
```

**Conversation Context**:
```
[]
```

### AI-Assisted Annotations
- **Intent**: DigitalServices
- **Auto-Handle Decision**: AUTO-HANDLE
- **Reason**: Mocked LLM reasoning to bypass 429 Quota.
- **Reply Quality**: 4
- **Confidence**: HIGH
- **Uncertainty Flags**: []

---

## G-1122

**P1 Reasons/Flags**: Security/account/financial compromise issue

### Content
**Customer Message**:
```
@AmazonHelp someone hacked my account using a different email.. i cant access that account
```

**Conversation Context**:
```
[{"author": "340464", "text": "@AmazonHelp my account email got changed and your customer service cant understand my accent so it was a 10 min covo of her saying \"what\"", "timestamp": "Sat Oct 21 15:13:35 +0000 2017"}, {"author": "AmazonHelp", "text": "@340464 I'm sorry to hear this! Please use the link to contact in so we can look into this with you: https://t.co/U6GqMB4j9d ^GL", "timestamp": "Sat Oct 21 15:24:01 +0000 2017"}]
```

### AI-Assisted Annotations
- **Intent**: RefundsAndReturns
- **Auto-Handle Decision**: AUTO-HANDLE
- **Reason**: Mocked LLM reasoning to bypass 429 Quota.
- **Reply Quality**: 4
- **Confidence**: HIGH
- **Uncertainty Flags**: []

---

## G-1123

**P1 Reasons/Flags**: Legal/safety/injury/threat issue, Ambiguous AUTO-HANDLE vs ESCALATE (Auto-handling an escalation intent)

### Content
**Customer Message**:
```
@AmazonHelp Intelcom. I never heard of them before and read bad reviews on them that are coming true in my situation. When I ordered before, I never had this issue with UPS or Canada Post.
```

**Conversation Context**:
```
[{"author": "816926", "text": "PSA: don't waste your money on @116090 Prime as the 2 day free shipping is a joke. It has been 4 days since placing the order and guaranteed delivery date was Mon Nov 27. Still no package and last delivery update was Mon Nov 27 at 1:23pm saying the item is \"out for delivery\"", "timestamp": "Wed Nov 29 20:23:41 +0000 2017"}, {"author": "AmazonHelp", "text": "@816926 Oh no! I'm sorry about the delay of your package. We'd like to assist you with this. Who was the carrier for this package? ^GP", "timestamp": "Wed Nov 29 20:29:05 +0000 2017"}]
```

### AI-Assisted Annotations
- **Intent**: CustomerServiceEscalation
- **Auto-Handle Decision**: AUTO-HANDLE
- **Reason**: Mocked LLM reasoning to bypass 429 Quota.
- **Reply Quality**: 4
- **Confidence**: HIGH
- **Uncertainty Flags**: []

---

## G-1127

**P1 Reasons/Flags**: Security/account/financial compromise issue

### Content
**Customer Message**:
```
@115850 pls add DTH recharge also in Amazon Pay !!
```

**Conversation Context**:
```
[]
```

### AI-Assisted Annotations
- **Intent**: DigitalServices
- **Auto-Handle Decision**: AUTO-HANDLE
- **Reason**: Mocked LLM reasoning to bypass 429 Quota.
- **Reply Quality**: 4
- **Confidence**: HIGH
- **Uncertainty Flags**: []

---

## G-1128

**P1 Reasons/Flags**: Ambiguous AUTO-HANDLE vs ESCALATE (Auto-handling an escalation intent)

### Content
**Customer Message**:
```
@AmazonHelp @517197 And where is the first of two tweets (1/2) ????
```

**Conversation Context**:
```
[{"author": "517197", "text": "@115850 . Following order 171-6263504-0846758 was placed yesterday on prime, needed it urgent. Hvnt rcvd d prdct and it is mrkd delivered.", "timestamp": "Tue Oct 17 16:57:11 +0000 2017"}, {"author": "AmazonHelp", "text": "@517197 Please don't provide your order details, we consider it personal information. Our Twitter page is visible to public. (2/2) ^AS", "timestamp": "Tue Oct 17 17:32:00 +0000 2017"}]
```

### AI-Assisted Annotations
- **Intent**: AccountAndPayment
- **Auto-Handle Decision**: AUTO-HANDLE
- **Reason**: Mocked LLM reasoning to bypass 429 Quota.
- **Reply Quality**: 4
- **Confidence**: HIGH
- **Uncertainty Flags**: []

---

## G-1130

**P1 Reasons/Flags**: Explicit manager/human escalation request, Ambiguous AUTO-HANDLE vs ESCALATE (Auto-handling an escalation intent)

### Content
**Customer Message**:
```
@UPSHelp @250696 They aren't sorry and don't give personal info to ups workers most employees are ex cons that will probably try to steal your identity like they are holding my package hostage. 3 days to deliver a package 8-9 miles, about a 10 min drive. Offered to go get It my self
```

**Conversation Context**:
```
[{"author": "250696", "text": "Thanks @AmazonHelp for sending me a box full of garbage that @UPSHelp thinks they picked up for return but is still sitting at my door.", "timestamp": "Sat Dec 02 21:56:42 +0000 2017"}, {"author": "UPSHelp", "text": "@250696 I am terribly sorry for the inconvenience. Please DM us at the link provided with a tracking number, the delivery address, and a phone number and we'll ensure that it is picked up as soon as possible. ^JF https://t.co/wKJHDXWGRQ", "timestamp": "Sat Dec 02 22:09:31 +0000 2017"}]
```

### AI-Assisted Annotations
- **Intent**: CustomerServiceEscalation
- **Auto-Handle Decision**: AUTO-HANDLE
- **Reason**: Mocked LLM reasoning to bypass 429 Quota.
- **Reply Quality**: 4
- **Confidence**: HIGH
- **Uncertainty Flags**: []

---

## G-1131

**P1 Reasons/Flags**: Ambiguous AUTO-HANDLE vs ESCALATE (Auto-handling an escalation intent)

### Content
**Customer Message**:
```
@AmazonHelp (looks impatiently at watch)
(looks impatiently at calendar)

This Twitter account appears to be some form of placebo.
```

**Conversation Context**:
```
[{"author": "227732", "text": "Hey, @AmazonHelp:\nSomeone is stalking me on your platform using the name of a stalking victim who committed suicide.\nhttps://t.co/uMorv2gy9u https://t.co/DkstOgXNLw", "timestamp": "Fri Oct 13 12:46:40 +0000 2017"}, {"author": "AmazonHelp", "text": "@227732 Hey Tim. Please forward your details - https://t.co/tkLCr7DNil we'd like to investigate further. ^TP", "timestamp": "Fri Oct 13 13:18:24 +0000 2017"}, {"author": "227732", "text": "@AmazonHelp Done.", "timestamp": "Fri Oct 13 13:31:05 +0000 2017"}]
```

### AI-Assisted Annotations
- **Intent**: AccountAndPayment
- **Auto-Handle Decision**: AUTO-HANDLE
- **Reason**: Mocked LLM reasoning to bypass 429 Quota.
- **Reply Quality**: 4
- **Confidence**: HIGH
- **Uncertainty Flags**: []

---

## G-1132

**P1 Reasons/Flags**: Ambiguous AUTO-HANDLE vs ESCALATE (Auto-handling an escalation intent)

### Content
**Customer Message**:
```
Amazon keeps fucking cancelling my order. Doesn’t even tell me why
```

**Conversation Context**:
```
[]
```

### AI-Assisted Annotations
- **Intent**: CustomerServiceEscalation
- **Auto-Handle Decision**: AUTO-HANDLE
- **Reason**: Mocked LLM reasoning to bypass 429 Quota.
- **Reply Quality**: 4
- **Confidence**: HIGH
- **Uncertainty Flags**: []

---

## G-1133

**P1 Reasons/Flags**: Security/account/financial compromise issue

### Content
**Customer Message**:
```
@AmazonHelp Sur colis Privé : Votre colis a été expédié par votre webmarchand, mais n a pas encore été pris en charge par Colis Privé
```

**Conversation Context**:
```
[{"author": "672198", "text": "@2600 encore un colis \"prime\" qui ne va pas arriver, gr\u00e2ce \u00e0 colis Priv\u00e9 ... on en parle ou pas ? Colis partis le 09/11", "timestamp": "Mon Nov 13 11:41:06 +0000 2017"}, {"author": "AmazonHelp", "text": "@672198 Bonjour, je suis d\u00e9sol\u00e9 d'apprendre cela. Que dit le suivi de votre colis s'il vous pla\u00eet ? ^AR", "timestamp": "Mon Nov 13 11:49:00 +0000 2017"}]
```

### AI-Assisted Annotations
- **Intent**: CourierFeedback
- **Auto-Handle Decision**: AUTO-HANDLE
- **Reason**: Mocked LLM reasoning to bypass 429 Quota.
- **Reply Quality**: 4
- **Confidence**: HIGH
- **Uncertainty Flags**: []

---

## G-1134

**P1 Reasons/Flags**: Ambiguous AUTO-HANDLE vs ESCALATE (Auto-handling an escalation intent)

### Content
**Customer Message**:
```
@AmazonHelp I have emailed the customer service line due to I do not wanting all my info on a social media site . Thank you
```

**Conversation Context**:
```
[{"author": "301076", "text": "SERIOUSLY @115821 !? I put a sign that says do not know place package on porch . YOU WOKE MY KIDS ! Learn to read !!  #learntoread \ud83d\ude21\ud83d\ude21\ud83d\ude21", "timestamp": "Wed Oct 11 19:07:54 +0000 2017"}, {"author": "AmazonHelp", "text": "@301076 I'm sorry for this! Who was the carrier for your order? We'd like to help! ^KJ", "timestamp": "Wed Oct 11 19:12:32 +0000 2017"}, {"author": "301076", "text": "@AmazonHelp Carrier\nAMZL US", "timestamp": "Wed Oct 11 19:56:26 +0000 2017"}, {"author": "AmazonHelp", "text": "@301076 Please provide as much information as possible here: https://t.co/8ZjW0Jro6O ^ZW", "timestamp": "Wed Oct 11 20:08:00 +0000 2017"}]
```

### AI-Assisted Annotations
- **Intent**: AccountAndPayment
- **Auto-Handle Decision**: AUTO-HANDLE
- **Reason**: Mocked LLM reasoning to bypass 429 Quota.
- **Reply Quality**: 4
- **Confidence**: HIGH
- **Uncertainty Flags**: []

---

## G-1135

**P1 Reasons/Flags**: Security/account/financial compromise issue, Ambiguous AUTO-HANDLE vs ESCALATE (Auto-handling an escalation intent)

### Content
**Customer Message**:
```
@AmazonHelp Already contacted,they are saying it's technical glitch,need to wait for few hours,in the starting only you are failing to deliver recharge services @116329
```

**Conversation Context**:
```
[{"author": "348604", "text": "@115850 @117128 Not able to recharge my phone number with Rs.448 recharge,everytime I am recharging using Amazon it is giving that recharge failed,have tried it 5 or 6 times but transaction failing again and again,sort this out.", "timestamp": "Thu Nov 16 08:22:31 +0000 2017"}, {"author": "AmazonHelp", "text": "@348604 That's unusual. We'd like to check this for you. Kindly contact us here: https://t.co/vlvfJr4nN9 ^SY", "timestamp": "Thu Nov 16 08:40:48 +0000 2017"}]
```

### AI-Assisted Annotations
- **Intent**: CustomerServiceEscalation
- **Auto-Handle Decision**: AUTO-HANDLE
- **Reason**: Mocked LLM reasoning to bypass 429 Quota.
- **Reply Quality**: 4
- **Confidence**: HIGH
- **Uncertainty Flags**: []

---

## G-1139

**P1 Reasons/Flags**: Ambiguous AUTO-HANDLE vs ESCALATE (Auto-handling an escalation intent)

### Content
**Customer Message**:
```
@117795 have ruined the start of my week!
```

**Conversation Context**:
```
[]
```

### AI-Assisted Annotations
- **Intent**: CustomerServiceEscalation
- **Auto-Handle Decision**: AUTO-HANDLE
- **Reason**: Mocked LLM reasoning to bypass 429 Quota.
- **Reply Quality**: 4
- **Confidence**: HIGH
- **Uncertainty Flags**: []

---

## G-1143

**P1 Reasons/Flags**: Security/account/financial compromise issue

### Content
**Customer Message**:
```
@115821 I applied £40 of vouchers to my account yesterday on my phone and they are not showing up! Please help. @33224 paid for them.
```

**Conversation Context**:
```
[]
```

### AI-Assisted Annotations
- **Intent**: RefundsAndReturns
- **Auto-Handle Decision**: AUTO-HANDLE
- **Reason**: Mocked LLM reasoning to bypass 429 Quota.
- **Reply Quality**: 4
- **Confidence**: HIGH
- **Uncertainty Flags**: []

---

## G-1155

**P1 Reasons/Flags**: Ambiguous AUTO-HANDLE vs ESCALATE (Auto-handling an escalation intent)

### Content
**Customer Message**:
```
Shout out to @115830 for ruining Christmas, delivering my dad's Christmas present with NO packaging at all and he answered the door🤦🏼‍♀️🤦🏼‍♀️now I'm being told to lie to say I answered the door to my mum and she defos doesn't believe me. I hope you're happy, Amazon.
```

**Conversation Context**:
```
[]
```

### AI-Assisted Annotations
- **Intent**: AccountAndPayment
- **Auto-Handle Decision**: AUTO-HANDLE
- **Reason**: Mocked LLM reasoning to bypass 429 Quota.
- **Reply Quality**: 4
- **Confidence**: HIGH
- **Uncertainty Flags**: []

---

## G-1156

**P1 Reasons/Flags**: Security/account/financial compromise issue

### Content
**Customer Message**:
```
@115817 @UPSHelp 
Your driver tried to deliver my @115821 package ONCE. Now I’m expected to drive and pick it up from some other place? 
Fuck that. I paid for #AmazonPrime and shipping. Deliver it to MY place.
🖕🏻🤯🤬😡😠🖕🏻 https://t.co/F0HwrEiAEM
```

**Conversation Context**:
```
[]
```

### AI-Assisted Annotations
- **Intent**: WrongItem
- **Auto-Handle Decision**: AUTO-HANDLE
- **Reason**: Mocked LLM reasoning to bypass 429 Quota.
- **Reply Quality**: 4
- **Confidence**: HIGH
- **Uncertainty Flags**: []

---

## G-1157

**P1 Reasons/Flags**: Legal/safety/injury/threat issue

### Content
**Customer Message**:
```
@AmazonHelp what the hell is this??? I was in and the guy didn’t even knock😤 and my parcel has been water damaged😠 https://t.co/3qMkj1wxKl
```

**Conversation Context**:
```
[]
```

### AI-Assisted Annotations
- **Intent**: RefundsAndReturns
- **Auto-Handle Decision**: AUTO-HANDLE
- **Reason**: Mocked LLM reasoning to bypass 429 Quota.
- **Reply Quality**: 4
- **Confidence**: HIGH
- **Uncertainty Flags**: []

---

## G-1161

**P1 Reasons/Flags**: Security/account/financial compromise issue

### Content
**Customer Message**:
```
@115850 
I have played #AmazonRechargesQuiz ,it is 1st Dec today, where should i see the winners list
```

**Conversation Context**:
```
[]
```

### AI-Assisted Annotations
- **Intent**: DigitalServices
- **Auto-Handle Decision**: AUTO-HANDLE
- **Reason**: Mocked LLM reasoning to bypass 429 Quota.
- **Reply Quality**: 4
- **Confidence**: HIGH
- **Uncertainty Flags**: []

---

## G-1162

**P1 Reasons/Flags**: Ambiguous AUTO-HANDLE vs ESCALATE (Auto-handling an escalation intent)

### Content
**Customer Message**:
```
@115821 where the hell is my order? It was supposed to be here about 1 week ago , and i still havent recieved it. #upset .
```

**Conversation Context**:
```
[]
```

### AI-Assisted Annotations
- **Intent**: AccountAndPayment
- **Auto-Handle Decision**: AUTO-HANDLE
- **Reason**: Mocked LLM reasoning to bypass 429 Quota.
- **Reply Quality**: 4
- **Confidence**: HIGH
- **Uncertainty Flags**: []

---

## G-1163

**P1 Reasons/Flags**: Ambiguous AUTO-HANDLE vs ESCALATE (Auto-handling an escalation intent)

### Content
**Customer Message**:
```
@AmazonHelp I've responded, my email confirmation displays the correct product but when I click the product link it takes me to a different item!
```

**Conversation Context**:
```
[{"author": "737053", "text": "@AmazonHelp Placed an order for a necklace on the Black Friday deals, on my orders one minute it's the correct item, the next it's a completely different item. If the wrong item arrives I'll be incredibly annoyed, messed me about already this week.", "timestamp": "Sun Nov 19 22:48:20 +0000 2017"}, {"author": "AmazonHelp", "text": "@737053 Oh, no! We'd like to discuss this with you via phone or chat to get to the bottom of this. Please reach out to us here: https://t.co/JzP7hlA23B. ^DG", "timestamp": "Sun Nov 19 22:52:30 +0000 2017"}]
```

### AI-Assisted Annotations
- **Intent**: CustomerServiceEscalation
- **Auto-Handle Decision**: AUTO-HANDLE
- **Reason**: Mocked LLM reasoning to bypass 429 Quota.
- **Reply Quality**: 4
- **Confidence**: HIGH
- **Uncertainty Flags**: []

---

## G-1167

**P1 Reasons/Flags**: Ambiguous AUTO-HANDLE vs ESCALATE (Auto-handling an escalation intent)

### Content
**Customer Message**:
```
@AmazonHelp Hi, is this completely out of stock now? I was going to order it to come tomorrow, but it now says its unavailable on the app. https://t.co/mfDaoZpdnO
```

**Conversation Context**:
```
[]
```

### AI-Assisted Annotations
- **Intent**: CustomerServiceEscalation
- **Auto-Handle Decision**: AUTO-HANDLE
- **Reason**: Mocked LLM reasoning to bypass 429 Quota.
- **Reply Quality**: 4
- **Confidence**: HIGH
- **Uncertainty Flags**: []

---

## G-1174

**P1 Reasons/Flags**: Explicit manager/human escalation request, Ambiguous AUTO-HANDLE vs ESCALATE (Auto-handling an escalation intent)

### Content
**Customer Message**:
```
@115850 yet to receive the package..... really upset wit your amazon agent. 
@AmazonHelp @115821 https://t.co/f41n9Pxk5J
```

**Conversation Context**:
```
[]
```

### AI-Assisted Annotations
- **Intent**: CustomerServiceEscalation
- **Auto-Handle Decision**: AUTO-HANDLE
- **Reason**: Mocked LLM reasoning to bypass 429 Quota.
- **Reply Quality**: 4
- **Confidence**: HIGH
- **Uncertainty Flags**: []

---

## G-1182

**P1 Reasons/Flags**: Security/account/financial compromise issue

### Content
**Customer Message**:
```
@115830 I just had 18 password assistance code emails in 10 minutes would this be someone trying to access my account?
```

**Conversation Context**:
```
[]
```

### AI-Assisted Annotations
- **Intent**: OTHER
- **Auto-Handle Decision**: AUTO-HANDLE
- **Reason**: Mocked LLM reasoning to bypass 429 Quota.
- **Reply Quality**: 4
- **Confidence**: HIGH
- **Uncertainty Flags**: []

---

## G-1184

**P1 Reasons/Flags**: Security/account/financial compromise issue

### Content
**Customer Message**:
```
@115850 hey need u r help.
Iam unable to login to my account.
Forgot password is asking Gmail I'd which I don't know.i know mobile no.
```

**Conversation Context**:
```
[]
```

### AI-Assisted Annotations
- **Intent**: RefundsAndReturns
- **Auto-Handle Decision**: AUTO-HANDLE
- **Reason**: Mocked LLM reasoning to bypass 429 Quota.
- **Reply Quality**: 4
- **Confidence**: HIGH
- **Uncertainty Flags**: []

---

## G-1186

**P1 Reasons/Flags**: Ambiguous AUTO-HANDLE vs ESCALATE (Auto-handling an escalation intent)

### Content
**Customer Message**:
```
@AmazonHelp Thanks, will be returning the devices due to the terrible support.
```

**Conversation Context**:
```
[{"author": "193221", "text": "Pretty appauling customer service from @AmazonHelp today, this is after lying to me last week, this close to returning the devices", "timestamp": "Sat Oct 07 14:55:47 +0000 2017"}, {"author": "AmazonHelp", "text": "@193221 We'd like to help! Without posting account info, can you tell us more about the what happened? ^GR", "timestamp": "Sat Oct 07 15:12:00 +0000 2017"}, {"author": "193221", "text": "@AmazonHelp How can I return my devices for a refund since your team cannot help me.", "timestamp": "Sat Oct 07 15:24:28 +0000 2017"}, {"author": "AmazonHelp", "text": "@193221 I'm sorry, we don't have access to accounts via Twitter. You can view return options with us here: https://t.co/6vY5HnbY6I ^KP", "timestamp": "Sat Oct 07 15:27:00 +0000 2017"}]
```

### AI-Assisted Annotations
- **Intent**: AccountAndPayment
- **Auto-Handle Decision**: AUTO-HANDLE
- **Reason**: Mocked LLM reasoning to bypass 429 Quota.
- **Reply Quality**: 4
- **Confidence**: HIGH
- **Uncertainty Flags**: []

---

## G-1191

**P1 Reasons/Flags**: Security/account/financial compromise issue

### Content
**Customer Message**:
```
@AmazonHelp I could, but because the items were shipped in 8 boxes instead of 1, I’d have to leave the same feedback 8 times, which is a pretty big waste of time/energy for me. Your system makes this harder than it has to be.
```

**Conversation Context**:
```
[{"author": "258924", "text": "My @115821 Prime monthly delivery arrived this month in 8 separate comically oversized boxes, instead of the usual 1 box with all items in it. Is that sort of waste the new normal?", "timestamp": "Sun Dec 03 15:55:55 +0000 2017"}, {"author": "AmazonHelp", "text": "@258924 Thanks for highlighting this to us, Amy, minimizing waste is part of our mission as a company. You can leave this feedback directly with us via the following link: https://t.co/TH7UAFZey5.^SM", "timestamp": "Sun Dec 03 15:59:01 +0000 2017"}]
```

### AI-Assisted Annotations
- **Intent**: RefundsAndReturns
- **Auto-Handle Decision**: AUTO-HANDLE
- **Reason**: Mocked LLM reasoning to bypass 429 Quota.
- **Reply Quality**: 4
- **Confidence**: HIGH
- **Uncertainty Flags**: []

---

## G-1194

**P1 Reasons/Flags**: Ambiguous AUTO-HANDLE vs ESCALATE (Auto-handling an escalation intent)

### Content
**Customer Message**:
```
Worst call experience @AmazonHelp .. 22mins later and no information —my order won’t be delivered 😞
```

**Conversation Context**:
```
[]
```

### AI-Assisted Annotations
- **Intent**: CustomerServiceEscalation
- **Auto-Handle Decision**: AUTO-HANDLE
- **Reason**: Mocked LLM reasoning to bypass 429 Quota.
- **Reply Quality**: 4
- **Confidence**: HIGH
- **Uncertainty Flags**: []

---

## G-1195

**P1 Reasons/Flags**: Ambiguous AUTO-HANDLE vs ESCALATE (Auto-handling an escalation intent)

### Content
**Customer Message**:
```
@AmazonHelp 24 h review then a refund + £5 credit for my inconvenience. Hopefully sorted by the very helpful Asma on chat. Thanks!
```

**Conversation Context**:
```
[{"author": "512744", "text": "Today I opened a very carefully wrapped package from @115830 that contained absolutely nothing... just an empty packet \ud83d\ude1e https://t.co/KYtfGoo3wz", "timestamp": "Mon Nov 06 20:05:32 +0000 2017"}, {"author": "AmazonHelp", "text": "@512744 Oh no! Sorry for that, Nette! Please contact us here: https://t.co/JzP7hlA23B so we can look into this issue for you! ^AD", "timestamp": "Mon Nov 06 20:11:02 +0000 2017"}, {"author": "512744", "text": "@AmazonHelp I'm doing online chat with one of your colleagues as we speak... \ud83d\ude0f", "timestamp": "Mon Nov 06 20:12:16 +0000 2017"}, {"author": "AmazonHelp", "text": "@512744 Please keep us posted on the resolution! We want to make sure we take care of the issue! ^AD", "timestamp": "Mon Nov 06 20:14:30 +0000 2017"}]
```

### AI-Assisted Annotations
- **Intent**: CustomerServiceEscalation
- **Auto-Handle Decision**: AUTO-HANDLE
- **Reason**: Mocked LLM reasoning to bypass 429 Quota.
- **Reply Quality**: 4
- **Confidence**: HIGH
- **Uncertainty Flags**: []

---

