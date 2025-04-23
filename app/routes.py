from flask import Blueprint, jsonify
from .stock_utils import get_stock_data, save_stock_to_csv

bp = Blueprint('main', __name__)

@bp.route('/')
def home():
    return "Welcome to StockVibes API"

@bp.route('/stock/<symbol>')
def fetch_and_save_stock(symbol):
    data = get_stock_data(symbol)

    #ensures that the data is not empty. Finnhub returns 200, but blank data for invalid stock symbols, so need to check for blankness too 
    if data and data.get("t", 0) != 0:
        save_stock_to_csv(symbol, data)
        return jsonify({"message": f"Data for {symbol.upper()} saved." }), 200
    else:
        return jsonify({"error": f"Invalid or unknown stock symbol: {symbol.upper()}"}), 400