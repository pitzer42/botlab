'''
Inspirade by:
    http://flask.pocoo.org/docs/0.12/testing/
    https://blog.hartleybrody.com/fb-messenger-bot/
    http://www.inf.ufrgs.br/~viviane/rslp/index.htm
    https://github.com/EmilStenstrom/rippletagger/tree/master/rippletagger
'''
import json
import requests
import botlab.config as config
from flask import Flask, request
from botlab.interactions import StrategySelector

import sys

strategy = StrategySelector()

app = Flask(__name__)

@app.route('/', methods=['GET'])
def verify_token():
    if request.args.get('hub.mode') == 'subscribe' and request.args.get('hub.challenge'):
        if request.args.get('hub.verify_token') == config.FB_CHALLENGE:
            return request.args['hub.challenge'], 200
        return 'Verification token mismatch', 403
    return 'Hello world', 200

@app.route('/', methods=['POST'])
def on_message_receive():
    data = request.get_json()
    if data['object'] == 'page':
        for entry in data['entry']:
            for messaging_event in entry['messaging']:
                if messaging_event.get('message'):
                    handle_message(messaging_event)
                elif messaging_event.get('postback'):
                    handle_postback(messaging_event)
    return 'ok', 200

def handle_message(event):
    sender_id = event['sender']['id']
    message_text = event['message']['text']
    answer = strategy.reply(sender_id, message_text)
    send_message(sender_id, answer)

def handle_postback(event):
    sender_id = event['sender']['id']
    payload = event['postback']['payload']
    print('postback ' + payload)
    sys.stdout.flush()
    answer = strategy.on_postback(sender_id, payload)
    send_message(sender_id, answer)

def send_message(recipient_id, message_text):
    params = {
        'access_token': config.FB_ACCESS_TOKEN
    }
    headers = {
        'Content-Type': 'application/json'
    }
    data = json.dumps({
        'recipient': {
            'id': recipient_id
        },
        'message': {
            'text': message_text
        }
    })
    r = requests.post(config.REPLY_ENDPOINT, params=params, headers=headers, data=data)
    if r.status_code != 200:
        print(r.status_code)
        print(r.text)

def send_button(recipient_id, message_text):
    params = {
        'access_token': config.FB_ACCESS_TOKEN
    }
    headers = {
        'Content-Type': 'application/json'
    }
    data = json.dumps({
        'recipient': {
            'id': recipient_id
        },
        'message': {
            'attachment':{
              'type':'template',
              'payload':{
                'template_type':'button',
                'text':'What do you want to do next?',
                'buttons':[
                  {
                    'type':'web_url',
                    'url':'https://www.messenger.com',
                    'title':'Visit Messenger'
                  }
                  ]}}}

    })
    r = requests.post(config.REPLY_ENDPOINT, params=params, headers=headers, data=data)
    if r.status_code != 200:
        print(r.status_code)
        print(r.text)

if __name__ == '__main__':
    app.run(debug=True)
