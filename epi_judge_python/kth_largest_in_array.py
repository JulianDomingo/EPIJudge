from test_framework import generic_test
import operator
import random


# The numbering starts from one, i.e., if A = [3, 1, -1, 2]
# find_kth_largest(1, A) returns 3, find_kth_largest(2, A) returns 2,
# find_kth_largest(3, A) returns 1, and find_kth_largest(4, A) returns -1.
def find_kth_largest(k, A):
	# Pick pivot arbitrarily. If there are exactly k - 1 elements larger than
	# the pivot, the pivot is the kth largest. If there are less than k - 1
	# elements larger than the pivot, we can discard all elements larger than
	# or equal to the pivot. Otherwise, we discard all elements less than
	# elements (greater than k - 1 elements)
	def kth_largest(comp):
		def partition_around_pivot(l, r, pivot_idx):
			pivot_val = A[pivot_idx]
			new_pivot = l
			A[pivot_idx], A[r] = A[r], A[pivot_idx]

			for i in range(l, r):
				if comp(A[i], pivot_val):
					A[i], A[new_pivot] = A[new_pivot], A[i]
					new_pivot += 1

			A[r], A[new_pivot] = A[new_pivot], A[r]
			return new_pivot

		l, r = 0, len(A) - 1

		while l <= r:
			pivot_idx = random.randint(l, r)
			new_pivot_idx = partition_around_pivot(l, r, pivot_idx)

			if new_pivot_idx == k - 1:
				return A[new_pivot_idx]
			elif new_pivot_idx > k - 1:
				r = new_pivot_idx - 1
			else:
				l = new_pivot_idx + 1

	return kth_largest(operator.gt)


if __name__ == '__main__':
	exit(
		generic_test.generic_test_main("kth_largest_in_array.py",
									   'kth_largest_in_array.tsv',
									   find_kth_largest))
