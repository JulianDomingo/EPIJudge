from test_framework import generic_test
from list_node import ListNode


def add_two_numbers(L1, L2):
	# 3 -> 1 -> 4
	# 8 -> 0 -> 2 -> 2

	#  2208
	# + 413
	#  2621

	# res = 1
	# res = 12
	# res = 126
	# res = 1262
	# final = 2621
	res = carry = 0

	while L1 or L2:
		res *= 10

		l1_add = L1.data if L1 else 0
		l2_add = L2.data if L2 else 0

		col_add = l1_add + l2_add + carry

		res += col_add % 10
		carry = col_add // 10

		L1 = L1.next if L1 else None
		L2 = L2.next if L2 else None

	if carry:
		# Count for MSD carry
		res *= 10
		res += carry

	# Reverse to proper order
	final = 0

	while res:
		final *= 10
		final += res % 10
		res //= 10

	return final


if __name__ == '__main__':
	exit(
		generic_test.generic_test_main("int_as_list_add.py",
									   'int_as_list_add.tsv', add_two_numbers))
