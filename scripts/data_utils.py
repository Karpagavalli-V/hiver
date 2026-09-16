import pandas as pd
import numpy as np

def build_dataset(raw_df_path, split_csv_path, max_context=3):
    """
    Loads raw text and joins with split assignments.
    Filters to only weakly labeled inbound messages (excluding AMBIGUOUS and NaN).
    Builds X_message_only, X_context_aware, and y.
    """
    raw_df = pd.read_csv(raw_df_path)
    split_df = pd.read_csv(split_csv_path)
    
    # We need the full raw_df for context building, but we only predict on items in split_df that have a weak label.
    # Join
    df = pd.merge(raw_df, split_df[['tweet_id', 'split', 'weak_label', 'root_id']], on='tweet_id', how='inner')
    
    # Sort chronologically. 'created_at' is string, let's convert to datetime.
    df['created_at_dt'] = pd.to_datetime(df['created_at'], format='%a %b %d %H:%M:%S +0000 %Y', errors='coerce')
    df = df.sort_values(by=['root_id', 'created_at_dt'])
    
    # Filter targets
    targets = df[(df['weak_label'].notna()) & (df['weak_label'] != 'AMBIGUOUS')].copy()
    
    X_message = []
    X_context = []
    y = []
    tweet_ids = []
    
    # Build dictionary by root_id for fast context lookup
    # Only keep relevant columns to save memory
    context_pool = df[['tweet_id', 'root_id', 'author_id', 'text', 'created_at_dt']].to_dict('records')
    from collections import defaultdict
    pool_dict = defaultdict(list)
    for row in context_pool:
        pool_dict[row['root_id']].append(row)
        
    for _, target_row in targets.iterrows():
        root = target_row['root_id']
        t_dt = target_row['created_at_dt']
        
        # Chronological filter: strictly BEFORE the target
        thread_msgs = pool_dict[root]
        past_msgs = [m for m in thread_msgs if m['created_at_dt'] < t_dt]
        
        # Take the last `max_context` messages
        past_msgs = past_msgs[-max_context:] if max_context > 0 else []
        
        # Format context
        context_str = ""
        for m in past_msgs:
            prefix = "Amazon:" if m['author_id'] == "AmazonHelp" else "Customer:"
            context_str += f"{prefix} {m['text']} ||| "
            
        context_str += f"Customer: {target_row['text']}"
        
        X_message.append(str(target_row['text']))
        X_context.append(context_str)
        y.append(target_row['weak_label'])
        tweet_ids.append(target_row['tweet_id'])
        
    return pd.DataFrame({
        'tweet_id': tweet_ids,
        'message_only': X_message,
        'context_aware': X_context,
        'label': y
    })
