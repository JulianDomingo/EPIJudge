from test_framework import generic_test
from test_framework.test_failure import TestFailure


def int_to_string(x):
	if x == 0:
		return '0'

	s = []

	is_neg = x < 0
	x = abs(x)

	# 123 -> "321"
	while x:
		# We know '0' is our base number, so we add the offset based on the ones
		# place digit
		s.append(chr(ord('0') + x % 10))
		x //= 10

	s = "".join(reversed(s))
	return "-" + s if is_neg else s


def string_to_int(s):
	import string

	is_neg = s[0] == '-'
	start = 1 if is_neg else 0

	res = 0

	# 13
	for i in range(start, len(s)):
		res *= 10
		res += string.digits.index(s[i])

	return -res if is_neg else res


def wrapper(x, s):
	if int_to_string(x) != s:
		raise TestFailure("Int to string conversion failed")
	if string_to_int(s) != x:
		raise TestFailure("String to int conversion failed")


if __name__ == '__main__':
	exit(
		generic_test.generic_test_main("string_integer_interconversion.py",
									   'string_integer_interconversion.tsv',
									   wrapper))
