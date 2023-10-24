#CLI tool 
import argparse
import logging
from newsapi import fetch_latest_news
import json


logger = logging.getLogger(__name__)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-k", dest="api_key", required=True, help="API key string")
    parser.add_argument("-b", dest="back_days", help="backward days")
    parser.add_argument("-i", dest="input_file", required=True, help="input keyword file")
    parser.add_argument("-o", dest="output_dir", required=True, help="output directory")

    args = parser.parse_args()
    json_string = get_keywords_from_file(args.input_file)
    for key in json_string:
        
        for word in set:
            s = ''
            s += word 
            s += "+"
        s -= "+"
        data = fetch_latest_news(args.api_key, args.back_days, args.s)
        output_path = '{args.output_dir}/key'
        with open(output_path, "w") as f:
            json.dump(data, f, indent=4)


def get_keywords_from_file(file):

    with open('data.json', 'r') as file:
        json_data = json.load(file)
    # Convert the JSON data to a JSON-formatted string
    json_string = json.dumps(json_data)
    
    
            
    return json_string







if __name__ == "__main__":
    main()