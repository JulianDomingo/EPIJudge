from test_framework import generic_test


def snake_string(s):
	# First print out peak of sinusoidal based on index of string, then 0, then
	# -1.
	# Hello World =>
	#
	#		e				-
	#
	#  H		l		o		W		r
	#
	#				l				o
	#
	#  0	1	2	3	4	5	6	7	8
	res = []

	PEAK_STEP_SIZE, REG_STEP_SIZE = 4, 2

	# "Hello World!"
	# Add peak hi characters
	for i in range(1, len(s), PEAK_STEP_SIZE):
		res.append(s[i])

	# Add 0 characters
	for i in range(0, len(s), REG_STEP_SIZE):
		res.append(s[i])

	# Add peak lo characters
	for i in range(3, len(s), PEAK_STEP_SIZE):
		res.append(s[i])

	return "".join(res)


if __name__ == '__main__':
	exit(
		generic_test.generic_test_main("snake_string.py", 'snake_string.tsv',
									   snake_string))
