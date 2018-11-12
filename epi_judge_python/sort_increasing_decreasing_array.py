from test_framework import generic_test
import heapq


def sort_k_increasing_decreasing_array(A):
	# Can optimize to O(N*log(K)) by reversing the decreasing partitions
	# into increasing partitions, leaving you with 'k' total increasing sublists.
	# By inserting one element from each of the k sublists, we can output a
	# ascending order resultant list == len(A) by maintaining a O(K) size min
	# heap.
	min_heap_k = []

	# Decompose A into sorted sublists
	sorted_sublists = []

	start_idx = 0
	INC, DEC = range(2)
	cur_type = INC

	for i in range(1, len(A) + 1):
		if (i == len(A) or # A ended, adds last subarray
			(A[i - 1] < A[i] and cur_type == DEC) or
			(A[i - 1] >= A[i] and cur_type == INC)):
			sorted_sublists.append(A[start_idx:i] if cur_type == INC else
								   A[i - 1:start_idx - 1:-1])

			# Update start_idx
			start_idx = i
			cur_type = INC if cur_type == DEC else DEC


	return list(heapq.merge(*sorted_sublists))


if __name__ == '__main__':
	exit(
		generic_test.generic_test_main("sort_increasing_decreasing_array.py",
									   'sort_increasing_decreasing_array.tsv',
									   sort_k_increasing_decreasing_array))
