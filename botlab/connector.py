"""
Inspirade by:
    http://flask.pocoo.org/docs/0.12/testing/
    https://blog.hartleybrody.com/fb-messenger-bot/
    http://www.inf.ufrgs.br/~viviane/rslp/index.htm
    https://github.com/EmilStenstrom/rippletagger/tree/master/rippletagger
"""
import os
import sys
import json
import requests
import botlab.config as config
from flask import Flask, request
from botlab.replier import reply

app = Flask(__name__)

@app.route('/', methods=['GET'])
def verify_token():
    log("verify_token")
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if request.args.get("hub.verify_token") == os.environ["VERIFY_TOKEN"]:
            return request.args["hub.challenge"], 200
        return "Verification token mismatch", 403
    return "Hello world", 200

@app.route('/', methods=['POST'])
def on_message_receive():
    log("on_message_receive")
    data = request.get_json()
    log(data)
    if data["object"] == "page":
        for entry in data["entry"]:
            for messaging_event in entry["messaging"]:
                if messaging_event.get("message"):
                    handle_message(messaging_event)
    return "ok", 200

def handle_message(event):
    log("handle_message")
    sender_id = event["sender"]["id"]
    message_text = event["message"]["text"]
    answer = reply(sender_id, message_text)
    send_message(sender_id, answer)

def send_message(recipient_id, message_text):
    log("send_message")
    log("sending message to {}: {}".format(recipient_id, message_text))
    params = {
        "access_token": os.environ["PAGE_ACCESS_TOKEN"]
    }
    headers = {
        "Content-Type": "application/json"
    }
    data = json.dumps({
        "recipient": {
            "id": recipient_id
        },
        "message": {
            "text": message_text
        }
    })
    r = requests.post(config.REPLY_ENDPOINT, params=params, headers=headers, data=data)
    if r.status_code != 200:
        log(r.status_code)
        log(r.text)

def send_button(recipient_id, message_text):
    log("send_message")
    log("sending message to {}: {}".format(recipient_id, message_text))
    params = {
        "access_token": os.environ["PAGE_ACCESS_TOKEN"]
    }
    headers = {
        "Content-Type": "application/json"
    }
    data = json.dumps({
        "recipient": {
            "id": recipient_id
        },
        "message": {
            "attachment":{
              "type":"template",
              "payload":{
                "template_type":"button",
                "text":"What do you want to do next?",
                "buttons":[
                  {
                    "type":"web_url",
                    "url":"https://www.messenger.com",
                    "title":"Visit Messenger"
                  }
                  ]}}}

    })
    r = requests.post(config.REPLY_ENDPOINT, params=params, headers=headers, data=data)
    if r.status_code != 200:
        log(r.status_code)
        log(r.text)

def log(msg, *args, **kwargs):
    print(msg)
    sys.stdout.flush()

if __name__ == '__main__':
    app.run(debug=True)