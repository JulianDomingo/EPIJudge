import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

RED, WHITE, BLUE = range(3)


def dutch_flag_partition(pivot_index, A):
	# O(N) time, O(1) space
	# pivot_value = A[pivot_index]

	# lt_pivot_idx, gt_pivot_idx = 0, len(A) - 1

	# for i in range(len(A)):
		# if A[i] < pivot_value:
			# A[i], A[lt_pivot_idx] = A[lt_pivot_idx], A[i]
			# lt_pivot_idx += 1

	# for j in reversed(range(len(A))):
		# if A[j] > pivot_value:
			# A[j], A[gt_pivot_idx] = A[gt_pivot_idx], A[j]
			# gt_pivot_idx -= 1

	# O(N) time, single pass through (lt pivot, eq pivot, and gt pivot partitions)
	pv = A[pivot_index]
	lt_pvt, eq_pvt, gt_pvt = 0, 0, len(A)

	# Since the eq_pvt partition is in between the lt_pvt and gt_pvt partition
	while eq_pvt < gt_pvt:
		# 'eq_pvt' is our index iterator ("unclassified")
		if A[eq_pvt] < pv:
			A[eq_pvt], A[lt_pvt] = A[lt_pvt], A[eq_pvt]
			lt_pvt, eq_pvt = lt_pvt + 1, eq_pvt + 1

		elif A[eq_pvt] == pv:
			eq_pvt += 1

		else:
			# A[eq_pvt] > pv
			gt_pvt -= 1
			A[eq_pvt], A[gt_pvt] = A[gt_pvt], A[eq_pvt]

	return


@enable_executor_hook
def dutch_flag_partition_wrapper(executor, A, pivot_idx):
	count = [0, 0, 0]
	for x in A:
		count[x] += 1
	pivot = A[pivot_idx]

	executor.run(functools.partial(dutch_flag_partition, pivot_idx, A))

	i = 0
	while i < len(A) and A[i] < pivot:
		count[A[i]] -= 1
		i += 1
	while i < len(A) and A[i] == pivot:
		count[A[i]] -= 1
		i += 1
	while i < len(A) and A[i] > pivot:
		count[A[i]] -= 1
		i += 1

	if i != len(A):
		raise TestFailure('Not partitioned after {}th element'.format(i))
	elif any(count):
		raise TestFailure("Some elements are missing from original array")


if __name__ == '__main__':
	exit(
		generic_test.generic_test_main("dutch_national_flag.py",
									   'dutch_national_flag.tsv',
									   dutch_flag_partition_wrapper))
