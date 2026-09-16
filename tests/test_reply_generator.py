import unittest
from src.generation.reply_generator import ReplyGenerator, MockReplyProvider, LLMReplyProvider

class TestReplyGenerator(unittest.TestCase):
    def setUp(self):
        self.mock_provider = MockReplyProvider()
        self.generator = ReplyGenerator(provider=self.mock_provider)
        
        self.sample_evidence = [
            {
                "root_id": 12345.0,
                "intent": "DeliveryStatus",
                "similarity_score": 0.85,
                "customer_message": "Where is my stuff?",
                "historical_response": "We are sorry for the delay, please DM us."
            }
        ]

    def test_valid_evidence_produces_valid_output(self):
        result = self.generator.generate("Where is my package?", "DeliveryStatus", self.sample_evidence)
        self.assertEqual(result["confidence"], 0.95)
        self.assertIn("[MOCK]", result["reply"])
        self.assertIn(12345.0, result["evidence_used"])
        self.assertEqual(len(result["warnings"]), 0)

    def test_empty_evidence_triggers_fallback(self):
        result = self.generator.generate("Where is my package?", "DeliveryStatus", [])
        self.assertEqual(result["confidence"], 0.0)
        self.assertIn("I apologize", result["reply"])
        self.assertEqual(len(result["evidence_used"]), 0)
        self.assertIn("Insufficient evidence", result["warnings"][0])

    def test_format_evidence_separates_correctly(self):
        formatted = self.generator._format_evidence(self.sample_evidence)
        self.assertIn("Historical Customer Message:\nWhere is my stuff?", formatted)
        self.assertIn("Historical AmazonHelp Response:\nWe are sorry for the delay, please DM us.", formatted)
        self.assertIn("Root ID: 12345.0", formatted)
        self.assertIn("Intent: DeliveryStatus", formatted)
        self.assertIn("Similarity Score: 0.850", formatted)

    def test_llm_provider_in_mock_mode(self):
        llm_provider = LLMReplyProvider(mock_mode=True)
        generator = ReplyGenerator(provider=llm_provider)
        res = generator.generate("Where is my package?", "DeliveryStatus", self.sample_evidence)
        self.assertEqual(res["confidence"], 0.95)
        self.assertIn("[MOCK]", res["reply"])

    def test_schema_is_always_valid(self):
        expected_keys = {"reply", "grounding_summary", "evidence_used", "confidence", "warnings"}
        res1 = self.generator.generate("Where is my package?", "DeliveryStatus", self.sample_evidence)
        res2 = self.generator.generate("Where is my package?", "DeliveryStatus", [])
        
        self.assertTrue(expected_keys.issubset(set(res1.keys())))
        self.assertTrue(expected_keys.issubset(set(res2.keys())))

if __name__ == "__main__":
    unittest.main()
