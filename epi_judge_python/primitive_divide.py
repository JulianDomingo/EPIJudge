from test_framework import generic_test


def divide(x, y):
	res = 0

	while x >= y:
		subtract_this = y
		pow2 = 1
		while (subtract_this << 1) < x:
			subtract_this, pow2 = subtract_this << 1, pow2 << 1

		x -= subtract_this
		res += pow2

	return res


if __name__ == '__main__':
	exit(
		generic_test.generic_test_main("primitive_divide.py",
									   "primitive_divide.tsv", divide))
