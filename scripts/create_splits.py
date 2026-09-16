import pandas as pd
import numpy as np
import argparse
import os

def assign_weak_labels(df_inbound):
    """
    Assigns weak labels to inbound messages based on Phase 2 taxonomy keywords.
    Returns a Series of labels. Unmatched or multi-matched are labelled as OTHER or AMBIGUOUS.
    """
    intents = {
        "DeliveryStatus": ["late", "delayed", "lost", "where is", "hasn't arrived", "not received", "didn't arrive", "delivery date", "status", "track", "arrive by"],
        "RefundsAndReturns": ["refund", "return", "cancel", "charged", "money back"],
        "DamagedOrDefective": ["damaged", "broken", "dirty", "soiled", "defective", "not working", "torn", "scratched", "ruined", "quality"],
        "WrongItem": ["wrong item", "not what i ordered", "different item", "sent me the wrong", "incorrect", "instead of"],
        "CourierFeedback": ["left it", "dumped", "driver", "courier", "didn't knock", "stolen", "front door", "instructions", "amzl", "usps", "ups"],
        "AccountAndPayment": ["hacked", "unauthorized", "locked", "password", "stolen account", "someone bought", "charge", "charged", "bank", "credit card", "prime fee"],
        "DigitalServices": ["kindle", "prime video", "music", "movie", "season", "episode", "audio", "subtitle", "streaming", "app"],
        "CustomerServiceEscalation": ["on hold", "customer service", "no reply", "promised a call", "still waiting for an email", "worst service", "agents", "rep", "manager", "called", "spoke to"]
    }
    
    labels = []
    for text in df_inbound['text'].astype(str).str.lower():
        matched = []
        for intent, keywords in intents.items():
            if any(k in text for k in keywords):
                matched.append(intent)
                
        if len(matched) == 1:
            labels.append(matched[0])
        elif len(matched) > 1:
            labels.append("AMBIGUOUS")
        else:
            labels.append("OTHER")
            
    return labels

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default="data/twcs.csv", help="Path to raw dataset")
    parser.add_argument("--seed", type=int, default=42, help="Random seed for splits")
    args = parser.parse_args()

    print(f"Loading {args.input}...")
    df = pd.read_csv(args.input)
    
    print("Tracing conversation roots globally...")
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
    
    print("Isolating AmazonHelp threads...")
    brand = "AmazonHelp"
    b_roots = df[df['author_id'] == brand]['root_id'].unique()
    b_df = df[df['root_id'].isin(b_roots)].copy()
    
    print("Creating splits at the conversation level...")
    # Get unique roots and shuffle deterministically
    unique_roots = b_roots
    np.random.seed(args.seed)
    np.random.shuffle(unique_roots)
    
    n_total = len(unique_roots)
    n_train = int(n_total * 0.8)
    n_val = int(n_total * 0.1)
    
    train_roots = set(unique_roots[:n_train])
    val_roots = set(unique_roots[n_train:n_train+n_val])
    test_roots = set(unique_roots[n_train+n_val:])
    
    def get_split(r_id):
        if r_id in train_roots: return 'TRAIN'
        if r_id in val_roots: return 'VALIDATION'
        return 'INTERNAL_TEST'
        
    b_df['split'] = b_df['root_id'].map(get_split)
    
    # Generate weak labels for inbound messages
    print("Generating weak labels for development...")
    inbound_mask = (b_df['inbound'] == True) & (b_df['author_id'] != brand)
    b_df.loc[inbound_mask, 'weak_label'] = assign_weak_labels(b_df[inbound_mask])
    
    print("Saving reproducible metadata/index files...")
    os.makedirs('data/splits', exist_ok=True)
    
    # We only save the necessary columns to avoid duplicating 516MB
    export_df = b_df[['tweet_id', 'root_id', 'split', 'weak_label', 'created_at']]
    
    export_df[export_df['split'] == 'TRAIN'].to_csv('data/splits/amazon_train.csv', index=False)
    export_df[export_df['split'] == 'VALIDATION'].to_csv('data/splits/amazon_val.csv', index=False)
    export_df[export_df['split'] == 'INTERNAL_TEST'].to_csv('data/splits/amazon_test.csv', index=False)
    
    print("\nSplit statistics (Conversations):")
    print(f"TRAIN: {len(train_roots)}")
    print(f"VALIDATION: {len(val_roots)}")
    print(f"INTERNAL_TEST: {len(test_roots)}")
    
    print("\nInbound Label Distribution (Train):")
    train_inbound = export_df[(export_df['split'] == 'TRAIN') & (export_df['weak_label'].notna())]
    print(train_inbound['weak_label'].value_counts())
    
    print("Done. Saved to data/splits/")

if __name__ == "__main__":
    main()
