from test_framework import generic_test


# Given n, return all primes up to and including n.
def generate_primes(n):
	sieve = list(range(2, n + 1))

	for i in range(len(sieve)):
		if sieve[i] != -1:
			sieve_step = sieve[i]
			idx = i + sieve_step
			# [2, 3, 4, 5, 6, 7, 8, 9, 10]

			while idx < len(sieve):
				# Clear out multiples of prime
				sieve[idx] = -1
				idx += sieve_step

	return list(filter(lambda num: num != -1, sieve))


if __name__ == '__main__':
	exit(
		generic_test.generic_test_main("prime_sieve.py", "prime_sieve.tsv",
									   generate_primes))
