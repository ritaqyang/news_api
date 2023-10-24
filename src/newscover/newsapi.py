import json
import requests
import logging
from datetime import date, timedelta


logger = logging.getLogger(__name__)


API_QUERY_STRING_TEMPLATE = "https://newsapi.org/v2/everything?apiKey={}&q={}&from={}&language=en"

api_key = '7b595b26853642c4a2cecb2fe18224a6'

def fetch_latest_news(api_key, news_keywords, lookback_days):
    #queries the api and 
    # returns a python list of English new articles that:
    # 1. contain those keywords  
    # 2. published within last <lookback_days> 
    #represented as dictionaries 

    from_date = get_from_date(lookback_days)
    keywords = get_news_keywords(news_keywords)
    query_string = API_QUERY_STRING_TEMPLATE.format(api_key,keywords,from_date)
    response = requests.get(query_string)
    if response.status_code != 200:
        raise Exception("unable to fetch articles for {keywords} and from {from_date}")

    data = response.json()
    return data

def get_from_date(lookback_days):

    today = date.today()
    # Calculate the from_date
    from_date = today - timedelta(days=lookback_days)

    return from_date


def get_news_keywords(news_keywords):
    #assume that input is a comma separated string
    #replace comma with +
    modified_string = news_keywords.replace(",", "+")
    return modified_string


    

