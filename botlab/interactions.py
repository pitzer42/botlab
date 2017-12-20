from random import choice
from botlab.config import DEFAULT_ANSWERS, CONVERSATION_STARTERS, SENTIMENT_THRESHOLD, SUGGEST_MENU
from botlab.nlp import topics_from_text
from botlab.url_provider import url_for
from botlab.storage import Storage

def know_your_customer(sender, topics):
    print('KYC')
    return choice(CONVERSATION_STARTERS)

def suggest_products(sender, topics):
    print('SUGGESTIONS')
    answer = ''
    for topic in topics:
        url = url_for(topic.key)
        if url:
            answer += url + '\n\n'
        return answer

reply_strategy = know_your_customer

class StrategySelector:

    def average_sentiment(self, topics):
        count = len(topics)
        total = 0
        for topic in topics:
            total += topic.sentiment
        return total/count

    def reply(self, client_id, message):
        topics = topics_from_text(message)
        if len(topics) == 0:
            return choice(DEFAULT_ANSWERS)
        storage = Storage()
        storage.save_topics(client_id, topics)
        storage.close()
        answer = reply_strategy(client_id, topics)
        if self.average_sentiment(topics) < SENTIMENT_THRESHOLD:
            answer += '\n\n' + SUGGEST_MENU
        return answer

    def on_postback(self, client_id, payload):
        print('change interaction strategy ' + payload)
        if payload == 'SUGGESTIONS':
            reply_strategy = suggest_products
        else:
            reply_strategy = know_your_customer
