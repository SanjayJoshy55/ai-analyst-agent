def is_fluff(article):
    keywords = ["game-changer", "revolutionary", "transformative", "visionary", "unleash", "future of"]
    title = article.get("title", "").lower()
    score = sum(1 for word in keywords if word in title)
    return score >= 2