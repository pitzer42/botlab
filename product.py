class Product:
    def __init__(self, name, attributes):
        self.name = name
        self.attributes = attributes

    def __str__(self):
        len_attributes = len(self.attributes)
        if(len_attributes == 0):
            return self.name
        if(len_attributes == 1):
            return self.name + ' ' + self.attributes[0]
        if(len_attributes == 2):
            return self.name + ' ' +  ' e '.join(self.attributes)
        return self.name + ' ' +  ', '.join(self.attributes[:-1]) + ' e ' + self.attributes[-1]
