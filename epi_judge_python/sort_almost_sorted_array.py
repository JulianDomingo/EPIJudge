from test_framework import generic_test
import heapq
import itertools


def sort_approximately_sorted_array(sequence, k):
	# Because the sequence property was specified to have all elements be
	# at most K indices away from its proper place, if we add (k + 1) elements
	# to the heap, we know the minimum from this heap must be GLOBALLY the
	# smallest element in the entire list because of the sequence invariant
	# given to us.
	res = []
	min_heap = []

	# [3, -1, 2, 6, 4, 5, 8], k = 2
	# [-1, 2, 3, 4, 5, 6, 8]

	# Add the first k + 1 elements
	for x in itertools.islice(sequence, k):
		heapq.heappush(min_heap, x)

	# Add remaining elements from sequence, making sure to also pop from the
	# min heap to ensure heap size stays at size k + 1.
	for x in sequence:
		res.append(heapq.heappushpop(min_heap, x))

	# Add last k + 1 elements in min_heap to result in the order needed
	while min_heap:
		res.append(heapq.heappop(min_heap))

	return res



def sort_approximately_sorted_array_wrapper(sequence, k):
	return sort_approximately_sorted_array(iter(sequence), k)


if __name__ == '__main__':
	exit(
		generic_test.generic_test_main(
			"sort_almost_sorted_array.py", 'sort_almost_sorted_array.tsv',
			sort_approximately_sorted_array_wrapper))
