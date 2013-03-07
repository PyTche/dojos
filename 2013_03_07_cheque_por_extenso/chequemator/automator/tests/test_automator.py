import unittest
from automator import Automator

class TestAutomator(unittest.TestCase):
	
	def setUp(self):
		self.auto = Automator()
		
	def test_menor_de_dez(self):
		self.assertEqual(self.auto.translate(5),'cinco')
	
	def test_dezena(self):
		self.assertEqual(self.auto.translate(15),'quinze')
		