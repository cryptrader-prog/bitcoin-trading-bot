import DiscordClient
import BinanceClient


def run():

    print("This is a python script Developed by cryptrader-prog.")
    print("This trading bot has been configured to use the Binance.us exchange.")
    print("Trading pairs utilized are: BTC/USD")
    
    #make call to Binance to gather trading data
    print(BinanceClient.getMarkets())

    tickerData = BinanceClient.getBinanceTickerData('BTC/USD')
    print("ticker Data: ",tickerData)
    symbolname =tickerData.get('symbol')
    marketHigh = tickerData.get('high')
    marketLow = tickerData.get('low')
    priceChange = tickerData.get('priceChangePercent')

    #prints current high and low for given symbol
    message = "symbol ("+ str(symbolname) + ") data: currentHigh: " + str(marketHigh) + " currentLow: " + str(marketLow) + " PriceChange: " + str(priceChange)

    #sends symbol data to discord channel
    print("calling webhook with ticker data, check your discord!")
    DiscordClient.callWebhook("ticker Data: " + message)

    #gets current balances of all currencies and displays freely usable funds for BTC and USD
    print("getting balance")
    balance = BinanceClient.getBalance()
    availableBtcFunds = balance['BTC']
    availableUsdFunds = balance['USD']
    print("available funds for trading: BTC = " + str(availableBtcFunds['free']) + ", USD = " + str(availableUsdFunds['free']))

    #makes a test order to confirm able to place orders
    print("placing a test order")
    testOrder = BinanceClient.makeTestOrder()
    print(testOrder)


    
    















run()


#when ready, switch to the below method to run the job continuously
'''
while(True):
    run()
'''
