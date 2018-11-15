import collections
import functools
import sys

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

Subarray = collections.namedtuple('Subarray', ('start', 'end'))

def find_smallest_sequentially_covering_subset(paragraph, keywords):
	result = Subarray(-1, -1)
	smallest = sys.maxsize
	res_s = res_e = 0
	left = 0
	tally = len(keywords)
	keywords_set = set(keywords)

	# Use counter object as threshold. Once tally is empty, record
	# result and start incrementing start pointer until no longer containing
	# words in keywords
	kw_counter = collections.Counter(keywords)

	for right, word in enumerate(paragraph):
		if word in kw_counter:
			kw_counter[word] -= 1
			if kw_counter[word] >= 0:
				# Only decrement tally for TOTAL occurrences in keywords.
				tally -= 1

		while not tally:
			if result == (-1, -1) or right - left < result[1] - result[0]:
				result = (left, right)

			if paragraph[left] in kw_counter:
				kw_counter[paragraph[left]] += 1
				if kw_counter[paragraph[left]] > 0:
					tally += 1

			left += 1

	return result


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
