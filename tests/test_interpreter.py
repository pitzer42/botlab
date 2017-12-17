import unittest
from interpreter import interpret, tag, identify_products

class SmokeTest(unittest.TestCase):

    def test_tokens_are_tagged(self):
        sender = 'tester'
        message = 'Eu quero um smartphone e uma geladeira'
        answer = interpret(sender, message)
        tagged = tag(answer)
        assert 1 == 1

    def test_products_are_extract_from_text(self):
        tagged_tokens = [('Eu', 'PRON'), ('quero', 'VERB'), ('um', 'DET'),
        ('microondas', 'NOUN'), (',', 'PUNCT'), ('uma', 'DET'), ('geladeira', 'NOUN'),
        ('barata', 'ADJ'), ('e', 'CONJ'), ('um', 'DET'), ('smartphone', 'NOUN'),
        ('novo', 'ADJ'), ('e', 'CONJ'), ('com', 'ADP'), ('uma', 'DET'), ('boa', 'ADJ'),
        ('camera', 'VERB')]

        products = identify_products(tagged_tokens)
        assert products[0].name == 'microondas'
        assert len(products[0].attributes) == 0
