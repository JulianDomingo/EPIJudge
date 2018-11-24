import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

NUM_PEGS = 3


def compute_tower_hanoi(num_rings):
	def helper(rings_left, from_peg, to_peg, intermediate_peg):
		# 'intermediate_peg' is the peg used to temporarily store the n - 1
		# top rings before placing them on top of the largest ring.
		if rings_left > 0:
			# Recurse until you've reached the n -1th peg.
			helper(rings_left - 1, from_peg, intermediate_peg, to_peg)

			# Places peg to intermediary peg (after n - 1 calls of above,
			# when it recurses back 'to_peg' is currently 'intermediate_peg')
			pegs[to_peg].append(pegs[from_peg].pop())

			# Update steps taken
			steps.append([from_peg, to_peg])

			# Finally, place the top n - 1 pegs on top of the largest peg. This
			# will use the 'from_peg' / initial peg as the intermediary. This
			# is safe because the first time this is executed, all pegs from
			# peg 1 have already been moved out.
			helper(rings_left - 1, intermediate_peg, to_peg, from_peg)


	steps = []

	# Initialize list of 3 lists, with the first containing all rings and the
	# other n - 1 (2 total) initially being empty
	pegs = [list(reversed(range(1, num_rings + 1)))] + \
			[[] for _ in range(1, NUM_PEGS)]

	helper(num_rings, 0, 1, 2)
	return steps


@enable_executor_hook
def compute_tower_hanoi_wrapper(executor, num_rings):
	pegs = [list(reversed(range(1, num_rings + 1)))] + [[] for _ in range(
		1, NUM_PEGS)]

	result = executor.run(functools.partial(compute_tower_hanoi, num_rings))

	for from_peg, to_peg in result:
		if pegs[to_peg] and pegs[from_peg][-1] >= pegs[to_peg][-1]:
			raise TestFailure("Illegal move from {} to {}".format(
				pegs[from_peg][-1], pegs[to_peg][-1]))
		pegs[to_peg].append(pegs[from_peg].pop())
	expected_pegs1 = [[], [], list(reversed(range(1, num_rings + 1)))]
	expected_pegs2 = [[], list(reversed(range(1, num_rings + 1))), []]
	if pegs not in (expected_pegs1, expected_pegs2):
		raise TestFailure("Pegs doesn't place in the right configuration")


if __name__ == '__main__':
	exit(
		generic_test.generic_test_main("hanoi.py", 'hanoi.tsv',
									   compute_tower_hanoi_wrapper))
