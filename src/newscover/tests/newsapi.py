import unittest
from newscover.newsapi import fetch_latest_news
from utils import check_article_date
from newscover.newsapi import get_from_date
class TestKeyWords(unittest.TestCase):

    def test_missing_news_keywords(self):
        api_key = '7b595b26853642c4a2cecb2fe18224a6'
        news_keywords = None  
        lookback_days = 10

        with self.assertRaises(Exception) as context:
            fetch_latest_news(api_key, news_keywords, lookback_days)

        self.assertIn("unable to fetch articles for", str(context.exception))

    def test_good_keywords(self):
        api_key = '7b595b26853642c4a2cecb2fe18224a6'
        news_keywords = "Taylor"  
        lookback_days = 10

        try:
            result = fetch_latest_news(api_key, news_keywords, lookback_days)
        except Exception as e:
            self.fail(f"Exception raised: {str(e)}")



class TestDate(unittest.TestCase):

    def test_correct_case(self):
        api_key = '7b595b26853642c4a2cecb2fe18224a6'
        news_keywords = "Taylor"  
        lookback_days = 10

        cutoff_date = get_from_date(lookback_days)
        articles = fetch_latest_news(api_key, news_keywords, lookback_days)

        result = check_article_date(articles, cutoff_date)

        self.assertTrue(result)  # All articles are after the cutoff date

    def test_correct_case(self):
        api_key = '7b595b26853642c4a2cecb2fe18224a6'
        news_keywords = "Taylor"  
        lookback_days = 100 

        cutoff_date = get_from_date(1) #set the cutoff date only yesterday from today(when program is run)
        articles = fetch_latest_news(api_key, news_keywords, lookback_days)

        result = check_article_date(articles, cutoff_date)

        self.assertFalse(result)  


    
if __name__ == '__main__':
    unittest.main()
