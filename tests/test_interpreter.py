import unittest
from interpreter import tokenize, tag, identify_products, interpret

class SmokeTest(unittest.TestCase):

    def _products_from_text(sef, text):
        return identify_products(tag(tokenize(text)))

    def _test_product_quantity_per_text(self, text, expectedQuantity):
        quantity = len(self._products_from_text(text))
        self.assertEqual(quantity, expectedQuantity)

    def test_identify_products(self):
        self._test_product_quantity_per_text('quero comprar um tênis vans azul, um notebook novo e um quadro branco, grande e novo', 3)
        self._test_product_quantity_per_text('quero um pastel', 1)
        self._test_product_quantity_per_text('sim', 0)

        self._test_attributes_per_product('quero comprar um tênis vans azul', 2)

        print(interpret('tester', 'sim'))



    def _test_attributes_per_product(self, text, expectedQuantity):
        products = self._products_from_text(text)
        quantity = len(products[0].attributes)
        self.assertEqual(quantity, expectedQuantity)
