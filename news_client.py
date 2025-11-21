import requests
from config import NEWS_API_KEY

def fetch_ai_news(limit=20):
    url = "https://newsapi.org/v2/everything"
    params = {
        "q": "AI startup OR artificial intelligence funding",
        "language": "en",
        "sortBy": "publishedAt",
        "apiKey": NEWS_API_KEY,
        "pageSize": limit 
    }  
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        articles = data.get("articles", [])
        print(f"✅ Fetched {len(articles)} raw articles.")
        return articles
    except Exception as e:
        print(f"Error fetching news: {e}")
        return []