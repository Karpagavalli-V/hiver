from typing import List, Dict, Tuple, Any

def calculate_cohen_kappa(human_scores: List[int], judge_scores: List[int], max_score: int = 5) -> float:
    """
    Calculates Cohen's kappa for categorical agreement.
    Note: Requires EXACT matches for agreement. For ordinal ratings (1-5), weighted kappa is better.
    """
    if not human_scores or not judge_scores or len(human_scores) != len(judge_scores):
        return 0.0
        
    n = len(human_scores)
    # Create confusion matrix
    matrix = [[0 for _ in range(max_score)] for _ in range(max_score)]
    
    for h, j in zip(human_scores, judge_scores):
        if 1 <= h <= max_score and 1 <= j <= max_score:
            matrix[h-1][j-1] += 1
            
    p0 = sum(matrix[i][i] for i in range(max_score)) / n
    
    pe = 0
    for i in range(max_score):
        row_sum = sum(matrix[i][j] for j in range(max_score))
        col_sum = sum(matrix[j][i] for j in range(max_score))
        pe += (row_sum / n) * (col_sum / n)
        
    if pe == 1.0:
        return 1.0 # Perfect agreement and predictions
        
    kappa = (p0 - pe) / (1 - pe)
    return kappa

def calculate_weighted_kappa(human_scores: List[int], judge_scores: List[int], max_score: int = 5) -> float:
    """
    Calculates quadratic weighted kappa for ordinal 1-5 ratings.
    """
    if not human_scores or not judge_scores or len(human_scores) != len(judge_scores):
        return 0.0
        
    n = len(human_scores)
    matrix = [[0 for _ in range(max_score)] for _ in range(max_score)]
    
    for h, j in zip(human_scores, judge_scores):
        if 1 <= h <= max_score and 1 <= j <= max_score:
            matrix[h-1][j-1] += 1
            
    # Calculate weights matrix (quadratic)
    weights = [[0 for _ in range(max_score)] for _ in range(max_score)]
    for i in range(max_score):
        for j in range(max_score):
            weights[i][j] = ((i - j) ** 2) / ((max_score - 1) ** 2)
            
    # Calculate expected matrix
    expected = [[0 for _ in range(max_score)] for _ in range(max_score)]
    for i in range(max_score):
        row_sum = sum(matrix[i][x] for x in range(max_score))
        for j in range(max_score):
            col_sum = sum(matrix[x][j] for x in range(max_score))
            expected[i][j] = (row_sum * col_sum) / n
            
    # Calculate kappa
    num = 0
    den = 0
    for i in range(max_score):
        for j in range(max_score):
            num += weights[i][j] * matrix[i][j]
            den += weights[i][j] * expected[i][j]
            
    if den == 0:
        return 1.0
        
    return 1.0 - (num / den)

def check_human_ratings_available(golden_set_df) -> Tuple[bool, str]:
    """
    Checks if genuine human reply-quality ratings are available.
    """
    if 'human_reply_quality' not in golden_set_df.columns:
        return False, "Column 'human_reply_quality' does not exist."
        
    # Check if there are any non-null integer ratings
    valid_ratings = golden_set_df['human_reply_quality'].dropna()
    
    if len(valid_ratings) == 0:
        return False, "No valid human ratings found."
        
    # Check if the column is mixed with AI-assisted placeholders
    # In our project, if the user didn't independently review them, we shouldn't use them.
    # The prompt says: "Do NOT fabricate this metric... clearly report 'NOT AVAILABLE' if genuine human reply-quality ratings are not yet present."
    # Since the annotations are currently a mixture, we enforce returning False.
    return False, "Current Golden Set annotations are a mixture of manually reviewed and AI-assisted annotations. Independent human reply-quality ratings are not available yet."

def report_agreement() -> str:
    return "Not available yet — no fabricated agreement score is reported."
