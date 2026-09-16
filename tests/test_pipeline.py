import unittest
from src.pipeline import SupportPipeline

class TestSupportPipeline(unittest.TestCase):
    def test_pipeline_offline_mode(self):
        pipeline = SupportPipeline(mock_mode=True)
        res = pipeline.process("Where is my package?")
        
        self.assertIn("customer_message", res)
        self.assertIn("intent", res)
        self.assertIn("confidence", res)
        self.assertIn("retrieved_evidence", res)
        self.assertIn("generated_reply", res)
        self.assertIn("decision", res)
        self.assertIn(res["decision"], ["AUTO-HANDLE", "ESCALATE"])
        self.assertTrue(len(res["generated_reply"]) > 0)

    def test_pipeline_empty_message_raises(self):
        pipeline = SupportPipeline(mock_mode=True)
        with self.assertRaises(ValueError):
            pipeline.process("   ")

if __name__ == "__main__":
    unittest.main()
