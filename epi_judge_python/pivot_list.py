import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

from list_node import ListNode

def list_pivoting(l, x):
	if not l:
		return l

	lt_head = lt_cur = ListNode(l)
	eq_head = eq_cur = ListNode(l)
	gt_head = gt_cur = ListNode(l)

	# Start populating these partitions. Since we do a linear traversal, this
	# algorithm maintains the original order

	while l:
		if l.data < x:
			lt_cur.next = l
			lt_cur = lt_cur.next
		elif l.data == x:
			eq_cur.next = l
			eq_cur = eq_cur.next
		else:
			gt_cur.next = l
			gt_cur = gt_cur.next

		l = l.next

	# Connect the partitions
	gt_cur.next = None
	eq_cur.next = gt_head.next
	lt_cur.next = eq_head.next

	return lt_head.next


def linked_to_list(l):
	v = list()
	while l is not None:
		v.append(l.data)
		l = l.next
	return v


@enable_executor_hook
def list_pivoting_wrapper(executor, l, x):
	original = linked_to_list(l)

	l = executor.run(functools.partial(list_pivoting, l, x))

	pivoted = linked_to_list(l)
	mode = -1
	for i in pivoted:
		if mode == -1:
			if i == x:
				mode = 0
			elif i > x:
				mode = 1
		elif mode == 0:
			if i < x:
				raise TestFailure('List is not pivoted')
			elif i > x:
				mode = 1
		else:
			if i <= x:
				raise TestFailure('List is not pivoted')

	if sorted(original) != sorted(pivoted):
		raise TestFailure('Result list contains different values')


if __name__ == '__main__':
	exit(
		generic_test.generic_test_main("pivot_list.py", 'pivot_list.tsv',
									   list_pivoting_wrapper))
