import csv
import requests
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv() #loads utility to read the .env file for secrets

api_key = os.getenv("GNEWS_API_KEY") #gets API key from env file

#get data for 10 news article for given symbol
def get_news_data(symbol):
    query = symbol.replace("& ", "").replace("/", " ")
    url = f"https://gnews.io/api/v4/search?q={query}&lang=en&country=us&max=10&apikey={api_key}"
    #send the API request
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        #returns the articles as a list
        return data.get("articles", [])
        
    else:
        print("Error:", response.status_code)
        return None
    
def save_news_to_csv(symbol, articles):
    
    #opens or creates a new file in append mode (a), meaning new data will be added to the end of the file. Newline ensures new lines are written correctly without blanks
    with open("data_news.csv", "a", newline="") as f:
        #creates a writer linked to f, which handles writing rows to csv files out of the box
        writer = csv.writer(f)

        #checks if the file is empty to write the first row
        if f.tell() == 0: #returns current file pointer. If 0, there are no rows
            writer.writerow(["timestamp", "symbol", "title", "description", "content", "publishedAt", "sentiment"])

        #writes row to csv
        for article in articles:
            #analyzes sentiment of article description
            sentiment = analyze_sentiment(article["description"])
            writer.writerow([
                datetime.now().isoformat(),
                symbol.upper(),
                article.get("title"),
                article.get("description"),
                article.get("content"),
                article.get("publishedAt"),
                sentiment
        ])
    
#anaylze article description for 
def analyze_sentiment(text):
    from textblob import TextBlob
    blob = TextBlob(text)
    sentiment_score = blob.sentiment.polarity
    if sentiment_score > 0:
        return 'Good'
    elif sentiment_score < 0:
        return 'Bad'
    else:
        return "Neutral"
