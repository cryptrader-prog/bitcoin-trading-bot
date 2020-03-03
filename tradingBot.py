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
        DiscordClient.callWebhook("ticker Data: " + tickerData)
        
        print("ticker Data: ",tickerData)
    except:
        pass















run()


#when ready, switch to the below method to run the job continuously
'''
while(True):
    run()
'''
