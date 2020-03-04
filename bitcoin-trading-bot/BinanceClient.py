import requests
import DateTime
import time
import json
import BinanceKey
from hashlib import sha256
from urllib.parse import urlencode
import hmac
import ccxt

# Information used for developing api calls was found at https://github.com/binance-exchange/binance-official-api-docs
# Each method that sends json in the api call uses the "data" variable to pass in json information 


apiKey = BinanceKey.BinanceKey1.get('api_key')
apiSecret = BinanceKey.BinanceKey1.get('api_secret')

Ccxt = ccxt.binanceus()

#sets exchange api key and secret for ccxt
exchange_id = 'binanceus'
exchange_class = getattr(ccxt, exchange_id)
exchange = exchange_class({
    'apiKey': 'YOUR_API_KEY',
    'secret': 'YOUR_API_SECRET',
    'enableRateLimit': True,
    'options': {
        'defaultType': 'future',  # ←-------------- quotes and 'future'
    },
})

markets = exchange.load_markets()

def getBinanceTickerData(ticker):

    return exchange.fetch_ticker(symbol=ticker)

def getAvailableCurrencies():
    return exchange.fetch_currencies()

def getBalances():
    return exchange.fetch_balance()

def makePurchase():
    pass

def makeSale():
    pass

def makeTestOrder():
    symbol = 'BNB/BTC'  
    type = 'limit'  # or 'market'
    side = 'sell'  # or 'buy'
    amount = 1.0
    price = 0.060154  # or None
    params = {
    'test': True,  # test if it's valid, but don't actually place it
    }
    return exchange.create_order(symbol, type, side, amount, price, params)

def getMarkets():
    return print(exchange.id, markets)