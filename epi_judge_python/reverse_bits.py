from test_framework import generic_test


def reverse_bits(x):
	s = 1
	e = (1 << 63)

	while s < e:
		if x & s and not x & e or not x & s and x & e:
			x ^= (s | e)

		s <<= 1
		e >>= 1

	return x

	# *** Assuming x is 64-bit integer ***
	#
	# Brute force would be visiting every bit until n / 2 bit is reached,
	# where n = bit width of x. However, creation of a cached lookup table
	# of the reverses of every 16-bit integer optimizes this solution to
	# O(n / L), where n = bit width of x and L = size of cache key partition (4
	# in this example)
	#
	# Let each 16 bit partition be represented as y0, y1, y2, y3, with y3
	# being the most significant partition within x. Then, reverse of y0 gets
	# placed in y3's position, reverse of y1 gets placed in y2's position,
	# reverse of y2 gets placed in y1's position, and reverse of y3 gets
	# placed in y0's position.


	# Assume "REVERSE" is hardcoded into this file. (Don't feel like writing
	# code to generate this)

	# BIT_MASK = 0xFF
	# return (REVERSE[(x & BIT_MASK)] << (3 * BIT_MASK)) | \
		   # (REVERSE[(x >> BIT_MASK) & BIT_MASK] << (2 * BIT_MASK)) | \
		   # (REVERSE[(x >> (2 * BIT_MASK))] << (BIT_MASK)) | \
		   # (REVERSE[(x >> (3 * BIT_MASK))])

if __name__ == '__main__':
	exit(
		generic_test.generic_test_main("reverse_bits.py", "reverse_bits.tsv",
									   reverse_bits))
