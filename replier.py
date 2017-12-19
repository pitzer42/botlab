from config import DEFAULT_ANSWERS
from random import choice
from url_provider import url_for
from nlp import products_from_text

def reply(sender, message):
	products = products_from_text(message)
	answer = ''
	for product in products:
		url = url_for(product)
		if url:
			answer += url + '\n\n'
	return answer if answer != '' else random_answer()

def random_answer():
	return choice(DEFAULT_ANSWERS)
