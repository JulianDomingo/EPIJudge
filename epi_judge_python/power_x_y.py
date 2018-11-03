from test_framework import generic_test


def power(x, y):
	res = 1.0

	if y < 0:
		# Just inverse x and make y positive
		x = (1 / x)
		y = abs(y)

	while y:
		if y & 1:
			# Isolate odd portion before dividing y
			res *= x

		# Keep squaring x until y reaches 1. By the time this happens, 'x'
		# contains the operand needed to multiply with res to get pow(x, y)
		x, y = x * x, y >> 1

	return res



if __name__ == '__main__':
	exit(
		generic_test.generic_test_main("power_x_y.py", 'power_x_y.tsv', power))
