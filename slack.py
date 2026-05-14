import os
from dotenv import load_dotenv
import requests


def send_to_slack(messages):
    load_dotenv()
    slack_web_hook_url = os.getenv('slack_web_hook_url')
    for message in messages:
        note = {"text" : message}
        response = requests.post(slack_web_hook_url, json = note)
        if response.status_code == 200:
            print ("message to slack is successful")
        else:
            print("message sent to slack failed")
