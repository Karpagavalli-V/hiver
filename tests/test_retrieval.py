import unittest
import pandas as pd
from src.retrieval.historical_retriever import HistoricalRetriever

class TestRetrieval(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.retriever = HistoricalRetriever()

    def test_train_only_index(self):
        train_df = pd.read_csv("data/splits/amazon_train.csv")
        train_roots = set(train_df['root_id'].dropna())
        
        val_df = pd.read_csv("data/splits/amazon_val.csv")
        val_roots = set(val_df['root_id'].dropna())
        
        for row in self.retriever.db:
            self.assertIn(row['root_id'], train_roots)
            self.assertNotIn(row['root_id'], val_roots)

    def test_no_target_conversation_leakage(self):
        if not self.retriever.db:
            self.skipTest("Empty DB")
        
        target = self.retriever.db[0]
        
        results = self.retriever.retrieve(
            query_message=target['text'],
            query_root_id=target['root_id'],
            top_k=5
        )
        
        for res in results:
            self.assertNotEqual(res['root_id'], target['root_id'])

    def test_no_future_message_leakage(self):
        if not self.retriever.db:
            self.skipTest("Empty DB")
            
        target = self.retriever.db[0]
        ts = target['created_at_dt']
        
        results = self.retriever.retrieve(
            query_message=target['text'],
            query_timestamp=ts,
            top_k=5
        )
        
        for res in results:
            self.assertLess(res['timestamp'], ts)

    def test_intent_filtering(self):
        results = self.retriever.retrieve(
            query_message="Where is my package?",
            intent="DeliveryStatus",
            top_k=10
        )
        for res in results:
            self.assertEqual(res['intent'], "DeliveryStatus")

    def test_empty_query(self):
        self.assertEqual(len(self.retriever.retrieve("")), 0)
        self.assertEqual(len(self.retriever.retrieve("   ")), 0)
        self.assertEqual(len(self.retriever.retrieve(None)), 0)

    def test_top_k(self):
        results = self.retriever.retrieve("Hello", top_k=2)
        self.assertLessEqual(len(results), 2)

if __name__ == "__main__":
    unittest.main()
