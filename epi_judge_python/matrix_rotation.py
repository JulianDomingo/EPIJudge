from test_framework import generic_test


def rotate_matrix(square_matrix):
	n = len(square_matrix)

	for i in range(n // 2):
		for j in range(n - n // 2):
		# We do below until row (or col) index is > n // 2
		# [~j] is equivalent to [n - 1 - j]
			tmp = square_matrix[i][j]
			square_matrix[i][j] = square_matrix[~j][i]
			square_matrix[~j][i] = square_matrix[~i][~j]
			square_matrix[~i][~j] = square_matrix[j][~i]
			square_matrix[j][~i] = tmp

	return


def rotate_matrix_wrapper(square_matrix):
	rotate_matrix(square_matrix)
	return square_matrix


if __name__ == '__main__':
	exit(
		generic_test.generic_test_main("matrix_rotation.py",
									   'matrix_rotation.tsv',
									   rotate_matrix_wrapper))
