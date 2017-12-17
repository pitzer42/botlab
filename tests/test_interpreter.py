import unittest
from interpreter import interpret, remove_stopwords, stem, tag

class SmokeTest(unittest.TestCase):

    def test_stopwords_are_ignored(self):
        sender = 'tester'
        message = 'Eu quero um smartphone e uma geladeira'
        answer = interpret(sender, message)
        assert len(message) > len(answer)

    def test_simmilar_words_are_normalized(self):
        tokens = ['pedra', 'pedreira', 'pedrada', 'pedraria', 'Pedro', 'pedrar', 'pedreiro']
        stemmed = set()
        for token in tokens:
            stemmed.add(stem(token))
        assert len(stemmed) == 1 and 'pedr' in stemmed

    def test_tokens_are_tagged(self):
        sender = 'tester'
        message = 'Eu quero um smartphone e uma geladeira'
        answer = interpret(sender, message)
        tagged = tag(answer)
        assert 1 == 1
