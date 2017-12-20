from random import choice
from botlab.config import DEFAULT_ANSWERS
from botlab.url_provider import url_for
from botlab.nlp import products_from_text
from botlab.storage import Storage

def reply(sender, message):
	products = products_from_text(message)
	storage = Storage()
	storage.save_interests(sender, products)
	storage.close()
	answer = ''
	for product in products:
		url = url_for(product)
		if url:
			answer += url + '\n\n'
	return answer if answer != '' else random_answer()

def random_answer():
	return choice(DEFAULT_ANSWERS)
