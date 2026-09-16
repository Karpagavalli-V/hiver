import pandas as pd
import json
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib
from data_utils import build_dataset

def main():
    print("Building training dataset...")
    train_df = build_dataset("data/twcs.csv", "data/splits/amazon_train.csv")
    
    X_msg = train_df['message_only']
    X_ctx = train_df['context_aware']
    y = train_df['label']
    
    print(f"Training on {len(train_df)} weakly labelled examples.")
    
    os.makedirs("models", exist_ok=True)
    
    # 1. Majority Class Baseline
    majority_class = y.value_counts().index[0]
    print(f"Majority Class: {majority_class}")
    with open("models/majority_baseline.json", "w") as f:
        json.dump({"majority_class": majority_class}, f)
        
    # 2. TF-IDF Message Only
    print("Training TF-IDF Message-Only...")
    vec_msg = TfidfVectorizer(max_features=10000, ngram_range=(1,2))
    X_msg_tfidf = vec_msg.fit_transform(X_msg)
    clf_msg = LogisticRegression(max_iter=1000, random_state=42, class_weight='balanced')
    clf_msg.fit(X_msg_tfidf, y)
    
    joblib.dump(vec_msg, "models/vec_msg.joblib")
    joblib.dump(clf_msg, "models/clf_msg.joblib")
    
    # 3. TF-IDF Context Aware
    print("Training TF-IDF Context-Aware...")
    vec_ctx = TfidfVectorizer(max_features=10000, ngram_range=(1,2))
    X_ctx_tfidf = vec_ctx.fit_transform(X_ctx)
    clf_ctx = LogisticRegression(max_iter=1000, random_state=42, class_weight='balanced')
    clf_ctx.fit(X_ctx_tfidf, y)
    
    joblib.dump(vec_ctx, "models/vec_ctx.joblib")
    joblib.dump(clf_ctx, "models/clf_ctx.joblib")
    
    print("Training complete. Models saved to models/")

if __name__ == "__main__":
    main()
