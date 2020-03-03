import DateTime
import DiscordClient
from ccxt import binanceus


def run():

    print("This is a python script Developed by Mark Lambert.")
    print("This trading bot has been configured to use the Binance.us exchange.")
    print("Trading pairs utilized are: BTCUSDT")
    
    #make call to Binance to gather trading data
    try:
        symbolData = binanceus.symbols
        
        print("symbol Data: ",symbolData)
    except:
        pass















run()
'''
while(True):
    run()
'''
