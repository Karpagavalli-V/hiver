import pandas as pd
import random
import os

def main():
    # Load exploration sample
    expl_df = pd.read_csv("reports/amazon_exploration_sample.csv")
    val_df = pd.read_csv("reports/amazon_validation_sample.csv")
    
    # We want to pull some keyword-based samples from exploration set to make it easier to find candidate examples for each intent.
    # We will just dump them to a markdown file for the agent to read.
    
    intents = {
        "DeliveryStatus": ["late", "delayed", "lost", "where is", "hasn't arrived", "not received", "didn't arrive", "delivery date", "status", "track", "arrive by"],
        "RefundsAndReturns": ["refund", "return", "cancel", "charged", "money back"],
        "DamagedOrDefective": ["damaged", "broken", "dirty", "soiled", "defective", "not working", "torn", "scratched", "ruined", "quality"],
        "WrongItem": ["wrong item", "not what i ordered", "different item", "sent me the wrong", "incorrect", "instead of"],
        "CourierFeedback": ["left it", "dumped", "driver", "courier", "didn't knock", "stolen", "front door", "instructions", "amzl", "usps", "ups"],
        "AccountAndPayment": ["hacked", "unauthorized", "locked", "password", "stolen account", "someone bought", "charge", "charged", "bank", "credit card", "prime fee"],
        "DigitalServices": ["kindle", "prime video", "music", "movie", "season", "episode", "audio", "subtitle", "streaming", "app"],
        "CustomerServiceEscalation": ["on hold", "customer service", "no reply", "promised a call", "still waiting for an email", "worst service", "agents", "rep", "manager", "called", "spoke to"],
        "OTHER": ["thank", "awesome", "great job", "love amazon", "kudos", "gracias", "merci", "danke"]
    }
    
    with open("reports/audit_exploration_samples.md", "w", encoding="utf-8") as f:
        for intent, keywords in intents.items():
            f.write(f"\n# Intent: {intent}\n\n")
            # Find matching tweets
            matches = expl_df[expl_df['text'].str.contains('|'.join(keywords), case=False, na=False)]
            # If we don't have enough matches, add some random ones
            sample_size = min(30, len(matches))
            if sample_size > 0:
                sampled = matches.sample(sample_size, random_state=42)
                for _, row in sampled.iterrows():
                    f.write(f"- [ID: {row['tweet_id']}] {row['text'].replace('\n', ' ')}\n")
            else:
                f.write("No matches found in exploration set for this heuristic.\n")
                
    # Also dump the entire validation sample (200) for manual ambiguity annotation
    with open("reports/audit_validation_manual.md", "w", encoding="utf-8") as f:
        f.write("# Validation Set (200 messages for manual audit)\n\n")
        for _, row in val_df.iterrows():
            f.write(f"ID: {row['tweet_id']}\nTEXT: {row['text'].replace('\n', ' ')}\n---\n")
            
    print("Prepared reports/audit_exploration_samples.md and reports/audit_validation_manual.md")

if __name__ == "__main__":
    main()
