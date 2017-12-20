from random import choice
from botlab.config import DEFAULT_ANSWERS
from botlab.url_provider import url_for
from botlab.nlp import topics_from_text
from botlab.storage import Storage

def reply(sender, message):
	topics = topics_from_text(message)
	storage = Storage()
	storage.save_topics(sender, topics)
	storage.close()
	answer = ''
	for topic in topics:
		url = url_for(topic.key)
		if url:
			answer += url + '\n\n'
	return answer if answer != '' else random_answer()

def random_answer():
	return choice(DEFAULT_ANSWERS)
