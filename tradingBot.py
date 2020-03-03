import DateTime
import DiscordClient
import BinanceClient




def run():

    print("This is a python script Developed by Mark Lambert.")
    print("This trading bot has been configured to use the Binance.us exchange.")
    print("Trading pairs utilized are: BTCUSDT")
    
    #make call to Binance to gather trading data
    try:
        tickerData = BinanceClient.getBinanceTickerData("BTCUSD")
        print("ticker Data: ",tickerData)
        print("calling webhook with ticker data, check your discord!")
        DiscordClient.callWebhook("ticker Data: " + tickerData)
        print("making test order")
        testOrder = DiscordClient.makeTestOrder()
        print(testOrder)
    except:
        pass















run()


#when ready, switch to the below method to run the job continuously
'''
while(True):
    run()
'''
