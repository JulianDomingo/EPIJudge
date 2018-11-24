from test_framework import generic_test


def levenshtein_distance(A, B):
	# Ex. horse -> hos, count=3
	# Explanation: convert 'r' to 's', delete 's' and 'e'
	#
	# Ex.2 hos -> horse, count=3
	# Explanation: convert 's' to 'r', add 's' and 'e'
	#
	# Ex.3 Saturday -> Sunday, count=3
	# Explanation: delete 'a' and 't', convert 'r' to 'n'
	#
	# Goal: return count of edits to convert word A to word B
	#
	# Intuition: process comparison of A and B left to right.
	#
	# 1. If prefix of A and B are equal, no edit is needed. Therefore,
	#		increment both pointers
	#
	# 2. If prefix of A != B, increment
	#



if __name__ == '__main__':
	exit(
		generic_test.generic_test_main("levenshtein_distance.py",
									   "levenshtein_distance.tsv",
									   levenshtein_distance))
