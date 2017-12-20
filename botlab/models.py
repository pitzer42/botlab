from datetime import datetime

class Topic:

    def __init__(self, key, attributes, sentiment):
        self.datetime = str(datetime.now())
        self.key = key
        self.attributes = attributes
        self.sentiment = sentiment

    def __str__(self):
        len_attributes = len(self.attributes)
        if(len_attributes == 0):
            return self.key
        if(len_attributes == 1):
            return self.key + ' ' + self.attributes[0]
        if(len_attributes == 2):
            return self.key + ' ' +  ' e '.join(self.attributes)
        return self.key + ' ' +  ', '.join(self.attributes[:-1]) + ' e ' + self.attributes[-1]
