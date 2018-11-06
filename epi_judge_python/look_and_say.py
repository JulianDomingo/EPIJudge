from test_framework import generic_test
from collections import Counter

def look_and_say(n):
	def next_las(s):
		i, res = 0, []

		while i < len(s):
			count = 1
			while i + 1 < len(s) and s[i] == s[i + 1]:
				count += 1
				i += 1

			res.append(str(count) + str(s[i]))
			i += 1

		return "".join(res)

	las = '1'
	for i in range(1, n):
		las = next_las(las)

	return las


if __name__ == '__main__':
	exit(
		generic_test.generic_test_main("look_and_say.py", "look_and_say.tsv",
									   look_and_say))
