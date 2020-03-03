# Crypto Currency Trading Bot

### Getting Started

```
git clone https://github.com/cryptrader-prog/bitcoin-trading-bot.git
```


### Description

- This is a crypto currency trading bot used to parse data from Binance and determine when to buy and sell crypto curencies. 
- When a trade is made an alert is sent to a discord webhook.
- Trade logic is left out in this project, but the methods for the api calls, discord calls, key values, and binance exchange data are available to be built off of.
- Note: this is set up to communicate with Binance.us, if you are planning to use this with Binance.com; you will need to update the base url value, however the api endpoints are the same.


### Setup Instructions

- to run the application, you will need to use "pip install" to install the following dependancies
    - json
    - requests
    - DateTime
    - time
    - ccxt

- in the BinanceClient file, update the api key and api secret with your information
- in the DiscordClient file, update the webhook url with your webhook url



