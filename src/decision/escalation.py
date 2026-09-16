import re
from typing import Dict, List, Optional

class EscalationDecisionEngine:
    def __init__(self):
        self.CLASSIFIER_CONFIDENCE_THRESHOLD = 0.70
        self.RETRIEVAL_SCORE_THRESHOLD = 0.65

        # Regex patterns for deterministic risk detection
        self.security_pattern = re.compile(r'\b(hacked|unauthorized|stolen|phishing|takeover)\b', re.IGNORECASE)
        self.finance_pattern = re.compile(r'\b(dispute|chargeback|fraud|bank|credit card|unusual charge)\b', re.IGNORECASE)
        self.legal_safety_pattern = re.compile(r'\b(sue|lawyer|police|threat|attorney|lawsuit)\b', re.IGNORECASE)
        self.unsupported_action_pattern = re.compile(r'\b(cancel my|refund me|refund my|change my|update my|delete my)\b', re.IGNORECASE)
        self.human_pattern = re.compile(r'\b(agent|human|manager|supervisor|speak to someone|real person|representative)\b', re.IGNORECASE)

    def decide(
        self,
        customer_message: str,
        intent: str,
        classifier_confidence: float,
        retrieved_examples: List[Dict],
        generated_reply: Dict,
        context: Optional[str] = None
    ) -> Dict:
        
        risk_flags = []
        msg_text = customer_message.lower()

        # 1. Critical safety/legal/security risk
        if self.security_pattern.search(msg_text):
            risk_flags.append("ACCOUNT_SECURITY")
        if self.finance_pattern.search(msg_text):
            risk_flags.append("FINANCIAL_DISPUTE")
        if self.legal_safety_pattern.search(msg_text):
            risk_flags.append("LEGAL_OR_SAFETY")

        # 2. Unsupported external/account action
        # If the customer asks to DO something (not just how to do it)
        if self.unsupported_action_pattern.search(msg_text):
            risk_flags.append("UNSUPPORTED_ACTION")

        # 3. Explicit human/manager request
        if self.human_pattern.search(msg_text):
            risk_flags.append("HUMAN_REQUEST")

        # 4. Severe unresolved escalation
        if intent == "CustomerServiceEscalation":
            risk_flags.append("REPEATED_ESCALATION")

        # 5. Insufficient/contradictory evidence
        if not retrieved_examples:
            risk_flags.append("NO_RETRIEVAL_EVIDENCE")
        else:
            best_score = max(ex.get("similarity_score", 0.0) for ex in retrieved_examples)
            if best_score < self.RETRIEVAL_SCORE_THRESHOLD:
                risk_flags.append("WEAK_RETRIEVAL")
            
            # Contradictory evidence: if top intents are all different (and there is more than 1 example)
            intents = [ex.get("intent") for ex in retrieved_examples if ex.get("intent")]
            if intents and len(set(intents)) == len(retrieved_examples) and len(retrieved_examples) > 1:
                risk_flags.append("CONTRADICTORY_EVIDENCE")

        # 6. Low classifier confidence
        if classifier_confidence < self.CLASSIFIER_CONFIDENCE_THRESHOLD:
            risk_flags.append("LOW_CLASSIFIER_CONFIDENCE")

        # Decision Precedence
        if risk_flags:
            # Find highest precedence reason
            precedence = [
                "ACCOUNT_SECURITY", "FINANCIAL_DISPUTE", "LEGAL_OR_SAFETY",
                "UNSUPPORTED_ACTION",
                "HUMAN_REQUEST",
                "REPEATED_ESCALATION",
                "NO_RETRIEVAL_EVIDENCE", "CONTRADICTORY_EVIDENCE", "WEAK_RETRIEVAL",
                "LOW_CLASSIFIER_CONFIDENCE"
            ]
            primary_flag = next((f for f in precedence if f in risk_flags), risk_flags[0])
            
            reason_map = {
                "ACCOUNT_SECURITY": "Account security issue detected.",
                "FINANCIAL_DISPUTE": "Financial dispute detected.",
                "LEGAL_OR_SAFETY": "Legal or safety threat detected.",
                "UNSUPPORTED_ACTION": "Customer requested an unsupported account action.",
                "HUMAN_REQUEST": "Customer explicitly requested a human agent.",
                "REPEATED_ESCALATION": "Severe customer service escalation intent detected.",
                "NO_RETRIEVAL_EVIDENCE": "No historical evidence available.",
                "CONTRADICTORY_EVIDENCE": "Retrieved evidence contains contradictory intents.",
                "WEAK_RETRIEVAL": "Retrieved evidence is too weak to confidently auto-handle.",
                "LOW_CLASSIFIER_CONFIDENCE": "Intent classification confidence is below threshold."
            }
            reason = reason_map.get(primary_flag, "Multiple risk factors detected.")
            
            return {
                "decision": "ESCALATE",
                "reason": reason,
                "risk_flags": risk_flags,
                "confidence": 1.0,
                "supporting_evidence": generated_reply.get("evidence_used", [])
            }

        # Otherwise, AUTO-HANDLE
        return {
            "decision": "AUTO-HANDLE",
            "reason": "All safety criteria met. High confidence and strong evidence.",
            "risk_flags": [],
            "confidence": 1.0,
            "supporting_evidence": generated_reply.get("evidence_used", [])
        }
