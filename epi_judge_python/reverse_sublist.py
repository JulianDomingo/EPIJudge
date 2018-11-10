from test_framework import generic_test
from list_node import ListNode


def reverse_sublist(L, start, finish):
	# dummy_head = sublist_head = ListNode(0, L)

	# for _ in range(1, start):
		# sublist_head = sublist_head.next

	# # Reverses sublist.
	# sublist_iter = sublist_head.next
	# for _ in range(finish - start):
		# temp = sublist_iter.next
		# sublist_iter.next, temp.next, sublist_head.next = (temp.next,
								   # sublist_head.next,
								   # temp)
	# return dummy_head.next
	res = sentinel = ListNode(0, L)

	# Find preceding node to start node
	for _ in range(1, start):
		sentinel = sentinel.next

	# rev_start is head of sublist of length finish - start to reverse
	# Think of reversal as popping then immediately pushing back to a queue
	# exactly (finish - start) times
	rev_start = sentinel.next
	for _ in range(finish - start):
		# Set the node you want to move to the front
		to_move_to_front = rev_start.next

		# node preceding to_move_to_front's next should point to
		# 'to_move_to_front's next
		rev_start.next = to_move_to_front.next

		# Now safe to move to_move_to_front to point to initial start of reversed
		# list (rev_start)
		to_move_to_front.next = sentinel.next

		# Since sentinel needs to now point to 'to_move_to_front', and
		# to_move_to_front's next already points to sentinel's existing next,
		# we can clobber sentinel's existing next to now point to 'to_move_to_front'
		sentinel.next = to_move_to_front

	return res.next


if __name__ == '__main__':
	exit(
		generic_test.generic_test_main("reverse_sublist.py",
									   "reverse_sublist.tsv", reverse_sublist))
