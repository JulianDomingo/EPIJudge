from test_framework import generic_test


def longest_contained_range(A):
	# Brute force! We don't need to have total ordering on the list. We simply
	# need to know whether there exists an adjacent element also present in the
	# list. So, we can use a hashtable with keys representing all existing
	# elements within A. We then do an expanding incremental search for keys
	# that are 1 off from the current value we're checking in A, adding 1 every
	# time we find a value that is of distance 1 to the current value in A we're
	# checking. We then DELETE these adjacent elements from the hashtable, and
	# stop once the hashtable is empty. This is O(n + m), where N is the size of
	# list A, and M is the total unique entries in the hash table. Since m < n,
	# this is essentially O(N). Spacewise, O(N) since we may need to store the
	# entire list A into the hashtable (if they are all unique elements).
	seen = set(A)
	longest = 0

	for num in A:
		if num not in seen:
			continue

		lt, gt = num - 1, num + 1
		# Account for current element 'num'
		cur_longest = 1

		while lt in seen or gt in seen:
			if lt in seen:
				cur_longest += 1
				seen.remove(lt)
				lt -= 1
			if gt in seen:
				cur_longest += 1
				seen.remove(gt)
				gt += 1

		longest = max(longest, cur_longest)

	return longest


	# 3, -2, 7, 9, 8, 1, 2, 0, -1, 5, 8
	# -2, -1, 0, 1, 2, 3, 5, 7, 8, 8, 9
	# Sort list and find largest subarray that has adjacent elements with
	# absolute difference of 1.
	# A.sort()
	# print('\n{}'.format(A))

	# start, longest = 0, 1

	# for end in range(1, len(A)):
		# if A[end] - A[end - 1] <= 1:
			# longest = max(longest, end - start + 1)
		# else:
			# # Start over
			# start = end

	# return max(longest, end - start + 1)


if __name__ == '__main__':
	exit(
		generic_test.generic_test_main("longest_contained_interval.py",
									   'longest_contained_interval.tsv',
									   longest_contained_range))
