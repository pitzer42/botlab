from pymongo import MongoClient
from botlab.config import DB_URI, SANDBOX, DEFAULT_INTERACTION_STRATEGY

def _sandbox_mode():
    return __builtins__.get('sandbox')

class Storage:

    def __init__(self, uri=DB_URI):
        self._connection = MongoClient(uri)
        if _sandbox_mode():
            self.clients = self._connection.botlab_db.test_clients
            self.clients.delete_many({}) #clear sandbox for a new test
        else:
            self.clients = self._connection.botlab_db.clients

    def save_topics(self, client_id, topics):
        client_interests = {}
        topics_dicts = [t.__dict__ for t in topics]
        self.clients.update_one({'client_id':client_id}, \
        {'$push': {'topics' : {'$each': topics_dicts}}}, \
        upsert=True)

    def save_interaction_strategy(self, client_id, strategy):
        self.clients.update_one({'client_id':client_id}, \
        {'$set': {'strategy' : strategy}}, \
        upsert=True)

    def get_interaction_strategy(self, client_id):
        client = self.clients.find_one({'client_id':client_id})
        if client:
            strategy = client.get('strategy')
            if strategy:
                return strategy
        self.clients.update_one({'client_id':client_id}, \
        {'$set' : {'strategy': DEFAULT_INTERACTION_STRATEGY}}, upsert=True)
        return DEFAULT_INTERACTION_STRATEGY

    def close(self):
        self._connection.close()
