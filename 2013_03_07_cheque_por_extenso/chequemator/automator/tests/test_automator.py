import unittest
from automator import Automator

class TestAutomator(unittest.TestCase):

    def setUp(self):
        self.auto = Automator()

    def test_menor_de_dez(self):
        self.assertEqual(self.auto.translate(5),'cinco')

    def test_11_19(self):
        self.assertEqual(self.auto.translate(15),'quinze')

    def test_dezena_2(self):
        self.assertEqual(self.auto.translate(53),'cinquenta e tres')
        self.assertEqual(self.auto.translate(87),'oitenta e sete')

    def test_centena(self):
        self.assertEqual(self.auto.translate(356),'trezentos e cinquenta e seis')

    def test_centena_11_19(self):
        self.assertEqual(self.auto.translate(519), 'quinhentos e dezenove')