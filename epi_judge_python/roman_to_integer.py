from test_framework import generic_test


def roman_to_integer(s):
	# Sophisticated right to left approach. If current romam numeral is larger
	# than subsequent value in right to left approach, we add the current roman
	# numeral value minus the subsequent roman numeral and decrement twice instead
	# of once. You can still do this from left to right, you just add the
	# abs difference of current and subsequent
	mapping = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

	res = 0
	start = 0

	while start < len(s):
		if start + 1 < len(s) and mapping[s[start]] < mapping[s[start + 1]]:
			res += mapping[s[start + 1]] - mapping[s[start]]
			start += 2
		else:
			# General case
			res += mapping[s[start]]
			start += 1

	# "LIX" ->
	# while start < len(s):
		# if start + 1 < len(s) and s[start] == 'I' and s[start + 1] == 'V':
			# res += 4
			# start += 2
		# elif start + 1 < len(s) and s[start] == 'I' and s[start + 1] == 'X':
			# res += 9
			# start += 2
		# elif start + 1 < len(s) and s[start] == 'X' and s[start + 1] == 'L':
			# res += 40
			# start += 2
		# elif start + 1 < len(s) and s[start] == 'X' and s[start + 1] == 'C':
			# res += 90
			# start += 2
		# elif start + 1 < len(s) and s[start] == 'C' and s[start + 1] == 'D':
			# res += 400
			# start += 2
		# elif start + 1 < len(s) and s[start] == 'C' and s[start + 1] == 'M':
			# res += 900
			# start += 2
		# else:
			# # General case
			# res += mapping[s[start]]
			# start += 1

	return res


if __name__ == '__main__':
	exit(
		generic_test.generic_test_main(
			"roman_to_integer.py", 'roman_to_integer.tsv', roman_to_integer))
