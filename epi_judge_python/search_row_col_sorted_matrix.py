from test_framework import generic_test


def matrix_search(A, x):
	# Compare first value at row i to the last element at the same row.
	# If elem is > last element, can eliminate entire row i from consideration.
	# On the other hand, if elem < last element, can eliminate entire last
	# column. keep doing this until you find the value needed.
	# O(M + N)
	m, n = 0, len(A[0]) - 1

	while True:
		if m == len(A) or n < 0:
			return False
		elif A[m][n] == x:
			return True
		elif x < A[m][n]:
			n -= 1
		else:
			# x > A[m][n]
			m += 1

	return False


if __name__ == '__main__':
	exit(
		generic_test.generic_test_main("search_row_col_sorted_matrix.py",
									   'search_row_col_sorted_matrix.tsv',
									   matrix_search))
