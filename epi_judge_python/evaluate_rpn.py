from test_framework import generic_test


def compute(op1, op2, operator):
	if operator == '-':
		return op2 - op1
	elif operator == '+':
		return op1 + op2
	elif operator == '*':
		return op1 * op2
	else:
		# operator == '/'
		return op2 // op1


def evaluate(expression):
	# Most parsing questions involve using a stack (i.e. polish notation,
	# valid parentheses, etc.)
	ops = expression.split(',')
	stack = list()

	for op in ops:
		# Assumes valid RPN expression
		if op == '+' or op == '-' or op == '*' or op == '/':
			# Pop 2
			op1, op2 = stack.pop(), stack.pop()
			stack.append(compute(op1, op2, op))
		else:
			stack.append(int(op))

	return stack[0]


if __name__ == '__main__':
	exit(
		generic_test.generic_test_main("evaluate_rpn.py", 'evaluate_rpn.tsv',
									   evaluate))
