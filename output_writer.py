import pandas as pd
import os

def save_to_csv(data, filename="samples/ai_startup_data.csv"):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    if not data:
        print(" No data to save.")
        return
    df = pd.DataFrame(data)
    cols = ["company_name", "category", "sentiment_score", "is_funding_news", "title", "url"]
    existing_cols = [c for c in cols if c in df.columns]
    df = df[existing_cols]
    df.to_csv(filename, index=False)
    print(f"💾 Successfully saved {len(df)} rows to {filename}")