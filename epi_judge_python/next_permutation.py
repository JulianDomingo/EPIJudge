from test_framework import generic_test


def next_permutation(perm):
	# Find the number immediately preceding the longest decreasing suffix (the
	# longest decreasing suffix means the next permutation must have the
	# number preceding it change. We want to change it incrementally, so this
	# intuitively means swapping it with the smallest value in the longest
	# decreasing suffix that is larger than this number)
	#
	# Ex. [6, 2, 1, 5, 4, 3, 0] => [6, 2, 3, 5, 4, 1, 0]
	#
	# Then, reverse the updated decreasing suffix, since we are now starting at
	# the smallest possible permutation with the new preceding element, "3"
	#
	# [6, 2, 3, 5, 4, 1, 0] => [6, 2, 3, 0, 1, 4, 5]

	# Find longest decreasing suffix
	idx = len(perm) - 2

	while idx >=0 and perm[idx] >= perm[idx + 1]:
		idx -= 1

	# If permuation is entirely decreasing, this is the largest permutation. We
	# therefore return an empty list as specified
	if idx == -1:
		return []

	# idx now points to value we need to swap with the smallest value that is
	# larger than perm[idx]
	for i in reversed(range(len(perm))):
		if perm[i] > perm[idx]:
			perm[i], perm[idx] = perm[idx], perm[i]
			break

	# Reverse the updated decreasing suffix
	s = idx + 1
	e = len(perm) - 1

	while s < e:
		perm[s], perm[e] = perm[e], perm[s]
		s += 1
		e -= 1

	return perm


if __name__ == '__main__':
	exit(
		generic_test.generic_test_main(
			"next_permutation.py", 'next_permutation.tsv', next_permutation))
