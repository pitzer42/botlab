from pymongo import MongoClient
from botlab.config import DB_URI

class Storage:

    def __init__(self, uri=DB_URI, sandbox=False):
        self._sandbox = sandbox
        self._connection = MongoClient(uri)
        if sandbox:
            self.clients = self._connection.botlab_db.test_clients
        else:
            self.clients = self._connection.botlab_db.clients

    def save_interests(self, client_id, interest_items):
        client_interests = {}
        client_interests['client_id'] = client_id
        client_interests['interests'] = [i.__dict__ for i in interest_items]
        self.clients.insert_one(client_interests)

    def close(self):
        if self._sandbox:
            self.clients.delete_many({})
        self._connection.close()
