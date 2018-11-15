from test_framework import generic_test
from collections import OrderedDict


# Test: f, s, f, e, t, w, e, n, w, e => {s, f, e, t, w}
#
def longest_subarray_with_distinct_entries(A):
	res = []
	start, longest = 0, 0
	seen = OrderedDict()

	for end, entry in enumerate(A):
		if entry not in seen:
			seen[entry] = end
		else:
			if longest < end - start:
				longest = end - start
				res = list(seen.keys())
			# Move start index to index AFTER the element 'entry' (so we can
			# add it to the set and find other subarrays)
			start = seen[entry] + 1

			# We need to delete from the hashtable all elements preceding the
			# occurrence of entry as well. However, there will only ever be
			# O(n) total deletions possible, so time complexity is still O(N).
			while True:
				# Pop least recently used
				popd = seen.popitem(last=False)
				if popd[0] == entry:
					# You've deleted all entries up to 'entry'. Stop now
					break

			# Re=add the entry, but with the updated index
			seen[entry] = end

	return max(longest, len(seen))


if __name__ == '__main__':
	exit(
		generic_test.generic_test_main(
			"longest_subarray_with_distinct_values.py",
			'longest_subarray_with_distinct_values.tsv',
			longest_subarray_with_distinct_entries))
