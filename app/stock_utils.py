import csv
import os
from datetime import datetime

#defines a function that takes a stock symbol and data (as a dictionary) to write to a CSV
def save_stock_to_csv(symbol, data):
    file_exists = os.path.isfile("stock_data.csv")

    #opens or creates a new file in append mode (a), meaning new data will be added to the end of the file. Newline ensures new lines are written correctly without blanks
    with open("stock_data.csv", "a", newline="") as f:
        #creates a writer linked to f, which handles writing rows to csv files out of the box
        writer = csv.writer(f)

        #checks if the file is empty to write the first row
        if f.tell() == 0: #returns current file pointer. If 0, there are no rows
            writer.writerow(["timestamp", "symbol", "current_price", "high", "low", "open", "previous_close"])

            writer.writerow([
                datetime.now().isoformat,
                symbol.upper(),
                data.get("c"),
                data.get("h"),
                data.get("l"),
                data.get("o"),
                data.get("pc")
            ])