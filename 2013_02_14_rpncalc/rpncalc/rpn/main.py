import operator


class RPNCalc(object):

	OPS = {
		'+' : operator.add,
		'-' : operator.sub,
		'*' : operator.mul,
		'/' : operator.div,
	}

	def __init__(self):
		self.stack = []
	
	def eval(self, expr):
		tokens = expr.split()
		for token in tokens:
			if token not in RPNCalc.OPS:
				try:
					value = float(token)
				except ValueError:
					raise NotImplementedError('Operator {} not'
						' implemented !'.format(token)) 
				self.stack.append(token)
			else:
				rhs, lhs = self.stack.pop(), self.stack.pop()
				op = RPNCalc.OPS[token]
				self.stack.append(op(float(lhs), float(rhs)))

		return self.stack.pop()