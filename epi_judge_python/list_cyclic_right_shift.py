from test_framework import generic_test
from list_node import ListNode


def cyclically_right_shift_list(L, k):
	if not L or not k:
		return L

	# Determine length
	n = 0
	temp, dummy = L, ListNode(0, L)
	while temp:
		n += 1
		temp = temp.next

	# Handles cases easily when k > n
	k %= n

	if not k:
		return L

	# NOTE: 'L' will still point to the initial head even if another reference
	# which was initially at L changes
	cur = L
	# Get needed pointers
	for i in range(n - k - 1):
		cur = cur.next

	new_head = cur.next

	old_tail = new_head

	while old_tail.next:
		old_tail = old_tail.next

	# Set old tail to old head
	old_tail.next = L
	# Set new tail's .next to None making it the end of the list
	cur.next = None

	return new_head


if __name__ == '__main__':
	exit(
		generic_test.generic_test_main("list_cyclic_right_shift.py",
									   'list_cyclic_right_shift.tsv',
									   cyclically_right_shift_list))
