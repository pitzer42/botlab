from pymongo import MongoClient
from botlab.config import DB_URI

class Storage:

    def __init__(self, uri=DB_URI, sandbox=False):
        self._sandbox = sandbox
        self._connection = MongoClient(uri)
        if sandbox:
            self.clients = self._connection.botlab_db.test_clients
            self.clients.delete_many({}) #clear sandbox for a new test
        else:
            self.clients = self._connection.botlab_db.clients

    def save_topics(self, client_id, topics):
        if len(topics) == 0:
            return
        client_interests = {}
        topics_dicts = [t.__dict__ for t in topics]
        self.clients.update_one({'client_id':client_id}, \
        {'$push': {'topics' : {'$each': topics_dicts}}}, \
        upsert=True)

    def close(self):
        self._connection.close()
