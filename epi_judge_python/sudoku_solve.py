import itertools
import copy
import functools
import math

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def solve_sudoku(partial_assignment):
	# Test 1-9 inclusive for an uninitialized cell. If placement is valid,
	# recurse to next cell. Otherwise, try the other 8 numbers
	n = len(partial_assignment)
	solved = False

	def solver(row, col):
		if row == n:
			# Go to next column
			row, col = 0, col + 1
			if col == n:
				# Reached last square, since we know we're given a valid board, can
				# simply stop here.
				return True

		# Skip uninitialized cells
		if not partial_assignment[row][col]:
			return solver(row + 1, col)

		# Checks whether placement of a number is valid.
		def is_valid(row, col, val):
			# Check row duplicates
			if any(val == partial_assignment[idx][col]
					for idx in range(n)):
				return False

			# Check col duplicates
			if any(val == partial_assignment[row][idx]
					for idx in range(n)):
				return False

			# Check current subgrid - only need to check current since we are
			# given a valid partially complete sudoku
			subgrid_size = int(math.sqrt(n))
			row_subgrid_ofs = row // subgrid_size
			col_subgrid_ofs = col // subgrid_size

			return not any(
				val ==
				partial_assignment[subgrid_size * row_subgrid_ofs + a]\
									[subgrid_size * col_subgrid_ofs + b]
				for a, b in itertools.product(range(subgrid_size), repeat=2)
			)


		for num in range(1, n + 1):
			if is_valid(row, col, num):
				partial_assignment[row][col] = num
				if solver(row + 1, col):
					return True

		# Undo assignment
		partial_assignment[row][col] = 0
		return False

	return solver(0, 0)


def assert_unique_seq(seq):
	seen = set()
	for x in seq:
		if x == 0:
			raise TestFailure('Cell left uninitialized')
		if x < 0 or x > len(seq):
			raise TestFailure('Cell value out of range')
		if x in seen:
			raise TestFailure('Duplicate value in section')
		seen.add(x)


def gather_square_block(data, block_size, n):
	block_x = (n % block_size) * block_size
	block_y = (n // block_size) * block_size

	return [
		data[block_x + i][block_y + j] for j in range(block_size)
		for i in range(block_size)
	]


@enable_executor_hook
def solve_sudoku_wrapper(executor, partial_assignment):
	solved = copy.deepcopy(partial_assignment)

	executor.run(functools.partial(solve_sudoku, solved))

	if len(partial_assignment) != len(solved):
		raise TestFailure('Initial cell assignment has been changed')

	for (br, sr) in zip(partial_assignment, solved):
		if len(br) != len(sr):
			raise TestFailure('Initial cell assignment has been changed')
		for (bcell, scell) in zip(br, sr):
			if bcell != 0 and bcell != scell:
				raise TestFailure('Initial cell assignment has been changed')

	block_size = int(math.sqrt(len(solved)))

	for i in range(len(solved)):
		assert_unique_seq(solved[i])
		assert_unique_seq([row[i] for row in solved])
		assert_unique_seq(gather_square_block(solved, block_size, i))


if __name__ == '__main__':
	exit(
		generic_test.generic_test_main("sudoku_solve.py", 'sudoku_solve.tsv',
									   solve_sudoku_wrapper))
