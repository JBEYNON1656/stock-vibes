from flask import Blueprint, jsonify
import requests, os
from .stock_utils import get_and_save_stock

bp = Blueprint('main', __name__)

@bp.route('/')
def home():
    return "Welcome to StockVibes API"

@bp.route('/stock/<symbol>')
def fetch_and_save_stock(symbol):
    data = get_and_save_stock(symbol)
    print(data)

    if data and data.get("t", 0) != 0:
        return jsonify({"message": f"Data for {symbol.upper()} saved." }), 200
    else:
        return jsonify({"error": f"Invalid or unknown stock symbol: {symbol.upper()}"}), 400