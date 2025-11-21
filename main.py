import time
from news_client import fetch_ai_news
from llm_client import extract_json
from deduplication import remove_duplicates
from hype_filter import is_fluff
from output_writer import save_to_csv

def main():
    print(" Starting AI Analyst Agent")
    raw_articles = fetch_ai_news(limit=10)
    unique_articles = remove_duplicates(raw_articles)
    processed_data = []
    print(f" Processing {len(unique_articles)} articles with LLM...")
    for article in unique_articles:
        if is_fluff(article):
            continue
        insights = extract_json(article)
        time.sleep(2.0)
        if insights:
            combined = {
                "title": article.get("title"),
                "url": article.get("url"),
                "published_at": article.get("publishedAt"),
                **insights
            }
            processed_data.append(combined)
    save_to_csv(processed_data)
    print(" Pipeline finished successfully.")
if __name__ == "__main__":
    main()
