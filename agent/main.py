import requests
import pymongo

API_URL = 'https://api.coinmarketcap.com/v1/ticker/'

def get_db_connection(uri):
    client = pymongo.MongoClient(uri)
    return  client.cryptongo

def get_crytocurrencies_from_api():
    r = requests.get(API_URL)
    if r.status_code == 200:
        result = r.json()
        return  result

    raise Exception('Api Error')

def get_hash():
    pass

def first_element():
    pass

def get_ticker_hash():
    pass


def check_if_exists(db_connection, ticker_data):
    pass

def save_ticket(db_connection, ticker_data = None):
    if not ticker_data:
        return  False

    if check_if_exists(db_connection, ticker_data):
        return  False


