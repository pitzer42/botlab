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

    def save_interests(self, client_id, interest_items):
        if len(interest_items) == 0:
            return
        client_interests = {}
        interest_items = [i.__dict__ for i in interest_items]
        self.clients.update_one({'client_id':client_id}, \
        {'$push': {'interests' : {'$each': interest_items}}}, \
        upsert=True)

    def close(self):
        self._connection.close()
