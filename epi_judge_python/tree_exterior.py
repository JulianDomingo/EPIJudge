import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def is_leaf(root):
	return not root.left and not root.right


def exterior_binary_tree(tree):
	def left_subtree(subtree, is_boundary):
		if not subtree:
			return []

		return (([subtree] if (is_boundary or is_leaf(subtree)) else []) +
				left_subtree(subtree.left, is_boundary) +
				left_subtree(subtree.right, is_boundary and not subtree.left))


	def right_subtree(subtree, is_boundary):
		if not subtree:
			return []

		return (right_subtree(subtree.left, is_boundary and not subtree.right) +
				right_subtree(subtree.right, is_boundary) +
			   ([subtree] if (is_boundary or is_leaf(subtree)) else []))


	return (tree + left_subtree(tree.left, is_boundary=True) +
				   right_subtree(tree.right, is_boundary=True) if tree else [])


def create_output_list(L):
	if any(l is None for l in L):
		raise TestFailure('Resulting list contains None')
	return [l.data for l in L]


@enable_executor_hook
def create_output_list_wrapper(executor, tree):
	result = executor.run(functools.partial(exterior_binary_tree, tree))

	return create_output_list(result)


if __name__ == '__main__':
	exit(
		generic_test.generic_test_main("tree_exterior.py", 'tree_exterior.tsv',
									   create_output_list_wrapper))
