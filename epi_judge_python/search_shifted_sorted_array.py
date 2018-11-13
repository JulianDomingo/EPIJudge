from test_framework import generic_test


def search_smallest(A):
	s, e = 0, len(A) - 1

	while s < e:
		mid = (s + e) // 2

		if A[mid - 1] > A[mid] < A[mid + 1]:
			return mid
		elif A[mid] > A[e]:
			# Must reside within [mid + 1, n]
			s = mid + 1
		else:
			# A[mid] < A[n]
			# Must reside within [0, mid - 1]
			e = mid

	return s


if __name__ == '__main__':
	exit(
		generic_test.generic_test_main("search_shifted_sorted_array.py",
									   'search_shifted_sorted_array.tsv',
									   search_smallest))
