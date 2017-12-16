import unittest
from interpreter import interpret, remove_stopwords

class SmokeTest(unittest.TestCase):

    def test_stopwords_are_ignored(self):
        sender = 'tester'
        message = 'Eu quero um smartphone e uma geladeira'
        answer = interpret(sender, message)
        assert len(message) > len(answer)
