import requests
import DiscordKey
import json

discordApi = DiscordKey.DiscordWebhook.get('webhookUrl')

def callWebhook(message):
    print(discordApi)
    message = '{"username": "Trading Bot","avatar_url": "https://i.imgur.com/4M34hi2.png", "content": "'+message+'"}'
    jsonMessage = json.loads(message)
    header = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    requests.post(url=discordApi, data=jsonMessage, headers=header)

callWebhook('abc')