import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def overlapping_no_cycle_lists(l0, l1):
	if not l0 or not l1:
		return None

	head0, head1 = l0, l1

	# Account for offsets
	while head0.next and head1.next:
		head0, head1 = head0.next, head1.next

	if not head0.next:
		head0 = l1

	if not head1.next:
		head1 = l0

	# Offsets have been equalized, traverse both pointers until either they
	# are the same pointer or reached end of list

	while head0:
		if head0 is head1:
			return head0

		head0, head1 = head0.next, head1.next

	return None


@enable_executor_hook
def overlapping_no_cycle_lists_wrapper(executor, l0, l1, common):
	if common:
		if l0:
			i = l0
			while i.next:
				i = i.next
			i.next = common
		else:
			l0 = common

		if l1:
			i = l1
			while i.next:
				i = i.next
			i.next = common
		else:
			l1 = common

	result = executor.run(
		functools.partial(overlapping_no_cycle_lists, l0, l1))

	if result != common:
		raise TestFailure('Invalid result')


if __name__ == '__main__':
	exit(
		generic_test.generic_test_main("do_terminated_lists_overlap.py",
									   'do_terminated_lists_overlap.tsv',
									   overlapping_no_cycle_lists_wrapper))
