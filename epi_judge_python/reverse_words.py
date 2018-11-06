import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


# Assume s is a string encoded as bytearray.
def reverse_words(s):
	s = list(s.decode('utf-8'))
	# Reverse once to get correct word ordering, reverse again to get correct
	# indvidual word letter ordering

	# Don't try to be Pythonic if it incurs extra space
	i, j = 0, len(s) - 1

	while i < j:
		s[i], s[j] = s[j], s[i]
		i, j = i + 1, j - 1

	t = st = 0
	while t < len(s):
		if t == len(s) - 1 or s[t + 1] == ' ':
			# Reverse word
			tmp = t
			while st < tmp:
				s[st], s[tmp] = s[tmp], s[st]
				st += 1
				tmp -= 1

			st = t + 2
			t = st

		t += 1

	s = str("".join(s))
	print(s)

	return s


@enable_executor_hook
def reverse_words_wrapper(executor, s):
	s_copy = bytearray()
	s_copy.extend(map(ord, s))

	executor.run(functools.partial(reverse_words, s_copy))

	return s_copy.decode("utf-8")


if __name__ == '__main__':
	exit(
		generic_test.generic_test_main("reverse_words.py", 'reverse_words.tsv',
									   reverse_words_wrapper))
