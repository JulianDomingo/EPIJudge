from test_framework import generic_test
from list_node import ListNode


def even_odd_merge(L):
	res = ListNode(0, L)
	res.next = L

	# Account for edge cases
	if not L or not L.next:
		return L

	even, odd = L, L.next

	f_odd = odd

	while odd and odd.next:
		even.next = odd.next
		odd.next = odd.next.next
		even, odd = even.next, odd.next

	# Link last even to first odd (through f_odd)
	even.next = f_odd

	# Ensure list terminates by setting odd.next to null
	if odd:
		odd.next = None

	return res.next


if __name__ == '__main__':
	exit(
		generic_test.generic_test_main("even_odd_list_merge.py",
									   'even_odd_list_merge.tsv',
									   even_odd_merge))
