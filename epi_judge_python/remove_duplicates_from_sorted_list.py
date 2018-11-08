from test_framework import generic_test
from list_node import ListNode


def remove_duplicates(L):
	dummy = ListNode(0, L)
	dummy.next = L

	while L and L.next:
		# There can be more than one duplicate
		if L.data == L.next.data:
			tmp = L.next

			while tmp.next and tmp.data == tmp.next.data:
				tmp = tmp.next

			L.next = tmp.next

		else:
			L = L.next

	return dummy.next


if __name__ == '__main__':
	exit(
		generic_test.generic_test_main(
			"remove_duplicates_from_sorted_list.py",
			'remove_duplicates_from_sorted_list.tsv', remove_duplicates))
