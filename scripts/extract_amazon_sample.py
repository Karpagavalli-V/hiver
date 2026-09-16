import pandas as pd
import re
from collections import Counter

def get_ngrams(text, n=2):
    words = re.findall(r'\b[a-z]{3,}\b', text.lower())
    # remove some common stop words
    stop_words = {'the', 'and', 'for', 'you', 'this', 'that', 'with', 'are', 'not', 'have', 'but', 'from', 'was', 'your', 'my', 'can', 'amazon', 'amazonhelp', 'http', 'https', 'com'}
    words = [w for w in words if w not in stop_words]
    return [' '.join(words[i:i+n]) for i in range(len(words)-n+1)]

def main():
    print("Loading dataset...")
    df = pd.read_csv("data/twcs.csv")
    
    print("Isolating AmazonHelp conversations...")
    parent_map = dict(zip(df['tweet_id'], df['in_response_to_tweet_id']))
    roots = {}
    for t_id in df['tweet_id']:
        curr = t_id
        path = []
        while pd.notna(curr) and curr in parent_map:
            if curr in roots:
                curr = roots[curr]
                break
            p = parent_map[curr]
            if pd.isna(p) or p == curr:
                break
            path.append(curr)
            curr = p
        for node in path:
            roots[node] = curr
        roots[t_id] = curr
        
    df['root_id'] = df['tweet_id'].map(roots)
    
    brand = "AmazonHelp"
    b_roots = df[df['author_id'] == brand]['root_id'].unique()
    b_all = df[df['root_id'].isin(b_roots)]
    
    # Inbound customer messages in AmazonHelp threads
    inbound = b_all[(b_all['inbound'] == True) & (b_all['author_id'] != brand)]
    
    print(f"Total AmazonHelp inbound messages: {len(inbound)}")
    
    # We want to sample across different lengths and times. 
    # Let's take a deterministic sample of 1000 messages for exploration.
    sample = inbound.sample(n=1000, random_state=42)
    
    # Basic frequency analysis for candidate intents
    all_text = " ".join(sample['text'].dropna().tolist())
    unigrams = [w for w in re.findall(r'\b[a-z]{4,}\b', all_text.lower()) if w not in {'amazon', 'amazonhelp', 'http', 'https', 'this', 'that', 'with', 'have', 'your', 'from', 'what', 'they', 'will', 'just', 'been', 'when', 'there'}]
    bigrams = get_ngrams(all_text, 2)
    trigrams = get_ngrams(all_text, 3)
    
    print("\nTop 30 unigrams:")
    print(Counter(unigrams).most_common(30))
    print("\nTop 30 bigrams:")
    print(Counter(bigrams).most_common(30))
    print("\nTop 30 trigrams:")
    print(Counter(trigrams).most_common(30))
    
    # Let's also create a validation set of 200 messages for step 8
    # Ensure they don't overlap with the exploration sample
    remaining = inbound.drop(sample.index)
    validation_sample = remaining.sample(n=200, random_state=42)
    
    import os
    os.makedirs("reports", exist_ok=True)
    
    sample.to_csv("reports/amazon_exploration_sample.csv", index=False)
    validation_sample.to_csv("reports/amazon_validation_sample.csv", index=False)
    
    # Write a readable markdown for manual inspection (just first 100)
    with open("reports/amazon_sample.md", "w", encoding="utf-8") as f:
        for idx, row in sample.head(100).iterrows():
            f.write(f"**Tweet ID:** {row['tweet_id']} | **Author:** {row['author_id']}\n")
            f.write(f"{row['text']}\n")
            f.write("---\n")
            
    print("\nSaved reports/amazon_exploration_sample.csv and reports/amazon_sample.md")

if __name__ == "__main__":
    main()
