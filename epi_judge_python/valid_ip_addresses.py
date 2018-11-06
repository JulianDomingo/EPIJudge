from test_framework import generic_test


def get_valid_ip_address(s):
	def is_valid(s):
		# Can't have preceding zeros unless it's the only digit in the part
		return len(s) == 1 or (s[0] != '0' and int(s) <= 255)

	# A valid IP address constitutes 3 period delimiters. Each period separated
	# partition must be in the range from 1 to 255 inclusive. Thus, we can
	# use nested for-loops first testing the first partition with 1 digit, 2
	# digits, then 3 digits and enumerating from these starting points. We can
	# prune by backtracking as soon as a partition is invalid (i.e. not within
	# [0, 255])
	res = []
	parts = [None] * 4

	# Use a 4-way nested for loop (1 for each partition)
	# O(2^32) => O(1) time complexity
	for i in range(1, min(4, len(s))):
		# 1st partition
		if not is_valid(s[:i]):
			continue

		parts[0] = s[:i]

		for j in range(1, min(len(s) - i, 4)):
			if not is_valid(s[i:i+j]):
				continue

			parts[1] = s[i:i+j]

			for k in range(1, min(len(s) - i - j, 4)):
				parts[2], parts[3] = s[i+j:i+j+k], s[i+j+k:]

				if not is_valid(parts[2]) or not is_valid(parts[3]):
					continue

				res.append(".".join(parts))

	return res


def comp(a, b):
	return sorted(a) == sorted(b)


if __name__ == '__main__':
	exit(
		generic_test.generic_test_main(
			"valid_ip_addresses.py",
			'valid_ip_addresses.tsv',
			get_valid_ip_address,
			comparator=comp))
