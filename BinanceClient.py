import requests
import DateTime


baseApiUrl = 'https://api.binance.us'
connectivityEndpoint = '/api/v3/ping'



def getHistoricalData():
    returnVal = 'abcd'
    return returnVal
    
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


def makePurchase():
    pass

def makeTestPurchase():
    pass

def makeSale():
    pass

def makeTestSale():
    pass

