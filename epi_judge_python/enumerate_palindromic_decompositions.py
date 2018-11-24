from test_framework import generic_test


def is_palindrome(string):
	s, e = 0, len(string) - 1

	while s < e:
		if string[s] != string[e]:
			return False
		s, e = s + 1, e - 1

	return True


def palindrome_decompositions(input):
	# 0201111 => [0, 2, 0, 1, 1, 1, 1]
	#			 [020, 1111]
	#			 [020, 1, 1, 1, 1]
	#			 [020, 11, 11]
	# From this case study, we traverse from left to right from the given input
	# and find the first possible palindrome (0). We then recursively call
	# and treat the substring not including the 'prefix palindrome' as the
	# new input string, bringing along existing palindrome decompositions as
	# deeper recursive calls are made.
	# Eventually the top level call is reached again, and this time we now
	# increment until we find the next palindrome - in this case, '020'. After
	# this, we have generated all palinndrome decomposition lists.
	def helper(cur_decomp, idx):
		if idx == len(input):
			# Done, add decomposition list
			final.append(list(cur_decomp))
			return

		# We start at idx + 1 since that's a single character
		for cur in range(idx + 1, len(input) + 1):
			# Find the starting palindrome prefix to begin recursive calls.
			if is_palindrome(input[idx:cur]):
				# Make sure to add the index offset, not idx + cur!
				helper(cur_decomp + [input[idx:cur]], idx + (cur - idx))

	final = []
	helper([], 0)
	return final


def comp(a, b):
	return sorted(a) == sorted(b)


if __name__ == '__main__':
	exit(
		generic_test.generic_test_main(
			"enumerate_palindromic_decompositions.py",
			'enumerate_palindromic_decompositions.tsv',
			palindrome_decompositions, comp))
