import DiscordClient
import BinanceClient
import TwitterClient
import indicatorUtils
import log
import time

logger = log.setup_custom_logger('root')

def run():

    logger.info("This is a python script Developed by cryptrader-prog.")
    logger.info("This trading bot has been configured to use the Binance.us exchange.")
    logger.info("Trading pairs utilized are: BTC/USD")
    
    indicatorUtils.createTable()

    while(True):

        #make call to Binance to gather trading data
        logger.info(BinanceClient.getMarkets())

        tickerData = BinanceClient.getBinanceTickerData('BTC/USD')
        logger.info("ticker Data: " + tickerData)
        symbolname =tickerData.get('symbol')
        marketHigh = tickerData.get('high')
        marketLow = tickerData.get('low')
        priceChange = tickerData.get('priceChangePercent')

        #prints current high and low for given symbol
        message = "symbol ("+ str(symbolname) + ") data: currentHigh: " + str(marketHigh) + " currentLow: " + str(marketLow) + " PriceChange: " + str(priceChange)

        #sends symbol data to discord channel
        logger.info("calling webhook with ticker data, check your discord!")
        DiscordClient.callWebhook("ticker Data: " + message)

        #sends symbol data to twitter account
        # print("sending ticker data, check your twitter!")
        # TwitterClient.sendToTwitter("ticker Data: " + message)

        #gets current balances of all currencies and displays freely usable funds for BTC and USD
        logger.info("getting balance")
        balance = BinanceClient.getBalance()
        availableBtcFunds = balance['BTC']
        availableUsdFunds = balance['USD']
        logger.info("available funds for trading: BTC = " + str(availableBtcFunds['free']) + ", USD = " + str(availableUsdFunds['free']))

        #makes a test order to confirm able to place orders
        logger.info("placing a test order")
        testOrder = BinanceClient.makeTestOrder()
        logger.info(testOrder)

        #script sleeps for one minute before next run
        time.sleep(60)



run()



