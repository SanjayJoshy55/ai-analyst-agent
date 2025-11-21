from rapidfuzz import fuzz
def is_duplicate(article_a, article_b, threshold=85):
    title_a = article_a.get("title", "")
    title_b = article_b.get("title", "")
    return fuzz.ratio(title_a, title_b) > threshold
def remove_duplicates(articles):
    unique = []
    for article in articles:
        if not any(is_duplicate(article, u) for u in unique):
            unique.append(article)   
    removed_count = len(articles) - len(unique)
    print(f" Removed {removed_count} duplicates.")
    return unique