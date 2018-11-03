import functools
import random

from test_framework import generic_test
from test_framework.random_sequence_checker import (
	check_sequence_is_uniformly_random, run_func_with_retries)
from test_framework.test_utils import enable_executor_hook


def zero_one_random():
	return random.randrange(2)


def uniform_random(lower_bound, upper_bound):
	num_outcomes = upper_bound - lower_bound + 1
	res = 0

	while True:
		res = i = 0

		while (1 << i) < num_outcomes:
			res = (res << 1) | zero_one_random()
			i += 1

		if res < num_outcomes:
			break

	return res + lower_bound

	# Find 'k' s.t. upper_bound <= 2^k
	# k = 1
	# while k < upper_bound:
		# k <<= 1

	# # Initialize result to a value outside of acceptable range
	# out = lower_bound - 1

	# while out < lower_bound or out > upper_bound:
		# # Generate a uniform distribution of values from [0, 2^k - 1]
		# tmp = k
		# res = 0

		# while tmp >= 0:
			# res = (res << 1) | zero_one_random()
			# tmp -= 1

		# out = res + lower_bound

	# print(str(out))
	# return out


@enable_executor_hook
def uniform_random_wrapper(executor, lower_bound, upper_bound):
	def uniform_random_runner(executor, lower_bound, upper_bound):
		result = executor.run(lambda : [uniform_random(lower_bound, upper_bound) for _ in range(100000)])

		return check_sequence_is_uniformly_random(
			[a - lower_bound
			 for a in result], upper_bound - lower_bound + 1, 0.01)

	run_func_with_retries(
		functools.partial(uniform_random_runner, executor, lower_bound,
						  upper_bound))


if __name__ == '__main__':
	exit(
		generic_test.generic_test_main("uniform_random_number.py",
									   'uniform_random_number.tsv',
									   uniform_random_wrapper))
