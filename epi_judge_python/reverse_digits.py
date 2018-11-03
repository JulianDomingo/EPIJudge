from test_framework import generic_test


def reverse(x):
	is_neg = x < 0
	res = 0

	x = abs(x)

	while x:
		res, x = (res * 10) + x % 10, x // 10

	return res if not is_neg else -res


if __name__ == '__main__':
	exit(
		generic_test.generic_test_main("reverse_digits.py",
									   'reverse_digits.tsv', reverse))
