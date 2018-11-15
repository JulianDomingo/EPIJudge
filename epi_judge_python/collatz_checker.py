from test_framework import generic_test


def test_collatz_conjecture(n):
	# Optimizations:
	# 1. Cache already proven integers that converge so we can stop (prune) if
	#	 we see the integer in subsequent checks.
	# 2. Stop once we reach a value that is lower than starting integer (if
	#	 starting integer is >= 3). This is safe since for any starting integer
	#	 N, this implies all integers from [1, N - 1] inclusive have already
	#	 been proven. Therefore, there's a lot of wasted computation if we don't
	#	 stop early.
	#
	# 3. Use bit shifting

	# Odd => 3*n + 1
	# Even => n // 2
	proven = set()

	# Start at 3, since hypothesis holds true trivially
	for num in range(3, n + 1):
		seen = set()
		tmp = num

		while num >= tmp:
			if num in seen:
				# Disproves conjecture! If we've seen this number previously,
				# this would go to an infinite loop, so return False here.
				return False

			seen.add(num)
			num = (num * 3) + 1 if (num & 1) else (num >> 1)

		proven.add(tmp)

	return True


if __name__ == '__main__':
	exit(
		generic_test.generic_test_main("collatz_checker.py",
									   'collatz_checker.tsv',
									   test_collatz_conjecture))
