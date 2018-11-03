import collections
import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def even_odd(A):
	# Partition the array into an even and odd partition, each starting from the
	# start and end of the array respectively.
	next_even, next_odd = 0, len(A) - 1

	while next_even < next_odd:
		# If next_even elem is not even, it belongs to the odd portion.
		if A[next_even] & 1:
			A[next_even], A[next_odd] = A[next_odd], A[next_even]
			# Increase odd partition size
			next_odd -= 1

		else:
			# Correctly even, just increase even partition size
			next_even += 1

	# Which condition you check for is arbitrary
	# while next_even < next_odd:
		# if A[next_odd] & 1:
			# next_odd -= 1
		# else:
			# A[next_even], A[next_odd] = A[next_odd], A[next_even]
			# next_even += 1

	return


@enable_executor_hook
def even_odd_wrapper(executor, A):
	before = collections.Counter(A)

	executor.run(functools.partial(even_odd, A))

	in_odd = False
	for a in A:
		if a % 2 == 0:
			if in_odd:
				raise TestFailure("Even elements appear in odd part")
		else:
			in_odd = True
	after = collections.Counter(A)
	if before != after:
		raise TestFailure("Elements mismatch")


if __name__ == '__main__':
	exit(
		generic_test.generic_test_main("even_odd_array.py",
									   'even_odd_array.tsv', even_odd_wrapper))
