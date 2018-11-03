from test_framework import generic_test


def count_bits(x):
	# - Clear the leftmost bit until x is 0
	# - O(1) solution would use a precomputed lookup table with partition key
	# sizes that are of a maintainable size in memory (i.e. for a 64 bit
	# integer x, we can use 16 bit size key partitions, as 2^64 entries for
	# 64-bit key partitions is too much). The solution would then simply be
	# the sum of the 4 partition key values.

	# Clear bit implementation
	num_bits = 0

	while x:
		x &= x - 1
		num_bits += 1

	return num_bits


if __name__ == '__main__':
	exit(
		generic_test.generic_test_main("count_bits.py", 'count_bits.tsv',
									   count_bits))
