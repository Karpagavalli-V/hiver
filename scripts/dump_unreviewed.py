import pandas as pd
df = pd.read_csv('data/golden_set/golden_set_final.csv')
unrev = df[df['human_verified_status'] == 'UNREVIEWED'][['golden_id', 'customer_message', 'conversation_context']].fillna('')
with open('compact_unreviewed.txt', 'w', encoding='utf-8') as f:
    for _, r in unrev.iterrows():
        f.write(f"ID:{r['golden_id']} | MSG:{r['customer_message']} | CTX:{r['conversation_context']}\n")
