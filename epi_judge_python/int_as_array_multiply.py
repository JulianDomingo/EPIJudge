from test_framework import generic_test


def multiply(num1, num2):
	# **ASSSUMES POSSIBILITY OF INTEGER OVERFLOW**
	# TODO: Write grade-school multiplication of partial products
	# This is now O(M * N), where M is the length of the partial product (at
	# most N - 1, and N is the length of the partial product digits)



	# **ASSUMES NO INTEGER OVERFLOW**
	# O(N) time and space
	# Convert to decimal notation
	i1, i2 = int_rep(num1), int_rep(num2)

	if not i1 or not i2:
		return [0]

	# Do native multiplication
	res = i1 * i2

	# Convert back to list representation
	resl = list_rep(res)

	return resl


def int_rep(l):
	res, mult = 0, 1

	is_neg = l[0] < 0

	if is_neg:
		l[0] *= -1

	for num in reversed(l):
		res, mult = res + (num * mult), mult * 10

	return -res if is_neg else res


def list_rep(x):
	resl = []
	is_neg = x < 0
	x = abs(x)

	while x:
		resl.insert(0, x % 10)
		x //= 10

	if is_neg:
		resl[0] *= -1

	return resl


if __name__ == '__main__':
	exit(
		generic_test.generic_test_main("int_as_array_multiply.py",
									   'int_as_array_multiply.tsv', multiply))
