#Inspirade by https://blog.hartleybrody.com/fb-messenger-bot/

import requests
from flask import Flask, request
app = Flask(__name__)

@app.route("/")
def index():
    return "ok ok", 200

@app.route('/', methods=['GET'])
def verify():
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == os.environ["VERIFY_TOKEN"]:
            return "Verification token mismatch", 403
        return request.args["hub.challenge"], 200
    return "ok ok", 200

if __name__ == "__main__":
    app.run()
