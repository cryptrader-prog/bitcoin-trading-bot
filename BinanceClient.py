import requests
import DateTime
import time
import json


baseApiUrl = 'https://api.binance.us'
connectivityEndpoint = '/api/v3/ping'
klineDataEndpoint = '/api/v3/klines'
testOrderEndpoint = '/api/v3/order/test'
tickerEndpoint = '/api/v3/ticker/price'


header = header = {'Content-type': 'application/json', 'Accept': 'text/plain'}

def getHistoricalData():
    url = baseApiUrl + klineDataEndpoint
    data = {'symbol': 'BTCUSDT', 'interval': 'KLINE_INTERVAL_1MINUTE'}
    jsonData = json.loads(data)
    try:
        response = requests.get(url, data=jsonData, header = header)
        if(response.status_code == 200)
            return response
        else:
            return 'recieved error code '+ response.status_code + ' when attempting to retrieve historical kline data'
    except:
        return 'error making historical data call to Binanace Exchange'
    
def testConnectivity():
    url = baseApiUrl + connectivityEndpoint
    try:
        response = requests.get(url)
        if(response.status_code == 200):
            return "connection is valid"
        else:
            return "error connecting to Binance exchange"
    
    except:
        return 'exception thrown while trying to ping binance exchange'

def getLatestPrice():
    url = baseApiUrl + tickerEndpoint
    data = {"symbol": "BTCUSDT"}
    jsonData = json.loads(data)
    try:
        response = requests.get(url, data=jsonData)
        if(response.status_code == 200):
            return response
        else:
            return 'recieved error code '+ response.status_code + ' when attempting to retrieve ticker data'
    except:

def makePurchase():
    pass

def makeTestOrder():
    pass

def makeSale():
    pass



