from test_framework import generic_test, test_utils
import heapq


def k_largest_in_binary_heap(A, k):
	# O(k * log(k)) time, O(k) space for heap
	i_am_left = False
	res, max_heap = [], []

	heapq.heappush(max_heap, (-A[0], 0))

	for _ in range(k):
		next_max, next_max_idx = heapq.heappop(max_heap)
		res.append(-next_max)

		# At most k nodes in heap
		left_child_idx = (2 * next_max_idx) + 1
		if (left_child_idx < len(A)):
			heapq.heappush(max_heap, (-A[left_child_idx], left_child_idx))

		right_child_idx = (2 * next_max_idx) + 2
		if (right_child_idx < len(A)):
			heapq.heappush(max_heap, (-A[right_child_idx], right_child_idx))

	return res


if __name__ == '__main__':
	exit(
		generic_test.generic_test_main(
			"k_largest_in_heap.py",
			"k_largest_in_heap.tsv",
			k_largest_in_binary_heap,
			comparator=test_utils.unordered_compare))
