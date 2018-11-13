from test_framework import generic_test


def search_first_of_k(A, k):
	# Do regular binary search, but keep continuously updating the result every
	# time you half the input size if the midpoint is still the value 'k' that
	# I'm looking for.
	first_idx = -1
	s, e = 0, len(A) - 1

	# 0, 1, 2, 3, 4, 5, 6, 7

	while s <= e:
		mid = (s + e) // 2

		if A[mid] == k:
			first_idx = mid
			e = mid - 1
		elif A[mid] < k:
			s = mid + 1
		else:
			# A[mid] > k
			e = mid - 1

	return first_idx


if __name__ == '__main__':
	exit(
		generic_test.generic_test_main(
			"search_first_key.py", 'search_first_key.tsv', search_first_of_k))
