import collections

from test_framework import generic_test
from test_framework.test_failure import PropertyName

MinMax = collections.namedtuple('MinMax', ('smallest', 'largest'))


def find_min_max(A):
	if len(A) <= 1:
		return MinMax(A[0], A[0])

	# 3n/2 - 1
	cur_min, cur_max = (A[0], A[1]) if (A[0] < A[1]) else (A[1], A[0])

	for i in range(2, len(A) - 1, 2):
		elem1, elem2 = A[i], A[i + 1]
		# 1 comparison
		tmp_smaller, tmp_larger = (elem1, elem2) if (elem1 < elem2) else (elem2, elem1)

		# 2 comparisons
		cur_min = min(cur_min, tmp_smaller)
		cur_max = max(cur_max, tmp_larger)

	# Account for odd length array
	if len(A) & 1:
		cur_min = min(cur_min, A[-1])
		cur_max = max(cur_max, A[-1])

	return MinMax(cur_min, cur_max)

	# 2n - 1
	# s, e = 0, len(A) - 1
	# cur_min, cur_max = A[s], A[e]

	# while s <= e:
		# cur_min = min(cur_min, min(A[s], A[e]))
		# cur_max = max(cur_max, max(A[s], A[e]))
		# s, e = s + 1, e - 1

	# return MinMax(cur_min, cur_max)


def res_printer(prop, value):
	def fmt(x):
		return 'min: {}, max: {}'.format(x[0], x[1]) if x else None

	if prop in (PropertyName.EXPECTED, PropertyName.RESULT):
		return fmt(value)
	else:
		return value


if __name__ == '__main__':
	exit(
		generic_test.generic_test_main(
			"search_for_min_max_in_array.py",
			'search_for_min_max_in_array.tsv',
			find_min_max,
			res_printer=res_printer))
