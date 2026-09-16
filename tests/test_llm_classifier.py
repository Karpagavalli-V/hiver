import os
import sys
import json
import unittest
from unittest.mock import patch, MagicMock

# Add src directory to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src', 'classification')))
from llm_classifier import LLMClassifier, IntentResult

class TestLLMClassifier(unittest.TestCase):
    
    def setUp(self):
        # Create a mock taxonomy for testing
        self.test_taxonomy = {
            "version": "test-1.0",
            "intents": [
                {
                    "id": "DeliveryStatus",
                    "description": "Delivery issues",
                    "inclusion_criteria": ["late"],
                    "exclusion_criteria": ["damaged"]
                },
                {
                    "id": "OTHER",
                    "description": "Fallback",
                    "inclusion_criteria": ["thanks"],
                    "exclusion_criteria": []
                }
            ]
        }
        
        with open("test_intents.json", "w") as f:
            json.dump(self.test_taxonomy, f)
            
        os.environ["OPENAI_API_KEY"] = "fake-test-key"
        self.classifier = LLMClassifier(taxonomy_path="test_intents.json", cache_dir="test_cache", mock_mode=False)
        # Manually clear cache for testing
        self.classifier.cache = {}
        
    def tearDown(self):
        if os.path.exists("test_intents.json"):
            os.remove("test_intents.json")
        if os.path.exists("test_cache/llm_cache.json"):
            os.remove("test_cache/llm_cache.json")
        if os.path.exists("test_cache"):
            os.rmdir("test_cache")

    def test_cache_determinism(self):
        key1 = self.classifier._get_cache_key("My package is late.", "Amazon: How can we help?")
        key2 = self.classifier._get_cache_key("My package is late.", "Amazon: How can we help?")
        key3 = self.classifier._get_cache_key("My package is late.", None)
        
        self.assertEqual(key1, key2)
        self.assertNotEqual(key1, key3)
        
    @patch('llm_classifier.OpenAI')
    def test_valid_json_and_intent(self, mock_openai):
        # Mock the OpenAI API response
        mock_client = MagicMock()
        self.classifier.client = mock_client
        
        mock_response = MagicMock()
        mock_response.choices = [
            MagicMock(message=MagicMock(content='{"intent": "DeliveryStatus", "confidence": 0.95, "reason": "Mentions late package."}'))
        ]
        mock_client.chat.completions.create.return_value = mock_response
        
        result = self.classifier.classify("Where is my package?")
        
        self.assertEqual(result.intent, "DeliveryStatus")
        self.assertEqual(result.confidence, 0.95)
        self.assertTrue("late package" in result.reason)
        
    @patch('llm_classifier.OpenAI')
    def test_invalid_intent_fallback(self, mock_openai):
        mock_client = MagicMock()
        self.classifier.client = mock_client
        
        mock_response = MagicMock()
        # Returns an intent NOT in our taxonomy
        mock_response.choices = [
            MagicMock(message=MagicMock(content='{"intent": "FakeIntent", "confidence": 0.5, "reason": "I made this up"}'))
        ]
        mock_client.chat.completions.create.return_value = mock_response
        
        result = self.classifier.classify("Where is my package?")
        
        # Should fallback to OTHER safely
        self.assertEqual(result.intent, "OTHER")
        self.assertTrue("FakeIntent" in result.reason)

    @patch('llm_classifier.OpenAI')
    def test_malformed_json_fallback(self, mock_openai):
        mock_client = MagicMock()
        self.classifier.client = mock_client
        
        mock_response = MagicMock()
        # Returns broken JSON
        mock_response.choices = [
            MagicMock(message=MagicMock(content='{"intent": "DeliveryStatus", "confidence": '))
        ]
        mock_client.chat.completions.create.return_value = mock_response
        
        result = self.classifier.classify("Broken JSON test")
        
        self.assertEqual(result.intent, "OTHER")
        self.assertEqual(result.confidence, 0.0)
        self.assertTrue("Failed to parse" in result.reason)

    def test_mock_mode(self):
        mock_classifier = LLMClassifier(taxonomy_path="test_intents.json", cache_dir="test_cache", mock_mode=True)
        result = mock_classifier.classify("Does not matter")
        self.assertEqual(result.intent, "OTHER")
        self.assertEqual(result.confidence, 1.0)
        self.assertEqual(result.reason, "Mock mode response")

if __name__ == '__main__':
    unittest.main()
