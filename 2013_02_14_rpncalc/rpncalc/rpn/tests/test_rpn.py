from __future__ import division
import unittest
from rpn import RPNCalc

class TestRPN(unittest.TestCase):

	def setUp(self):
		self.calc = RPNCalc()

	def test_add_2(self):
		self.assertEqual(self.calc.eval('2 2 +'), 2+2) 
		self.assertEqual(self.calc.eval('2 3 +'), 2+3)

	def test_multiple_var(self):
		self.assertEqual(self.calc.eval('5 3 8 + -'), -6)

	def test_add_3(self):
		self.assertEqual(self.calc.eval('2 3 + 2 +'), 2+3+2)

	def test_sub(self):
		self.assertEqual(self.calc.eval('3 2 -'), 3-2)

	def test_mul(self):
		self.assertEqual(self.calc.eval('3 2 *'), 3*2)

	def test_div(self):
		self.assertEqual(self.calc.eval('4 2 /'), 4/2)
	
	def test_inf(self):
		self.assertEqual(self.calc.eval('+inf -inf -'), float("+inf"))

	def test_negative(self):
		self.assertEqual(self.calc.eval('-20 2 +'), -20+2)

	def test_final(self):
		expr = '3 2 / 1.5 + 2 - 4 *'
		self.assertEqual(self.calc.eval(expr), ((((3/2)+1.5)-2)*4))

	def test_not_implemented(self):
		with self.assertRaises(NotImplementedError):
		    self.calc.eval('3 2 @')

if __name__ == "__main__":
	unittest.main()