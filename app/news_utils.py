import csv
import requests
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv() #loads utility to read the .env file for secrets

api_key = os.getenv("GNEWS_API_KEY")

def get_news_data(symbol):
    search_value = symbol
    url = f"https://gnews.io/api/v4/search?q={search_value}&lang=en&country=us&max=10&apikey={api_key}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        #returns a list of articles
        return data.get("articles", [])
        
    else:
        print("Error:", response.status_code)
        return None
    
def save_news_to_csv(symbol, articles):
    
    #opens or creates a new file in append mode (a), meaning new data will be added to the end of the file. Newline ensures new lines are written correctly without blanks
    with open("news_data.csv", "a", newline="") as f:
        #creates a writer linked to f, which handles writing rows to csv files out of the box
        writer = csv.writer(f)

        #checks if the file is empty to write the first row
        if f.tell() == 0: #returns current file pointer. If 0, there are no rows
            writer.writerow(["timestamp", "symbol", "title", "description", "content", "publishedAt"])

        for article in articles:
            writer.writerow([
                datetime.now().isoformat(),
                symbol.upper(),
                article.get("title"),
                article.get("description"),
                article.get("content"),
                article.get("publishedAt")
        ])
    
get_news_data("AAPL")