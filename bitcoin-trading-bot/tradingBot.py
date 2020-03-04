import DateTime
import DiscordClient
import BinanceClient




def run():

    print("This is a python script Developed by Mark Lambert.")
    print("This trading bot has been configured to use the Binance.us exchange.")
    print("Trading pairs utilized are: BTCUSDT")
    
    #make call to Binance to gather trading data
    print(BinanceClient.getMarkets())

    tickerData = BinanceClient.getBinanceTickerData('BTC/USDT')
    print("ticker Data: ",tickerData)
       
       
    print("calling webhook with ticker data, check your discord!")
    DiscordClient.callWebhook("ticker Data: " + tickerData.toString())
       
    print("making test order")
    testOrder = BinanceClient.makeTestOrder()
    print(testOrder)
    
    
    















run()


#when ready, switch to the below method to run the job continuously
'''
while(True):
    run()
'''
