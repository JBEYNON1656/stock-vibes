from flask import Blueprint, jsonify
import requests, os
from .stock_utils import save_stock_to_csv

bp = Blueprint('main', __name__)

@bp.route('/')
def home():
    return "Welcome to StockVibes API"

@bp.route('/help')
def help():
    return "HELP"