from test_framework import generic_test
from test_framework.test_failure import TestFailure


def decoding(s):
	# 4a1b3c -> "aaaabccc"
	# When you see a character, keep incrementing index until you reach another
	# character to get frequency we want to add.
	res = []
	st = end = 0

	while end < len(s):
		end += 1
		if end == len(s) - 1:
			# Add last character
			for i in range(int(s[st:end])):
				res.append(s[end])

			break

		if end + 1 < len(s) and not s[end].isnumeric():
			# Found full number, add s[end] (the character) int(s[st:end]) times
			for i in range(int(s[st:end])):
				res.append(s[end])

			st = end + 1
			end += 1

	return ''.join(res)


def encoding(s):
	# "aaaabccc" -> a4b1c3
	# "abcd" -> a1b1c1d1
	res = []
	idx, freq = 0, 1

	while idx < len(s):
		if idx + 1 == len(s) or idx + 1 < len(s) and s[idx] != s[idx + 1]:
			# Update string
			res.append('{}{}'.format(str(freq), s[idx]))
			freq = 1
		else:
			freq += 1

		idx += 1

	return ''.join(res)


def rle_tester(encoded, decoded):
	if decoding(encoded) != decoded:
		raise TestFailure('Decoding failed')
	if encoding(decoded) != encoded:
		raise TestFailure('Encoding failed')


if __name__ == '__main__':
	exit(
		generic_test.generic_test_main("run_length_compression.py",
									   'run_length_compression.tsv',
									   rle_tester))
