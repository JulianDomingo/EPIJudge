import copy
import functools
import math

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def solve_sudoku(partial_assignment):
	def has_duplicate(block):
		vals = list(filter(lambda x: x != 0, block))
		return len(vals) != len(set(vals))

	m = len(partial_assignment)
	n = len(partial_assignment[0])

	# Check for duplicates in rows and columns
	if any(
		has_duplicate([partial_assignment[row][col] for col in range(n)]) or
		has_duplicate([partial_assignment[col][row] for col in range(n)])
		for row in range(n)
	):
		return False

	# Check for duplicates in 3x3 subgrids
	subgrid_size = int(math.sqrt(n))

	return all(
		not has_duplicate([
			partial_assignment[row][col]
			for row in range(subgrid_size * i, subgrid_size * (i + 1))
			for col in range(subgrid_size + j, subgrid_size * (j + 1))
		])
		for i in range(m)
		for j in range(n)
	)


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
