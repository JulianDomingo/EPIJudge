from test_framework import generic_test
from list_node import ListNode


def revrse(h):
	prev, cur = None, h

	while cur:
		n = cur.next
		cur.next = prev
		cur, prev = n, cur

	return prev


def is_linked_list_a_palindrome(L):
	# Reverse second half of list and do walkthrough until reverse half reaches
	# end of list
	if not L or not L.next:
		return True

	# Determine length to get midpoint
	sz, tmp = 0, L

	while tmp:
		tmp = tmp.next
		sz += 1

	mid = sz // 2

	rev = L
	for _ in range(mid):
		rev = rev.next

	rev = revrse(rev)

	while rev:
		if rev.data != L.data:
			return False

		rev, L = rev.next, L.next

	return True


if __name__ == '__main__':
	exit(
		generic_test.generic_test_main("is_list_palindromic.py",
									   'is_list_palindromic.tsv',
									   is_linked_list_a_palindrome))
