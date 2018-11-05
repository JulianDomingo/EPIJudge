from test_framework import generic_test


def matrix_in_spiral_order(square_matrix):
	# Right is R0C0, R0C1, ... R0Cn-1
	# Down is R1Cn-1, R2Cn-1, ... Rn-1Cn-1
	# Left is Rn-1Cn-1, Rn-1Cn-2, ... Rn-1C0
	# Up is Rn-1C0, Rn-2C0, ... R0C0

	# We keep doing above steps, stopping when you reach the boundary of the
	# matrix or you find a None type (we clobber already seen values)

	# From left to right, determines the next traversal point
	SHIFT = [(0, 1), (1, 0), (0, -1), (-1, 0)]
	shift_idx = x = y = 0

	ordering = []
	n = len(square_matrix)

	for i in range(n**2):
		ordering.append(square_matrix[x][y])

		# Mark cell as visited
		square_matrix[x][y] = None

		# Go to next traversal coordinate
		next_x, next_y = x + SHIFT[shift_idx][0], y + SHIFT[shift_idx][1]

		# If reached boundary of grid or already traversed upcoming cell,
		# switch to the next traversal direction
		if (next_x not in range(n) or
			next_y not in range(n) or
			not square_matrix[next_x][next_y]):

			# Set new direction. "& 3" to rotate back to initial direction
			shift_idx = (shift_idx + 1) & 3
			next_x, next_y = x + SHIFT[shift_idx][0], y + SHIFT[shift_idx][1]

		x, y = next_x, next_y

	return ordering


if __name__ == '__main__':
	exit(
		generic_test.generic_test_main("spiral_ordering_segments.py",
									   "spiral_ordering_segments.tsv",
									   matrix_in_spiral_order))
