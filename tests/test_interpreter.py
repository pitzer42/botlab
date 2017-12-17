import unittest
from interpreter import interpret, tag
from product_identifier import ProductIdentifier

class SmokeTest(unittest.TestCase):

    def test_products_are_extract_from_text(self):
        tagged_tokens = [('Eu', 'PRON'), ('quero', 'VERB'), ('um', 'DET'),
        ('microondas', 'NOUN'), (',', 'PUNCT'), ('uma', 'DET'), ('geladeira', 'NOUN'),
        ('barata', 'ADJ'), ('e', 'CONJ'), ('um', 'DET'), ('smartphone', 'NOUN'),
        ('novo', 'ADJ'), (',', 'PUNCT'), ('com', 'ADP'), ('uma', 'DET'), ('boa', 'ADJ'),
        ('camera', 'VERB'), ('e', 'CONJ'), ('branco', 'ADJ')]

        identifier = ProductIdentifier()
        products = identifier.identify_products(tagged_tokens)

        for product in products:
            print(product)

        assert len(products) > 0
        assert products[0].name == 'microondas'
        assert len(products[0].attributes) == 0
