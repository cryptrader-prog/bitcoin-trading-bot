import BinanceKey
import ccxt

# ccxt docs https://buildmedia.readthedocs.org/media/pdf/ccxt/stable/ccxt.pdf

apiKey = BinanceKey.BinanceKey1.get('api_key')
apiSecret = BinanceKey.BinanceKey1.get('api_secret')



#sets exchange api key and secret for ccxt
#exchange id can be changed to use other exchanges, for example: to use binance.com instead of binance.us, change the id to 'binance'
exchange_id = 'binanceus'
exchange_class = getattr(ccxt, exchange_id)
exchange = exchange_class({
    'apiKey': apiKey,
    'secret': apiSecret,
    'enableRateLimit': True,
    'options': { 'adjustForTimeDifference': True }
})

markets = exchange.load_markets()

def getBinanceTickerData(ticker):

    return exchange.fetch_ticker(symbol=ticker)

def getAvailableCurrencies():
    return exchange.fetch_currencies()

def getBalance():
    return exchange.fetch_balance()

def makePurchase(amt, price):
    symbol = 'BTC/USD'
    type = 'market'  # 'limit' or 'market'
    side = 'buy'  # 'buy' or 'sell'
    amount = amt
    price = None  # or None
    params = {
        'test': False,  # test if it's valid, but don't actually place it
    }
    return exchange.create_order(symbol, type, side, amount, price, params)


def makeSale(amt, price):
    symbol = 'BTC/USD'
    type = 'market'  # ' limit' or 'market'
    side = 'sell'  # 'buy' or 'sell'
    amount = amt
    price = price  # or None
    params = {
        'test': False,  # test if it's valid, but don't actually place it
    }
    return exchange.create_order(symbol, type, side, amount, price, params)


def makeTestOrder():
    symbol = 'BTC/USDT'
    type = 'limit'  # or 'market'
    side = 'sell'  # or 'buy'
    amount = .001
    price = 10000.00  # or None
    params = {
    'test': True,  # test if it's valid, but don't actually place it
    }
    return exchange.create_order(symbol, type, side, amount, price, params)

def getMarkets():
    return print(exchange.id, markets)

