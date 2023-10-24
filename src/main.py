
from newscover.newsapi import fetch_latest_news


def main():
    api_key = '7b595b26853642c4a2cecb2fe18224a6'
    data = fetch_latest_news(api_key,"Taylor,Swift,Concerts",10)


    

if __name__ == "__main__":

    main()