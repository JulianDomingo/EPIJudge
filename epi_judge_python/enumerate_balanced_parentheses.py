from test_framework import generic_test, test_utils


def generate_balanced_parentheses(num_pairs):
	def compute(n, left, right, cur):
		if left == 0:
			# Fill rest with remaining closed parentheses
			enumeration = cur + (')' * (right))
			final.append(enumeration)
			return

		# Still have left parentheses left, try with adding '('
		compute(n, left - 1, right, cur + '(')

		# Also try adding ')' iff number of right parentheses is strictly more
		# than number of left parentheses
		# (If there's less closing parentheses left to add, adding a right
		# incorrectly will result in inbalanced parentheses)
		if right > left:
			compute(n, left, right - 1, cur + ')')

	final = []
	compute(num_pairs, num_pairs, num_pairs, '')
	return final


if __name__ == '__main__':
	exit(
		generic_test.generic_test_main("enumerate_balanced_parentheses.py",
									   'enumerate_balanced_parentheses.tsv',
									   generate_balanced_parentheses,
									   test_utils.unordered_compare))
