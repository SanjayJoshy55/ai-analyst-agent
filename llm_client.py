import json
import google.generativeai as genai
from config import GEMINI_API_KEY, GEMINI_MODEL
genai.configure(api_key=GEMINI_API_KEY)

def extract_json(article):
    title = article.get('title', '')
    desc = article.get('description', '')
    if not title or not desc:
        return None
    prompt = f"""
    Analyze this news article and extract structured data.
    Article Title: {title}
    Article Description: {desc}

    Return a JSON object with these exact keys:
    - summary (string, a concise 1-sentence summary of what happened)
    - company_name (string, "N/A" if not found)
    - category (string, e.g., "Healthcare", "Finance", "Generative AI")
    - sentiment_score (float between -1.0 and 1.0)
    - is_funding_news (boolean)
    """

    try:
        model = genai.GenerativeModel(
            GEMINI_MODEL,
            generation_config={"response_mime_type": "application/json"}
        )
        response = model.generate_content(prompt)
        return json.loads(response.text)    
    except Exception as e:
        print(f"LLM Error on '{title[:30]}...': {e}")
        return None