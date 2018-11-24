from test_framework import generic_test, test_utils


def generate_power_set(S):
	def compute(idx, cur):
		if idx == len(S):
			final.append(list(cur))
			return

		compute(idx + 1, cur)
		compute(idx + 1, cur + [S[idx]])

	final = []
	compute(0, [])
	return final


if __name__ == '__main__':
	exit(
		generic_test.generic_test_main("power_set.py", 'power_set.tsv',
									   generate_power_set,
									   test_utils.unordered_compare))
