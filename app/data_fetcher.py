from stock_utils import get_stock_data, save_stock_to_csv, get_long_name
from news_utils import get_news_data, save_news_to_csv
from config import stocks
import time

def fetch_and_save_stock():
    for symbol in stocks:
        #gets the stock data from Finnhub
        data = get_stock_data(symbol)
        #ensures that the data is not empty. Finnhub returns 200, but blank data for invalid stock symbols, so need to check for blankness too 
        if data and data.get("t", 0) != 0:
            save_stock_to_csv(symbol, data)
            print(f"Stock data from {symbol} written to csv.")
        else:
            print(f"Stock data from {symbol} is empty.")

def fetch_and_save_news():
    for symbol in stocks:
        #delays requests to prevent too many requests error
        time.sleep(1)
        #gets the long name for the stock symbol
        long_name = get_long_name(symbol)
        symbol_and_name = symbol + " " + long_name
        #gets the stock data from Gnews by querying for symbol and long name
        data = get_news_data(symbol_and_name)
        #ensures that the data is not empty.
        if data:
            save_news_to_csv(symbol_and_name, data)
            print(f"News data from {symbol_and_name} written to csv.")
        else:
            print(f"News data from {symbol_and_name} is empty.")

fetch_and_save_stock()
fetch_and_save_news()