from datetime import datetime

def check_article_date(articles, cutoff_date):
    
    for article in articles:
        published_date = article["publishedAt"]

        article_date = datetime.strptime(published_date, "%Y-%m-%d")
        cutoff_date = datetime.strptime(cutoff_date, "%Y-%m-%d")

        if article_date <= cutoff_date:
            return False

    return True

