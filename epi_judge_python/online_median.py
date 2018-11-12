from test_framework import generic_test
import heapq


def online_median(sequence):
	# Use min heap to store elements after median and max heap to store elements
	# before the median. Then, the root of each heap averaged out is the
	# median.
	# O(log(N)), where N is the size of the sequence for insertions

	min_h, max_h = [], []
	res = []

	store_min = True

	# 5, 4, 3, 2, 1
	# min: [5] max: []
	# min: [5] max: [4] => 4.5
	# min: [3, 5] max: [4] => 4

	for num in sequence:
		if store_min:
			heapq.heappush(min_h, num)
		else:
			heapq.heappush(max_h, -num)

		store_min = not store_min

		# Compute median
		if not max_h:
			res.append(min_h[0])
		elif len(max_h) == len(min_h):
			res.append((min_h[0] + (-max_h[0])) * 0.5)
		else:
			# Odd number of elements, return root of min_h
			res.append(max(-max_h[0], min_h[0]))

	return res


def online_median_wrapper(sequence):
	return online_median(iter(sequence))


if __name__ == '__main__':
	exit(
		generic_test.generic_test_main("online_median.py", "online_median.tsv",
									   online_median_wrapper))
