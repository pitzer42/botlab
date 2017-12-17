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
from interpreter import interpret

import requests
from flask import Flask, request

app = Flask(__name__)

REPLY_ENDPOINT = "https://graph.facebook.com/v2.6/me/messages"

@app.route('/', methods=['GET'])
def verify_token():
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if request.args.get("hub.verify_token") == os.environ["VERIFY_TOKEN"]:
            return request.args["hub.challenge"], 200
        return "Verification token mismatch", 403
    return "Hello world", 200

@app.route('/', methods=['POST'])
def on_message_receive():
    data = request.get_json()
    log(data)
    if data["object"] == "page":
        for entry in data["entry"]:
            for messaging_event in entry["messaging"]:
                if messaging_event.get("message"):
                    handle_message(messaging_event)
    return "ok", 200

def handle_message(event):
    sender_id = event["sender"]["id"]
    message_text = event["message"]["text"]
    answer = interpret(sender_id, message_text)
    send_message(sender_id, answer)

def send_message(recipient_id, message_text):
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
    r = requests.post(REPLY_ENDPOINT, params=params, headers=headers, data=data)
    if r.status_code != 200:
        log(r.status_code)
        log(r.text)

def log(msg, *args, **kwargs):
    pass
    """
    try:
        if type(msg) is dict:
            msg = json.dumps(msg)
        else:
            msg = msg.format(*args, **kwargs)
        print(msg)
    except UnicodeEncodeError:
        pass
    sys.stdout.flush()
    """


if __name__ == '__main__':
    app.run(debug=True)
