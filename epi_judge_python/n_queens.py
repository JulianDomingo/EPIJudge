from test_framework import generic_test


def n_queens(n):
	def helper(row):
		if row == n:
			# Able to place n queens without backtracking. Add result to
			# solution set
			res.append(list(col_placement))
		else:
			# Check all possible cells for the nth queen in current column
			for col in range(n):
				if all(
						# (row, col) is on the diagonal of a previously placed queen if
						# the absolute difference of the row/col values equate.
						abs(existing_col - col) != abs(row - idx) and
						# Furthermore, the queen cannot be placed on the same
						# row as a previously placed queen.
						abs(existing_col - col) != 0
						for idx, existing_col in enumerate(col_placement[:row])
				):
					col_placement[row] = col
					helper(row + 1)


	# We only need either row or column values to know what cells are
	# 'unrestrictive' since it's an nxn board. For example, if an existing
	# column we've placed a queen is 1, then the entirety of row 1 is also
	# restricted.
	col_placement = [0] * n
	res = []
	helper(0)
	return res


def comp(a, b):
	return sorted(a) == sorted(b)


if __name__ == '__main__':
	exit(
		generic_test.generic_test_main("n_queens.py", 'n_queens.tsv', n_queens,
									   comp))
