import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


def replace_and_remove(size, s):
	# Forward pass for determining total size of new string and skipping over
	# 'b', second backward pass for overwriting 'a' with 'dd'
	a_cnt = 0
	write_idx = 0

	for i in range(size):
		if s[i] != 'b':
			s[write_idx] = s[i]
			write_idx += 1
		if s[i] == 'a':
			a_cnt += 1

	# -1 since it write_idx will point to next available write space. -1 will
	# move it back to last valid character
	traverse = write_idx - 1
	write_idx += a_cnt - 1
	final_size = write_idx + 1

	while traverse >= 0:
		if s[traverse] == 'a':
			s[write_idx - 1:write_idx + 1] = 'dd'
			write_idx -= 2

		else:
			# Non 'a' character
			s[write_idx] = s[traverse]
			write_idx -= 1

		traverse -= 1

	return final_size


@enable_executor_hook
def replace_and_remove_wrapper(executor, size, s):
	res_size = executor.run(functools.partial(replace_and_remove, size, s))
	return s[:res_size]


if __name__ == '__main__':
	exit(
		generic_test.generic_test_main("replace_and_remove.py",
									   'replace_and_remove.tsv',
									   replace_and_remove_wrapper))
