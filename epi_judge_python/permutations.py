from test_framework import generic_test, test_utils
from copy import deepcopy


def permutations(A):
	def gen_permutes(cur):
		if len(cur) == len(A):
			final.append(deepcopy(cur))
			return
		else:
			for num in A:
				if len(cur) == 0 or num not in cur:
					cur.append(num)
					gen_permutes(cur)
					# Remove it for next permutation
					cur.pop()

	cur, final = [], []
	gen_permutes(cur)
	return final


if __name__ == '__main__':
	exit(
		generic_test.generic_test_main("permutations.py", 'permutations.tsv',
									   permutations,
									   test_utils.unordered_compare))
