import DateTime
import DiscordClient
import BinanceClient


def run():

    print("This is a python script Developed by Mark Lambert.")
    print("This trading bot has been configured to use the Binance.us exchange.")
    print("Trading pairs utilized are: BTCUSDT")
    
    #make call to Binance to gather trading data
    try:
        historicalData = BinanceClient.getHistoricalData()
        print("Historical Data: ",historicalData)
    except:
        pass















run()
'''
while(True):
    run()
'''
