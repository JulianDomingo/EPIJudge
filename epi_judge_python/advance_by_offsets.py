from test_framework import generic_test


def can_reach_end(A):
	# If we keep track of the furthest index we can traverse to as you iterate
	# across the array, we know we can reach the end if A[len(A) - 2] is a value
	# that is >= dst index (A(len(A) - 1]) is the destination index, so we don't
	# count that).
	furthest_index = 0
	dst = len(A) - 1
	i = 0

	# Cannot continue if traversing index surpasses furthest_index, because this
	# means you can't go any further than furthest_index. If you keep traversing,
	# we are incorrectly assuming that the elements starting at index
	# furthest_index + 1 are reachable
	while i <= furthest_index and furthest_index < dst:
		furthest_index = max(furthest_index, A[i] + i)
		i += 1

	return furthest_index >= dst


if __name__ == '__main__':
	exit(
		generic_test.generic_test_main(
			"advance_by_offsets.py", "advance_by_offsets.tsv", can_reach_end))
