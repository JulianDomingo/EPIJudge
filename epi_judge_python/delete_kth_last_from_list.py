from test_framework import generic_test
from list_node import ListNode


# Assumes L has at least k nodes, deletes the k-th last node in L.
def remove_kth_last(L, k):
	# Two pointers. One trails the list normally, other is exactly k nodes behind
	# it. When normal pointer reaches end, trailing pointer points to the node
	# we want to delete.
	trailing = None
	dummy_head = ListNode(0, L)
	cur = dummy_head.next

	for i in range(k):
		cur = cur.next

	# 1 -> 2 -> 3 -> 4 -> 5, k = 2 (delete 4)
	# 2 -> 1, k = 2 (delete 2)

	trailing = dummy_head

	while cur:
		cur, trailing = cur.next, trailing.next

	# Trailing points to node to delete
	trailing.next = trailing.next.next

	return dummy_head.next


if __name__ == '__main__':
	exit(
		generic_test.generic_test_main("delete_kth_last_from_list.py",
									   'delete_kth_last_from_list.tsv',
									   remove_kth_last))
