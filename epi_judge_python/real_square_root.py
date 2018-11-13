from test_framework import generic_test
import math


def square_root(x):
	# Account for values of x < 1.0
	s, e = (1.0, x) if x >= 1.0 else (x, 1.0)

	# Keep searching until s and e are very close to each other, at which point
	# you know it's the square_root
	while not math.isclose(s, e):
		mid = (s + e) * 0.5

		if mid * mid <= x:
			s = mid
		else:
			# mid * mid > x
			e = mid

	return s


if __name__ == '__main__':
	exit(
		generic_test.generic_test_main("real_square_root.py",
									   'real_square_root.tsv', square_root))
