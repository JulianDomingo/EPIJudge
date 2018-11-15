import collections
import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

Subarray = collections.namedtuple('Subarray', ('start', 'end'))

def find_smallest_sequentially_covering_subset(paragraph, keywords):
	# Caveat: This stores the entire paragraph in memory. To optimize memory,
	# use a DLL that stores the latest index of any keyword in the keywords set.
	# When we find a closer index of a word in keywords, we push the DLL node
	# to thet end of the DLL, so that the head is the starting point of the
	# subarray which contains all keywords. Since we update the indices, this
	# DLL will always have the most optimized length (by taking difference of
	# current index and index of node at head of linked list). We use a dict
	# to access nodes in the DLL in O(1) time.

	res = Subarray(0, 0)
	kw_counter = collections.Counter(keywords)
	l, tally = 0, len(keywords)

	for r, text in enumerate(paragraph):
		if text in kw_counter:
			kw_counter[text] -= 1
			if kw_counter[text] >= 0:
				# Account for occurrences only up to the frequency found in keywords
				tally -= 1

		while tally == 0:
			if res == (0, 0) or res[1] - res[0] > r - l:
				res = (l, r)

			if paragraph[l] in kw_counter:
				kw_counter[paragraph[l]] += 1
				if kw_counter[paragraph[l]] > 0:
					tally += 1

			l += 1

	return res


@enable_executor_hook
def find_smallest_sequentially_covering_subset_wrapper(executor, paragraph,
													   keywords):
	result = executor.run(
		functools.partial(find_smallest_sequentially_covering_subset,
						  paragraph, keywords))

	kw_idx = 0
	para_idx = result.start
	if para_idx < 0:
		raise RuntimeError('Subarray start index is negative')

	while kw_idx < len(keywords):
		if para_idx >= len(paragraph):
			raise TestFailure("Not all keywords are in the generated subarray")
		if para_idx >= len(paragraph):
			raise TestFailure("Subarray end index exceeds array size")
		if paragraph[para_idx] == keywords[kw_idx]:
			kw_idx += 1
		para_idx += 1

	return result.end - result.start + 1


if __name__ == '__main__':
	exit(
		generic_test.generic_test_main(
			"smallest_subarray_covering_all_values.py",
			'smallest_subarray_covering_all_values.tsv',
			find_smallest_sequentially_covering_subset_wrapper))
