import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook
from binary_tree_node import BinaryTreeNode


def reconstruct_preorder(preorder):
	preorder_iter = iter(preorder)

	def helper(it):
		cur_root = next(it)

		if not cur_root:
			# Reached null pointer, simply return yourself
			return None

		left_subtree = helper(it)
		right_subtree = helper(it)

		return BinaryTreeNode(cur_root, left_subtree, right_subtree)

	return helper(preorder_iter)


@enable_executor_hook
def reconstruct_preorder_wrapper(executor, data):
	data = [None if x == 'null' else int(x) for x in data]
	return executor.run(functools.partial(reconstruct_preorder, data))


if __name__ == '__main__':
	exit(
		generic_test.generic_test_main("tree_from_preorder_with_null.py",
									   'tree_from_preorder_with_null.tsv',
									   reconstruct_preorder_wrapper))
