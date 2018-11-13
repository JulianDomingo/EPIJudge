from test_framework import generic_test


def square_root(k):
	if k < 0:
		raise ValueError('Cannot take negative of square root!')

	s, e = 0, k // 2

	while s <= e:
		mid = (s + e) // 2

		if mid * mid <= k < (mid + 1) * (mid + 1):
			return mid
		elif mid * mid < k:
			s = mid + 1
		else:
			e = mid - 1

	return s


if __name__ == '__main__':
	exit(
		generic_test.generic_test_main("int_square_root.py",
									   "int_square_root.tsv", square_root))
