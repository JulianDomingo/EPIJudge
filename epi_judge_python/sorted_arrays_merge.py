from test_framework import generic_test
import heapq


def merge_sorted_arrays(sorted_arrays):
	# Pythonic solution
	# return list(merge(*sorted_arrays))

	# Create iterators for all k sorted sublists
	sorted_arrays_iter = [iter(x) for x in sorted_arrays]

	# O(k) where k is number of sorted sublists within sorted_arrays
	min_heap = []

	# Add the first element from the k sublists
	for i, sublist in enumerate(sorted_arrays_iter):
		# Prevent next() from raising StopIteration error
		val = next(sublist, None)
		if val is not None:
			heapq.heappush(min_heap, (val, i))

	# Keep going until no more elements to process in min_heap
	res = []

	while min_heap:
		smallest_k, smallest_k_idx = heapq.heappop(min_heap)
		smallest_k_iter = sorted_arrays_iter[smallest_k_idx]
		res.append(smallest_k)
		next_val = next(smallest_k_iter, None)

		# We still want to add values of '0' to heap! So specify explicitly that
		# we only don't add if it's not None type
		if next_val is not None:
			heapq.heappush(min_heap, (next_val, smallest_k_idx))

	return res


if __name__ == '__main__':
	exit(
		generic_test.generic_test_main("sorted_arrays_merge.py",
									   "sorted_arrays_merge.tsv",
									   merge_sorted_arrays))
