from test_framework import generic_test


def is_palindrome_number(x):
	# The negative sign never appears before a digit, so negative values can
	# never be palindromic
	if x < 0:
		return False

	# Reverse digit and compare whether original x is == reversed
	tmp_x = x
	rev = 0

	while tmp_x:
		rev, tmp_x = (rev * 10) + tmp_x % 10, tmp_x // 10

	return rev == x


if __name__ == '__main__':
	exit(
		generic_test.generic_test_main("is_number_palindromic.py",
									   "is_number_palindromic.tsv",
									   is_palindrome_number))
