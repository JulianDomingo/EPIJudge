from test_framework import generic_test, test_utils
from collections import deque

MAPPING = ['0', '1', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

def phone_mnemonic(phone_number):
	# Shouldn't use recursive approach due to possibility of incurring too much
	# stack space.
	# Iterative approach involves using a queue which iteratively processes the
	# combinations of strings
	q = deque()

	for digit in phone_number:
		if not q:
			for char in MAPPING[int(digit)]:
				q.append(char)

			# First digit
			continue

		sentinel_length = len(q[0])

		# Stop adding once all values have been updated to new length
		while len(q[0]) == sentinel_length:
			# Pop roots from queue and add onto them before pushing back
			popd = q.popleft()

			for char in MAPPING[int(digit)]:
				q.append(popd + char)

	return list(q)


if __name__ == '__main__':
	exit(
		generic_test.generic_test_main(
			"phone_number_mnemonic.py",
			'phone_number_mnemonic.tsv',
			phone_mnemonic,
			comparator=test_utils.unordered_compare))
