from test_framework import generic_test
from test_framework.test_failure import TestFailure


class Stack:
	def __init__(self):
		self.s = []

	def empty(self):
		return not len(self.s)

	def max(self):
		return self.s[-1][1] if self.s else float('-inf')

	def pop(self):
		return self.s.pop()[0] if len(self.s) > 0 else float('-inf')

	def push(self, x):
		# Push a tuple pairing of value and current max
		self.s.append((x, max(x, self.max())))


def stack_tester(ops):
	try:
		s = Stack()

		for (op, arg) in ops:
			if op == 'Stack':
				s = Stack()
			elif op == 'push':
				s.push(arg)
			elif op == 'pop':
				result = s.pop()
				if result != arg:
					raise TestFailure(
						"Pop: expected " + str(arg) + ", got " + str(result))
			elif op == 'max':
				result = s.max()
				if result != arg:
					raise TestFailure(
						"Max: expected " + str(arg) + ", got " + str(result))
			elif op == 'empty':
				result = int(s.empty())
				if result != arg:
					raise TestFailure(
						"Empty: expected " + str(arg) + ", got " + str(result))
			else:
				raise RuntimeError("Unsupported stack operation: " + op)
	except IndexError:
		raise TestFailure('Unexpected IndexError exception')


if __name__ == '__main__':
	exit(
		generic_test.generic_test_main("stack_with_max.py",
									   'stack_with_max.tsv', stack_tester))
