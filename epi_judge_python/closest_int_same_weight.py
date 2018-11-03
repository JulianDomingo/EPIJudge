from test_framework import generic_test


def closest_int_same_bit_count(x):
	# Brute force solution would be to iteratively check every integer lower
	# and higher than x, then take the min of the difference between x and the
	# first integer with same bit weight lower than x + difference between x
	# and the first integer with the same bit weight higher than x. However,
	# this can be upwards of O(2^n) when x is a power of 2 (since the next
	# integer closest to x would be another power of 2)
	#
	# We know the closest integer to x is more likely to have a different bit
	# pattern towards the bits of lower significance, as this minimimzes the
	# numerical difference. Thus, we know a bit swap of a set and unset bit
	# which are close together would yield a correct and optimal solution.
	#
	# This is O(1) runtime and space.

	if x & 1:
		# If no trailing zeros exist, we take a similar approach to finding this
		# bit. Since decrementing clears the set LSB, incrementing sets the unset
		# LSB (due to ripple).
		lsb_unset = (x + 1) & ~(x - 1 + 1)

		# Clear the adjacently set bit to the right of the unset bit
		x ^= (lsb_unset >> 1)

		x |= lsb_unset

	else:
		# Trailing zero exists. We can simply right shift and OR the set bit
		# to "swap" the set bit.
		lsb_set = x & ~(x - 1)

		# Make sure to clear the initially LSB set bit BEFORE setting the
		# trailing zero. Otherwise, we just end up clearing the bit.
		x &= (x - 1)

		x |= (lsb_set >> 1)

	return x


if __name__ == '__main__':
	exit(
	generic_test.generic_test_main("closest_int_same_weight.py",
					   "closest_int_same_weight.tsv",
					   closest_int_same_bit_count))
