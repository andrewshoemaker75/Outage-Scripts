import requests
import json

slackResponse = requests.get("https://status.slack.com/api/v2.0.0/current")
outage = slackResponse.json()
url = "https://api.bigpanda.io/data/v2/alerts"
headers = {

    "Authorization": "Bearer 57ac0a285f2cb36300af3cb19804a67",
    "Content-Type": "application/json",
    "Accept": "application/json"

}

bigPandaPost = requests.post(url, headers=headers, json=
    {
        "app_key": "4013d9600abb99e6243e2d1b1aea49d3",
        "service": "Slack",
        "description": "Slack API is returning an issue with their status. Please refer to https://status.slack.com for further details.",
        "status": "warning"
    })

print(bigPandaPost.status_code)

if outage['status'] == "ok":
    print("Slack status is operational")

else:
    print("Slack status is fucked")
    print(bigPandaPost.text)



# Next line just prints status field received from json object
# print(outage['status'])
