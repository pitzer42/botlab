from random import choice
from botlab.config import DEFAULT_ANSWERS, CONVERSATION_STARTERS, SENTIMENT_THRESHOLD, SUGGEST_MENU
from botlab.nlp import topics_from_text
from botlab.url_provider import url_for
from botlab.storage import Storage

def know_your_customer(sender, topics):
    return choice(CONVERSATION_STARTERS)

def suggest_products(sender, topics):
    answer = ''
    for topic in topics:
        url = url_for(topic.key)
        if url:
            answer += url + '\n\n'
        return answer

interaction_strategy_map ={
    'KYC':know_your_customer,
    'SUG':suggest_products
}

class StrategySelector:

    def __init__(self):
        self.storage = Storage()

    def average_sentiment(self, topics):
        count = len(topics)
        total = 0
        for topic in topics:
            total += topic.sentiment
        return total/count

    def use_strategy(self, client_id, topics):
        key = self.storage.get_interaction_strategy(client_id)
        strategy = interaction_strategy_map.get(key)
        if strategy:
            return strategy(client_id, topics)
        return know_your_customer(client_id, topics)

    def reply(self, client_id, message):
        topics = topics_from_text(message)
        self.storage.save_topics(client_id, topics)
        if len(topics) == 0:
            return choice(DEFAULT_ANSWERS)
        answer = self.use_strategy(client_id, topics)
        self.storage.close()
        if self.average_sentiment(topics) < SENTIMENT_THRESHOLD:
            answer += '\n\n' + SUGGEST_MENU
        return answer

    def on_postback(self, client_id, payload):
        storage.save_interaction_strategy(client_id, payload)
        storage.close()
