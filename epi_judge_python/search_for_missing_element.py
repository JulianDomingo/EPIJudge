import collections

from test_framework import generic_test
from test_framework.test_failure import PropertyName

DuplicateAndMissing = collections.namedtuple('DuplicateAndMissing',
											 ('duplicate', 'missing'))


def find_duplicate_missing(A):
	# This will only work if we are guaranteed elements are within the inclusive
	# range from [0, n - 1].
	#
	# Swap each element to their corresponding index (i.e. value 1 should go to
	# index 1). Before this swap, check if the element seen at the index I am
	# going to swap to is already correct - if so, this is the duplicate.
	# Keep doing this even after we find the duplicate, because now we are
	# left with a nondecreasing array. At this point, we can trivially find the
	# missing by checking for the difference beteween a current element and
	# its preceding value is > 1.
	#
	# O(1) space, O(N) time.

	dup, missing = 0, -1

	# Find duplicate
	for i in range(len(A)):
		# Second boolean statement is important for incorrectly determining
		# duplicate
		if A[A[i]] == A[i] and i != A[i]:
			dup = A[i]

		# We need a 'tmp' variable since we're using A[i] as an index. If we
		# write to it beforehand though, the existing value is clobbered so we
		# need to preserve it.
		tmp_idx = A[i]
		A[i], A[tmp_idx] = A[tmp_idx], A[i]

	print('\nNon-decreasing A: {}'.format(A))
	# Find missing
	for i in range(1, len(A)):
		if A[i] - A[i - 1] > 1:
			missing = A[i]

	# Account for edge case of missing value being the largest in A
	if missing == -1:
		missing = len(A) - 1

	return DuplicateAndMissing(dup, missing)


def res_printer(prop, value):
	def fmt(x):
		return 'duplicate: {}, missing: {}'.format(x[0], x[1]) if x else None

	if prop in (PropertyName.EXPECTED, PropertyName.RESULT):
		return fmt(value)
	else:
		return value


if __name__ == '__main__':
	exit(
		generic_test.generic_test_main(
			"search_for_missing_element.py",
			'find_missing_and_duplicate.tsv',
			find_duplicate_missing,
			res_printer=res_printer))
