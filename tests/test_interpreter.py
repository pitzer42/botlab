import unittest
from interpreter import interpret, tag

class SmokeTest(unittest.TestCase):

    def test_smoke(self):
        try:
            print(interpret('tester', 'quero comprar um tênis vans azul, um notebook novo e um quadro branco, grande e novo'))
            print(interpret('tester', ''))
            print(interpret('tester', 'sim'))
        except:
            print("FAIÔ")
