import unittest
from interpreter import interpret, tag

class SmokeTest(unittest.TestCase):

    def test_smoke(self):
        print(interpret('tester', 'quero comprar um tênis vans azul, um notebook novo e um quadro branco, grande e novo'))
        print(interpret('tester', ''))
