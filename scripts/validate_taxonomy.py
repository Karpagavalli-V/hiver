import pandas as pd
import random
import os

def main():
    df = pd.read_csv("reports/amazon_validation_sample.csv")
    
    # We will do a simple keyword-based heuristic just to get an approximate distribution
    # This is NOT the final classifier, just an exploration tool.
    
    intents = {
        "OrderDelayedOrLost": ["late", "delayed", "lost", "where is", "hasn't arrived", "not received", "didn't arrive", "where's", "still waiting", "delivery date", "status", "track"],
        "ReturnRefund": ["refund", "return", "cancel", "charged", "money back"],
        "DamagedDefective": ["damaged", "broken", "dirty", "soiled", "defective", "not working", "torn", "scratched", "ruined"],
        "WrongItem": ["wrong item", "not what i ordered", "different item", "sent me the wrong", "incorrect"],
        "DigitalContent": ["kindle", "prime video", "music", "movie", "season", "episode", "audio", "subtitle"],
        "CourierBehavior": ["left it", "dumped", "driver", "courier", "didn't knock", "stolen", "front door", "instructions", "amzl", "usps", "ups"],
        "AccountSecurity": ["hacked", "unauthorized", "locked", "password", "stolen account", "someone bought"],
        "CustomerServiceEscalation": ["on hold", "customer service", "no reply", "promised a call", "still waiting for an email", "worst service", "agents", "rep", "manager"],
        "ThanksOrPraise": ["thank", "awesome", "great job", "love amazon", "kudos"]
    }
    
    results = {k: 0 for k in intents.keys()}
    results["OTHER"] = 0
    results["AMBIGUOUS"] = 0
    
    for _, row in df.iterrows():
        text = str(row['text']).lower()
        matched = []
        for intent, keywords in intents.items():
            if any(k in text for k in keywords):
                matched.append(intent)
                
        if len(matched) == 1:
            results[matched[0]] += 1
        elif len(matched) > 1:
            results["AMBIGUOUS"] += 1
        else:
            results["OTHER"] += 1
            
    print("Approximate Distribution on Validation Set (Heuristic Keyword Matching):")
    for k, v in sorted(results.items(), key=lambda x: x[1], reverse=True):
        print(f"{k}: {v} ({(v/len(df))*100:.1f}%)")
        
    # Let's dump some "OTHER" to see what we missed
    print("\nSample OTHER tweets:")
    count = 0
    for _, row in df.iterrows():
        text = str(row['text']).lower()
        matched = []
        for intent, keywords in intents.items():
            if any(k in text for k in keywords):
                matched.append(intent)
        if len(matched) == 0 and count < 10:
            print("-", row['text'].replace('\n', ' '))
            count += 1

if __name__ == "__main__":
    main()
