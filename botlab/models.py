from datetime import datetime

class Topic:

    def __init__(self, key, attributes, sentiment):
        self.datetime = str(datetime.now())
        self.key = key
        self.attributes = attributes
        self.sentiment = sentiment

    def __str__(self):
        return str(self.__dict__)
