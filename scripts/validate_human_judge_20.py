import os
import sys
import pandas as pd
from typing import List, Tuple

CSV_PATH = "data/human_judge/human_judge_20.csv"
REQUIRED_HUMAN_COLS = [
    "human_relevance",
    "human_groundedness",
    "human_helpfulness",
    "human_safety",
    "human_tone"
]
REQUIRED_JUDGE_COLS = [
    "judge_relevance",
    "judge_groundedness",
    "judge_helpfulness",
    "judge_safety",
    "judge_tone"
]

def validate_human_judge_csv(filepath: str = CSV_PATH) -> Tuple[bool, List[str]]:
    errors = []
    
    if not os.path.exists(filepath):
        return False, [f"File not found: {filepath}"]

    df = pd.read_csv(filepath)
    
    # Check total rows
    if len(df) != 20:
        errors.append(f"Expected exactly 20 rows, but found {len(df)} rows.")

    # Check unique Golden IDs
    gids = df["golden_id"].dropna().tolist()
    if len(gids) != len(set(gids)):
        errors.append("Duplicate golden_id values found in dataset.")

    # Check human rating completeness and valid range (1-5)
    missing_ratings = 0
    invalid_range_count = 0
    copied_exact_judge_count = 0

    for idx, row in df.iterrows():
        gid = row.get("golden_id", f"Row {idx+1}")
        row_human_scores = []
        row_judge_scores = []

        for hcol in REQUIRED_HUMAN_COLS:
            val = row.get(hcol)
            if pd.isna(val) or str(val).strip() == "" or str(val).strip().lower() == "nan":
                missing_ratings += 1
                errors.append(f"[{gid}] Missing rating for field '{hcol}'.")
            else:
                try:
                    score = int(float(val))
                    if not (1 <= score <= 5):
                        invalid_range_count += 1
                        errors.append(f"[{gid}] Field '{hcol}' score {score} out of 1-5 range.")
                    else:
                        row_human_scores.append(score)
                except ValueError:
                    errors.append(f"[{gid}] Field '{hcol}' non-numeric value: {val}.")

        for jcol in REQUIRED_JUDGE_COLS:
            jval = row.get(jcol)
            if not pd.isna(jval):
                try:
                    row_judge_scores.append(int(float(jval)))
                except ValueError:
                    pass

        # Check if human scores are exact copy of judge scores across all 5 dimensions
        if len(row_human_scores) == 5 and len(row_judge_scores) == 5 and row_human_scores == row_judge_scores:
            copied_exact_judge_count += 1

    if copied_exact_judge_count == len(df) and len(df) > 0:
        errors.append("CRITICAL: All human ratings are exact copies of LLM judge ratings! Ratings appear fabricated/copied.")

    is_valid = len(errors) == 0
    return is_valid, errors

def main():
    print("=" * 80)
    print(" VALIDATING HUMAN-AS-A-JUDGE (20 EXAMPLES) DATASET")
    print("=" * 80)
    
    is_valid, errors = validate_human_judge_csv()
    
    if is_valid:
        print("SUCCESS: dataset is valid! All 20 examples have complete, valid human ratings.")
        sys.exit(0)
    else:
        print(f"VALIDATION FAILED with {len(errors)} error(s):")
        for err in errors[:10]:
            print(f" - {err}")
        if len(errors) > 10:
            print(f" ... and {len(errors) - 10} more errors.")
        sys.exit(1)

if __name__ == "__main__":
    main()
