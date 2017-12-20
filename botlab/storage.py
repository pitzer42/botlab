from pymongo import MongoClient
from botlab.config import DB_URI, SANDBOX

class Storage:

    def __init__(self, uri=DB_URI):
        self._connection = MongoClient(uri)
        if SANDBOX:
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

    def close(self):
        self._connection.close()
