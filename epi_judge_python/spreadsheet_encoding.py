from test_framework import generic_test


def ss_decode_col_id(col):
	# Can treat it as base 26 (hexadecimal is from A-F, so spreadsheet is from
	# A-Z)
	# AA => 1 * 26^1 + 1 * 26^0
	import string
	col_id = 0

	BASE = 26
	exp = 0

	for char in reversed(col):
		col_id += (string.ascii_uppercase.index(char) + 1) * BASE ** exp
		exp += 1

	return col_id


if __name__ == '__main__':
	exit(
		generic_test.generic_test_main("spreadsheet_encoding.py",
									   'spreadsheet_encoding.tsv',
									   ss_decode_col_id))
