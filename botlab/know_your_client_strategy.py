from random import choice
from botlab.config import DEFAULT_ANSWERS
from botlab.url_provider import url_for
from botlab.nlp import products_from_text
from botlab.storage import Storage

class KnowYourClientStrategy:

    def greetings(self):
        return choice(['O que você achou do Iphone X?',
                        'Você tem assistido alguma série?',
                        'Bateu uma fome aqui... alguma sugestão?',
                        'Acho que estou precisando de umas férias.\nQual foi a sua última viagem?',
                        'O que você acha do cenário atual socioeconômico brasileiro?',
                        'Hj eu tô assim: https://scontent.fcpq1-1.fna.fbcdn.net/v/t1.0-9/25498382_2147912955433618_8826704789237580227_n.jpg?oh=2c842e11a51a67ac91b15f4d175de697&oe=5AC71B5D',
                        'Cachorros ou gatos?',
                        ' Bolacha ou biscoito?'])

    def reply(sender, message):
        topics = topics_from_text(message)
    	storage = Storage()
    	storage.save_topics(sender, topics)
    	storage.close()
    	return self.greetings()

"""
def reply(sender, message):
	products = products_from_text(message)
	storage = Storage()
	storage.save_interests(sender, products)
	storage.close()
	answer = ''
	for product in products:
		url = url_for(product.name)
		if url:
			answer += url + '\n\n'
	return answer if answer != '' else random_answer()

def random_answer():
	return choice(DEFAULT_ANSWERS)
    """
