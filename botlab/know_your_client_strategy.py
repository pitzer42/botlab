from random import choice, shuffle
from botlab.config import DEFAULT_ANSWERS
from botlab.config import CONVERSATION_STARTERS
from botlab.url_provider import url_for
from botlab.nlp import topics_from_text
from botlab.storage import Storage

class KnowYourClientStrategy:

    def __init__(self):
        self._answers = []

    def next_answer(self):
        if len(self._answers) == 0:
            self._answers = list(CONVERSATION_STARTERS)
            shuffle(self._answers)
        return self._answers.pop()

    def reply(self, sender, message):
        topics = topics_from_text(message)
        storage = Storage()
        storage.save_topics(sender, topics)
        storage.close()
        return self.next_answer()
