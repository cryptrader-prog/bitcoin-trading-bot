import json

from keyValues import DiscordWebhook
import requests

# used to post messages to discord
discordApi = DiscordWebhook.get('webhookUrl')


def callWebhook(message):
    data = {}
    data["content"] = message
    data["username"] = "bitcoin bot"

    result = requests.post(discordApi, data=json.dumps(data), headers={"Content-type": "application/json"})
    try:
        result.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(err)

