from test_framework import generic_test

def hash_apppend(existing_hash, to_append):
	existing_hash = (existing_hash * BASE) + ord(to_append)
	return existing_hash % PRIME


def hash_pop(existing_hash, to_pop):
	existing_hash -= (ord(to_pop) * (BASE**(S_LEN - 1) % PRIME))
	return existing_hash % PRIME


def rabin_karp(t, s):
	if len(s) > len(t):
		return -1

	global BASE, PRIME, S_LEN
	# We assume we are only given a character set of alphabetical characters.
	# Thus, a base of 27 is unique.
	BASE = 255
	# Should be a prime
	PRIME = 97
	S_LEN = len(s)
	s_hash, cur_hash = 0, 0

	# Calculate hash to find
	for i in range(len(s)):
		s_hash = hash_apppend(s_hash, s[i])

	# Calculate starting hash
	for i in range(len(t[:S_LEN])):
		cur_hash = hash_apppend(cur_hash, t[i])

	# Find the first occurrence of string 's' in text 't'
	# Sliding window lmao
	n = len(s)
	st, end = 0, n

	while end < len(t):
		cur_hash = hash_pop(cur_hash, t[st])
		cur_hash = hash_apppend(cur_hash, t[end])
		st, end = st + 1, end + 1

		if cur_hash == s_hash:
			# Check actual strings in case of hash collision
			print("Checking {} and {}".format(s, t[st:end]))
			return st

	return -1

if __name__ == '__main__':
	exit(
		generic_test.generic_test_main("substring_match.py",
									   'substring_match.tsv', rabin_karp))
