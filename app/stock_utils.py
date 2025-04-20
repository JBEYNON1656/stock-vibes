import csv
import requests
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv() #loads utility to read the .env file for secrets
api_key = os.getenv("FINNHUB_API_KEY")

#defines a function that takes a stock symbol and data (as a dictionary) to write to a CSV
def get_stock_data(symbol):
    url = f"https://finnhub.io/api/v1/quote?symbol={symbol}&token={api_key}"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json() 
    else:
        print("Error:", response.status_code)
        return None
    
def save_stock_to_csv(symbol, data):

    #opens or creates a new file in append mode (a), meaning new data will be added to the end of the file. Newline ensures new lines are written correctly without blanks
    with open("stock_data.csv", "a", newline="") as f:
        #creates a writer linked to f, which handles writing rows to csv files out of the box
        writer = csv.writer(f)

        #checks if the file is empty to write the first row
        if f.tell() == 0: #returns current file pointer. If 0, there are no rows
            writer.writerow(["timestamp", "symbol", "current_price", "high", "low", "open", "previous_close"])

        #writes row to csv
        writer.writerow([
            datetime.now().isoformat(),
            symbol.upper(),
            data.get("c"),
            data.get("h"),
            data.get("l"),
            data.get("o"),
            data.get("pc")
        ])

def get_long_name(symbol):
    url = f"https://finnhub.io/api/v1/search?q={symbol}&token={api_key}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        for item in data.get('result',[]):
            if item['symbol'] == symbol:
                print(item['description'])
                return item['description']
        print(f"No exact match for {symbol} found")
        return None
    else:
        print(f"Error fetching long name for symbol {symbol}")
        return None
    

get_long_name("DIS")