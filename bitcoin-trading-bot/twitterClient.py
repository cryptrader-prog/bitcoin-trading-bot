import tweepy
import twitterKey

consumerSecret = twitterKey.twitterKey.get('consumer_secret')
accessToken = twitterKey.twitterKey.get('access_token_secret')



# Authenticate to Twitter
auth = tweepy.OAuthHandler("CONSUMER_KEY", consumerSecret)
auth.set_access_token("ACCESS_TOKEN", "ACCESS_TOKEN_SECRET")

# Create API object

def sendToTwitter(message):
# Create a tweet
    api = tweepy.API(auth)
    api.update_status("Hello Tweepy")