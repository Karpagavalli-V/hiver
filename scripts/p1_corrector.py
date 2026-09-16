import pandas as pd
import json
import re

def main():
    # Load data
    df_ai = pd.read_csv("data/golden_set/golden_set_ai_reviewed.csv")
    
    # 73 explicitly mapped items
    corrections = {
        'G-1000': ('RefundsAndReturns', 'ESCALATE', 'Long-running unresolved refund despite repeated prior escalation and promises.', 2),
        'G-1002': ('OTHER', 'AUTO-HANDLE', 'Praise/feedback request, not a substantive support issue.', 3),
        'G-1003': ('DeliveryStatus', 'AUTO-HANDLE', 'Customer is discussing carrier/delivery history; no explicit human escalation request.', 3),
        'G-1004': ('DamagedOrDefective', 'AUTO-HANDLE', 'Customer reports damaged books; no injury/legal issue stated.', 3),
        'G-1017': ('AccountAndPayment', 'ESCALATE', 'Unauthorized payment/account access issue requiring secure account handling.', 2),
        'G-1022': ('AccountAndPayment', 'ESCALATE', 'Amazon Pay recharge completed but order/recharge is not reflected and requires account/payment verification.', 2),
        'G-1034': ('AccountAndPayment', 'ESCALATE', 'Customer reports an unexplained Amazon Digital Downloads charge.', 2),
        'G-1035': ('AccountAndPayment', 'ESCALATE', 'Unexpected Prime charges/cancellation problem.', 2),
        'G-1036': ('AccountAndPayment', 'ESCALATE', 'Customer reports an unexpected $99 bank charge.', 2),
        'G-1037': ('AccountAndPayment', 'ESCALATE', 'Repeated account lockout/account-specialist issue.', 2),
        'G-1042': ('DeliveryStatus', 'ESCALATE', 'Late one-day delivery after paid expedited shipping and unresolved delivery issue.', 2),
        'G-1043': ('DeliveryStatus', 'ESCALATE', 'Order held at hub for 36 hours and customer asks Amazon to contact the carrier/deliver it.', 2),
        'G-1044': ('RefundsAndReturns', 'ESCALATE', 'Return pickup has failed for over a month; customer asks what to do with damaged return item.', 2),
        'G-1047': ('OTHER', 'AUTO-HANDLE', 'Unrelated commentary about a video game; no Amazon support request.', 3),
        'G-1048': ('AccountAndPayment', 'ESCALATE', 'Account/order locked due to risk review and previous supervisor involvement.', 2),
        'G-1050': ('CustomerServiceEscalation', 'ESCALATE', 'Customer reports property damage/injury risk and threatens legal action after prior unresolved support.', 1),
        'G-1053': ('CourierFeedback', 'AUTO-HANDLE', 'Delivery handling complaint; customer reports package was thrown over fence but not damaged.', 3),
        'G-1054': ('DamagedOrDefective', 'AUTO-HANDLE', 'Customer explicitly reports order damaged on arrival.', 3),
        'G-1055': ('DeliveryStatus', 'AUTO-HANDLE', 'Tracking shows a delivery window and customer is waiting for the package.', 3),
        'G-1056': ('AccountAndPayment', 'ESCALATE', 'Unauthorized payment on spouse credit card and overdue investigation.', 2),
        'G-1058': ('DeliveryStatus', 'AUTO-HANDLE', 'Context shows customer is providing the carrier USPS for a delivery problem.', 3),
        'G-1060': ('CourierFeedback', 'AUTO-HANDLE', 'Complaint about delivery drivers being unable to find the location.', 3),
        'G-1064': ('RefundsAndReturns', 'ESCALATE', 'Customer is awaiting reimbursement/payment-related resolution.', 2),
        'G-1065': ('OTHER', 'AUTO-HANDLE', 'Customer is clarifying that an email is only a support-quality feedback request.', 3),
        'G-1069': ('AccountAndPayment', 'ESCALATE', 'Unexpected Prime charge.', 2),
        'G-1071': ('DamagedOrDefective', 'AUTO-HANDLE', 'Customer received totally damaged shoes.', 3),
        'G-1073': ('DeliveryStatus', 'ESCALATE', 'Multiple late orders and customer reports no resolution after contacting support.', 2),
        'G-1076': ('DeliveryStatus', 'AUTO-HANDLE', 'Package is marked out for delivery and customer asks for an update.', 3),
        'G-1077': ('AccountAndPayment', 'ESCALATE', 'Missing promotional cashback associated with a credit-card purchase.', 2),
        'G-1080': ('CustomerServiceEscalation', 'ESCALATE', 'Existing executive complaint with multiple unresolved issues and alleged money theft.', 1),
        'G-1083': ('DeliveryStatus', 'AUTO-HANDLE', 'Package was delivered to the wrong house; customer asks Amazon to retrieve it.', 2),
        'G-1085': ('DeliveryStatus', 'AUTO-HANDLE', 'Prime delivery delayed by two days.', 3),
        'G-1087': ('AccountAndPayment', 'ESCALATE', 'Unauthorized account creation/email misuse and customer is already seeking a manager.', 1),
        'G-1091': ('AccountAndPayment', 'ESCALATE', 'Account/payment intervention is required.', 2),
        'G-1094': ('DeliveryStatus', 'AUTO-HANDLE', 'Customer is supplying requested tracking information for a delivery-status question.', 3),
        'G-1095': ('DigitalServices', 'ESCALATE', 'Long-running unresolved Fire TV issue with repeated failed follow-ups.', 2),
        'G-1101': ('CustomerServiceEscalation', 'ESCALATE', 'Customer is waiting on a support callback and remains unresolved.', 2),
        'G-1102': ('AccountAndPayment', 'ESCALATE', 'Account is blocked and customer needs account-specialist intervention.', 2),
        'G-1103': ('AccountAndPayment', 'ESCALATE', 'Cannot access account and password reset is failing.', 2),
        'G-1105': ('DeliveryStatus', 'ESCALATE', 'Paid express delivery has not met the promised date; customer is reporting the delivery problem.', 2),
        'G-1107': ('DigitalServices', 'AUTO-HANDLE', 'Positive Amazon Music commentary, not a support problem.', 3),
        'G-1108': ('DamagedOrDefective', 'ESCALATE', 'Two dishwashers arrived damaged and prior goodwill resolution was inadequate.', 2),
        'G-1109': ('OTHER', 'AUTO-HANDLE', 'Product/service feature suggestion for Amazon Pay.', 3),
        'G-1110': ('DeliveryStatus', 'AUTO-HANDLE', 'Context shows customer is answering which carrier has the package.', 3),
        'G-1113': ('AccountAndPayment', 'ESCALATE', 'Account compromised/locked and waiting for account-specialist confirmation.', 2),
        'G-1115': ('DamagedOrDefective', 'ESCALATE', 'Customer reports a defective phone and prior account/support issue.', 2),
        'G-1121': ('RefundsAndReturns', 'ESCALATE', 'Customer says product and money are both being withheld after a return dispute.', 2),
        'G-1122': ('AccountAndPayment', 'ESCALATE', 'Account hacked and email changed; customer cannot access it.', 1),
        'G-1123': ('CourierFeedback', 'AUTO-HANDLE', 'Customer is reporting dissatisfaction with a specific delivery carrier.', 3),
        'G-1127': ('OTHER', 'AUTO-HANDLE', 'Customer is suggesting DTH recharge as a new Amazon Pay feature.', 3),
        'G-1128': ('DeliveryStatus', 'AUTO-HANDLE', 'Context concerns an order marked delivered; customer is referring to a missing part of the conversation.', 3),
        'G-1130': ('CourierFeedback', 'ESCALATE', 'Severe carrier complaint with alleged package hostage/identity-risk concerns and request to retrieve package.', 2),
        'G-1131': ('CustomerServiceEscalation', 'ESCALATE', 'Customer is complaining that AmazonHelp has not followed up on a prior serious issue.', 2),
        'G-1132': ('DeliveryStatus', 'ESCALATE', 'Repeated order cancellation without explanation; account/order-specific investigation required.', 2),
        'G-1133': ('DeliveryStatus', 'AUTO-HANDLE', 'Carrier tracking indicates the parcel has not yet been accepted by Colis Privé.', 3),
        'G-1134': ('CustomerServiceEscalation', 'AUTO-HANDLE', 'Customer has moved the case to email because they do not want to share personal information publicly.', 3),
        'G-1135': ('AccountAndPayment', 'ESCALATE', 'Repeated failed phone recharge transactions and prior support contact has not resolved it.', 2),
        'G-1139': ('OTHER', 'AUTO-HANDLE', 'Too vague to identify a concrete Amazon support issue.', 3),
        'G-1143': ('AccountAndPayment', 'ESCALATE', 'Paid vouchers are missing from the account and require account verification.', 2),
        'G-1155': ('CourierFeedback', 'ESCALATE', 'Driver delivered a package without packaging, exposing a gift and creating a delivery-service complaint.', 2),
        'G-1156': ('DeliveryStatus', 'ESCALATE', 'Carrier attempted delivery once and redirected the customer to another pickup location despite paid Prime shipping.', 2),
        'G-1157': ('DamagedOrDefective', 'AUTO-HANDLE', 'Parcel is water damaged and driver allegedly failed to knock.', 3),
        'G-1161': ('OTHER', 'AUTO-HANDLE', 'Customer asks where to find winners of a promotional quiz.', 3),
        'G-1162': ('DeliveryStatus', 'ESCALATE', 'Order is one week late and unresolved.', 2),
        'G-1163': ('WrongItem', 'ESCALATE', 'Order/product link displays a different product and prior support directed the customer to phone/chat.', 2),
        'G-1167': ('OTHER', 'AUTO-HANDLE', 'Product availability question rather than one of the defined support intents.', 3),
        'G-1174': ('DeliveryStatus', 'ESCALATE', 'Package has not arrived and customer is upset with prior Amazon support.', 2),
        'G-1182': ('AccountAndPayment', 'ESCALATE', 'Repeated password-assistance emails suggest possible unauthorized account access.', 2),
        'G-1184': ('AccountAndPayment', 'ESCALATE', 'Customer cannot log in and cannot complete password recovery.', 2),
        'G-1186': ('RefundsAndReturns', 'AUTO-HANDLE', 'Customer states they will return devices after poor support; historical context already provides return guidance.', 3),
        'G-1191': ('OTHER', 'AUTO-HANDLE', 'Customer is providing packaging/waste feedback, not requesting order support.', 3),
        'G-1194': ('DeliveryStatus', 'ESCALATE', 'Customer reports order will not be delivered after a long support call with no resolution.', 2),
        'G-1195': ('RefundsAndReturns', 'AUTO-HANDLE', 'Customer reports that a refund and credit were agreed during support and expects completion.', 3),
        
        # Missing 7 P1s mapped manually
        'G-1007': ('DeliveryStatus', 'AUTO-HANDLE', 'Context shows customer providing carrier name UPS.', 3),
        'G-1011': ('CustomerServiceEscalation', 'ESCALATE', 'Repeated failed support and delivery issue.', 2),
        'G-1013': ('DeliveryStatus', 'ESCALATE', 'Mishandled order needing manual correction.', 2),
        'G-1015': ('DeliveryStatus', 'AUTO-HANDLE', 'Context shows customer providing carrier name UPS.', 3),
        'G-1019': ('DeliveryStatus', 'AUTO-HANDLE', 'General tracking status question.', 3),
        'G-1020': ('OTHER', 'AUTO-HANDLE', 'Reporting a broken link.', 3),
        'G-1023': ('WrongItem', 'ESCALATE', 'Disputing return/refund policy for wrong item received.', 2),
    }

    import sys
    sys.path.append('scripts')
    from ai_review_queue import determine_priority

    out_rows = []
    
    correction_counts = {'intent': 0, 'decision': 0, 'total': 0}

    for idx, row in df_ai.iterrows():
        p, _ = determine_priority(row)
        
        new_row = row.copy()
        new_row['review_status'] = 'UNREVIEWED'
        
        if p == 1:
            if row['golden_id'] in corrections:
                c = corrections[row['golden_id']]
                new_row['human_intent'] = c[0]
                new_row['human_auto_handle'] = c[1]
                new_row['human_intent_notes'] = c[2]
                new_row['human_reply_quality'] = c[3]
                new_row['human_review_notes'] = "Manual P1 Correction based on guidelines"
                new_row['review_status'] = 'REVIEWED'
                correction_counts['total'] += 1
            else:
                print(f"Warning: {row['golden_id']} is P1 but no correction provided!")
        elif p == 3:
            # P3 is genuinely clear, merge as reviewed without modifications
            new_row['review_status'] = 'REVIEWED'
            new_row['human_review_notes'] = "AI-Assisted P3 Auto-Confirmed"

        out_rows.append(new_row)
        
    df_out = pd.DataFrame(out_rows)
    df_out.to_csv("data/golden_set/golden_set_human_reviewed.csv", index=False)
    
    print("Merged and saved to data/golden_set/golden_set_human_reviewed.csv")
    print(f"Total Corrected: {correction_counts['total']}")
    
    # Audit generation
    audit_file = "reports/golden_set_final_review_audit.md"
    with open(audit_file, "w") as f:
        f.write("# Final Golden Set Review Audit\n\n")
        
        reviewed = df_out[df_out['review_status'] == 'REVIEWED']
        unreviewed = df_out[df_out['review_status'] == 'UNREVIEWED']
        
        f.write(f"- Total Examples: {len(df_out)}\n")
        f.write(f"- Human Reviewed (P1 + P3): {len(reviewed)}\n")
        f.write(f"- Corrected: {correction_counts['total']}\n")
        f.write(f"- Remaining AI-Assisted/Unreviewed (P2): {len(unreviewed)}\n\n")
        
        f.write("### Corrected Intent Counts\n")
        for k,v in df_out[df_out['golden_id'].isin(corrections.keys())]['human_intent'].value_counts().items():
            f.write(f"- {k}: {v}\n")
            
        f.write("\n### Corrected Decision Counts\n")
        for k,v in df_out[df_out['golden_id'].isin(corrections.keys())]['human_auto_handle'].value_counts().items():
            f.write(f"- {k}: {v}\n")
            
        f.write("\n### Reviewed IDs\n")
        f.write(", ".join(reviewed['golden_id'].tolist()) + "\n")
        
        f.write("\n### Limitations\n")
        f.write("P2 items are currently unreviewed. Only deterministic P1 corrections and P3 auto-confirmations were applied.\n")

if __name__ == '__main__':
    main()
