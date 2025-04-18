from stock_utils import return_stock_data, save_stock_to_csv
from news_utils import get_news_data, save_news_to_csv
from config import stocks
import time


def fetch_and_save_stock():
    for symbol in stocks:
        #gets the stock data from Finnhub
        data = return_stock_data(symbol)
        #ensures that the data is not empty. Finnhub returns 200, but blank data for invalid stock symbols, so need to check for blankness too 
        if data and data.get("t", 0) != 0:
            save_stock_to_csv(symbol, data)
            print(f"Data from {symbol} written to csv.")
        else:
            print(f"Data from {symbol} is empty.")

def fetch_and_save_news():
    for symbol in stocks:
        #delays requests to prevent too many requests error
        time.sleep(1)
        #gets the stock data from Gnews
        data = get_news_data(symbol)
        #ensures that the data is not empty. Gnews returns 200, but blank data for invalid stock symbols, so need to check for blankness too 
        if data:
            save_news_to_csv(symbol, data)
            print(f"Data from {symbol} written to csv.")
        else:
            print(f"Data from {symbol} is empty.")

fetch_and_save_stock()
fetch_and_save_news()