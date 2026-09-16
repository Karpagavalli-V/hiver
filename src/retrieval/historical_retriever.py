import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle
import os
from typing import List, Dict, Optional

class HistoricalRetriever:
    def __init__(self, twcs_path="data/twcs.csv", train_split_path="data/splits/amazon_train.csv", cache_dir="cache"):
        self.twcs_path = twcs_path
        self.train_split_path = train_split_path
        self.cache_dir = cache_dir
        self.vectorizer_path = os.path.join(cache_dir, "tfidf_vectorizer.pkl")
        self.index_path = os.path.join(cache_dir, "tfidf_index.pkl")
        self.db_path = os.path.join(cache_dir, "retrieval_db.pkl")
        
        os.makedirs(cache_dir, exist_ok=True)
        
        if os.path.exists(self.vectorizer_path) and os.path.exists(self.index_path) and os.path.exists(self.db_path):
            self._load_index()
        else:
            self._build_index()

    def _load_index(self):
        with open(self.vectorizer_path, 'rb') as f:
            self.vectorizer = pickle.load(f)
        with open(self.index_path, 'rb') as f:
            self.tfidf_matrix = pickle.load(f)
        with open(self.db_path, 'rb') as f:
            self.db = pickle.load(f)

    def _build_index(self):
        print("Building retrieval index from TRAIN split...")
        twcs_df = pd.read_csv(self.twcs_path)
        train_df = pd.read_csv(self.train_split_path)
        
        # We only want train rows with an intent
        train_df = train_df[train_df['weak_label'].notna() & (train_df['weak_label'] != 'AMBIGUOUS')]
        
        # We'll merge train_df with twcs_df to get the customer message
        merged = pd.merge(train_df, twcs_df[['tweet_id', 'text']], on='tweet_id', how='inner')
        
        # Now find the responses
        # For each customer message, we look for an AmazonHelp tweet where in_response_to_tweet_id == tweet_id
        responses_df = twcs_df[(twcs_df['author_id'] == 'AmazonHelp') & (twcs_df['in_response_to_tweet_id'].notna())].copy()
        responses_df = responses_df[['in_response_to_tweet_id', 'text']].rename(columns={'in_response_to_tweet_id': 'tweet_id', 'text': 'response_text'})
        
        # Drop duplicates just in case there are multiple replies, we take the first
        responses_df = responses_df.drop_duplicates(subset=['tweet_id'])
        
        # Merge to get the response
        final_df = pd.merge(merged, responses_df, on='tweet_id', how='inner')
        
        # Convert created_at to datetime for chronological filtering
        final_df['created_at_dt'] = pd.to_datetime(final_df['created_at'], format='%a %b %d %H:%M:%S +0000 %Y', errors='coerce')
        
        self.db = final_df.to_dict('records')
        
        # Build TF-IDF
        self.vectorizer = TfidfVectorizer(stop_words='english', max_features=10000)
        corpus = [row['text'] for row in self.db]
        self.tfidf_matrix = self.vectorizer.fit_transform(corpus)
        
        # Save cache
        with open(self.vectorizer_path, 'wb') as f:
            pickle.dump(self.vectorizer, f)
        with open(self.index_path, 'wb') as f:
            pickle.dump(self.tfidf_matrix, f)
        with open(self.db_path, 'wb') as f:
            pickle.dump(self.db, f)
            
        print(f"Indexed {len(self.db)} historical conversations.")

    def retrieve(self, query_message: str, intent: Optional[str] = None, top_k: int = 5, query_root_id: Optional[float] = None, query_timestamp: Optional[pd.Timestamp] = None) -> List[Dict]:
        if not query_message or str(query_message).strip() == "":
            return []
            
        query_vec = self.vectorizer.transform([query_message])
        similarities = cosine_similarity(query_vec, self.tfidf_matrix).flatten()
        
        # Sort by similarity descending
        ranked_indices = np.argsort(similarities)[::-1]
        
        results = []
        for idx in ranked_indices:
            score = similarities[idx]
            if score == 0.0:
                continue
                
            record = self.db[idx]
            
            # Filters
            if intent and record['weak_label'] != intent:
                continue
                
            if query_root_id is not None and record['root_id'] == query_root_id:
                continue
                
            if query_timestamp is not None and pd.notna(record['created_at_dt']) and record['created_at_dt'] >= query_timestamp:
                continue
                
            results.append({
                'similarity_score': float(score),
                'customer_message': record['text'],
                'historical_response': record['response_text'],
                'intent': record['weak_label'],
                'root_id': record['root_id'],
                'timestamp': record['created_at_dt']
            })
            
            if len(results) >= top_k:
                break
                
        return results
