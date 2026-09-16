import unittest
from src.decision.escalation import EscalationDecisionEngine

class TestEscalationDecisionEngine(unittest.TestCase):
    def setUp(self):
        self.engine = EscalationDecisionEngine()
        self.strong_evidence = [{"intent": "DeliveryStatus", "similarity_score": 0.90, "root_id": 1.0}]
        self.generated_reply = {"reply": "Your order is on the way.", "evidence_used": [1.0]}

    def test_strong_evidence_safe_intent_auto_handle(self):
        res = self.engine.decide(
            customer_message="Where is my package?",
            intent="DeliveryStatus",
            classifier_confidence=0.9,
            retrieved_examples=self.strong_evidence,
            generated_reply=self.generated_reply
        )
        self.assertEqual(res["decision"], "AUTO-HANDLE")
        self.assertEqual(len(res["risk_flags"]), 0)

    def test_no_evidence_escalate(self):
        res = self.engine.decide(
            customer_message="Where is my package?",
            intent="DeliveryStatus",
            classifier_confidence=0.9,
            retrieved_examples=[],
            generated_reply=self.generated_reply
        )
        self.assertEqual(res["decision"], "ESCALATE")
        self.assertIn("NO_RETRIEVAL_EVIDENCE", res["risk_flags"])

    def test_low_confidence_escalate(self):
        res = self.engine.decide(
            customer_message="Where is my package?",
            intent="DeliveryStatus",
            classifier_confidence=0.6,
            retrieved_examples=self.strong_evidence,
            generated_reply=self.generated_reply
        )
        self.assertEqual(res["decision"], "ESCALATE")
        self.assertIn("LOW_CLASSIFIER_CONFIDENCE", res["risk_flags"])

    def test_explicit_human_request_escalate(self):
        res = self.engine.decide(
            customer_message="I want to speak to a manager",
            intent="DeliveryStatus",
            classifier_confidence=0.9,
            retrieved_examples=self.strong_evidence,
            generated_reply=self.generated_reply
        )
        self.assertEqual(res["decision"], "ESCALATE")
        self.assertIn("HUMAN_REQUEST", res["risk_flags"])

    def test_account_security_escalate(self):
        res = self.engine.decide(
            customer_message="My account is hacked",
            intent="AccountAndPayment",
            classifier_confidence=0.9,
            retrieved_examples=self.strong_evidence,
            generated_reply=self.generated_reply
        )
        self.assertEqual(res["decision"], "ESCALATE")
        self.assertIn("ACCOUNT_SECURITY", res["risk_flags"])

    def test_financial_dispute_escalate(self):
        res = self.engine.decide(
            customer_message="I want to dispute this charge",
            intent="AccountAndPayment",
            classifier_confidence=0.9,
            retrieved_examples=self.strong_evidence,
            generated_reply=self.generated_reply
        )
        self.assertEqual(res["decision"], "ESCALATE")
        self.assertIn("FINANCIAL_DISPUTE", res["risk_flags"])

    def test_legal_safety_escalate(self):
        res = self.engine.decide(
            customer_message="I will sue you",
            intent="OTHER",
            classifier_confidence=0.9,
            retrieved_examples=self.strong_evidence,
            generated_reply=self.generated_reply
        )
        self.assertEqual(res["decision"], "ESCALATE")
        self.assertIn("LEGAL_OR_SAFETY", res["risk_flags"])

    def test_unsupported_action_escalate(self):
        res = self.engine.decide(
            customer_message="Please cancel my order",
            intent="RefundsAndReturns",
            classifier_confidence=0.9,
            retrieved_examples=self.strong_evidence,
            generated_reply=self.generated_reply
        )
        self.assertEqual(res["decision"], "ESCALATE")
        self.assertIn("UNSUPPORTED_ACTION", res["risk_flags"])

    def test_repeated_escalation_escalate(self):
        res = self.engine.decide(
            customer_message="This is ridiculous",
            intent="CustomerServiceEscalation",
            classifier_confidence=0.9,
            retrieved_examples=self.strong_evidence,
            generated_reply=self.generated_reply
        )
        self.assertEqual(res["decision"], "ESCALATE")
        self.assertIn("REPEATED_ESCALATION", res["risk_flags"])

    def test_strong_informational_question_auto_handle(self):
        res = self.engine.decide(
            customer_message="How do I return my order?",
            intent="RefundsAndReturns",
            classifier_confidence=0.9,
            retrieved_examples=self.strong_evidence,
            generated_reply=self.generated_reply
        )
        self.assertEqual(res["decision"], "AUTO-HANDLE")
        self.assertEqual(len(res["risk_flags"]), 0)

    def test_contradictory_evidence_escalate(self):
        contradictory_evidence = [
            {"intent": "DeliveryStatus", "similarity_score": 0.90, "root_id": 1.0},
            {"intent": "RefundsAndReturns", "similarity_score": 0.88, "root_id": 2.0}
        ]
        res = self.engine.decide(
            customer_message="Where is my package?",
            intent="DeliveryStatus",
            classifier_confidence=0.9,
            retrieved_examples=contradictory_evidence,
            generated_reply=self.generated_reply
        )
        self.assertEqual(res["decision"], "ESCALATE")
        self.assertIn("CONTRADICTORY_EVIDENCE", res["risk_flags"])

    def test_output_schema_valid(self):
        res = self.engine.decide(
            customer_message="Where is my package?",
            intent="DeliveryStatus",
            classifier_confidence=0.9,
            retrieved_examples=self.strong_evidence,
            generated_reply=self.generated_reply
        )
        self.assertIn("decision", res)
        self.assertIn("reason", res)
        self.assertIn("risk_flags", res)
        self.assertIn("confidence", res)
        self.assertIn("supporting_evidence", res)

    def test_multiple_risk_flags_attached(self):
        res = self.engine.decide(
            customer_message="I want to sue you because my account was hacked and you won't refund me",
            intent="AccountAndPayment",
            classifier_confidence=0.9,
            retrieved_examples=self.strong_evidence,
            generated_reply=self.generated_reply
        )
        self.assertIn("LEGAL_OR_SAFETY", res["risk_flags"])
        self.assertIn("ACCOUNT_SECURITY", res["risk_flags"])
        self.assertIn("UNSUPPORTED_ACTION", res["risk_flags"])

    def test_decision_precedence_respected(self):
        res = self.engine.decide(
            customer_message="I want to sue you, human agent now", 
            intent="AccountAndPayment",
            classifier_confidence=0.9,
            retrieved_examples=self.strong_evidence,
            generated_reply=self.generated_reply
        )
        self.assertEqual(res["decision"], "ESCALATE")
        self.assertEqual(res["reason"], "Legal or safety threat detected.")

if __name__ == "__main__":
    unittest.main()
