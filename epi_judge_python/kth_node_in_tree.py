import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


class BinaryTreeNode:
	def __init__(self, data=None, left=None, right=None, size=None):
		self.data = data
		self.left = left
		self.right = right
		self.size = size


def leaf(cur):
	return not cur.left and not cur.right


def find_kth_node_binary_tree(tree, k):
	if not tree or leaf(tree):
		return tree

	left_st_sz = tree.left.size if tree.left else 0

	if left_st_sz + 1 == k:
		return tree
	elif left_st_sz + 1 < k:
		# Don't forget to update k if we want to find node in right subtree!!
		# Remember to do case analysis to detect this.
		k -= (left_st_sz + 1)
		return find_kth_node_binary_tree(tree.right, k)
	else:
		return find_kth_node_binary_tree(tree.left, k)


@enable_executor_hook
def find_kth_node_binary_tree_wrapper(executor, tree, k):
	def init_size(node):
		if not node:
			return 0
		node.size = 1 + init_size(node.left) + init_size(node.right)
		return node.size

	init_size(tree)

	result = executor.run(
		functools.partial(find_kth_node_binary_tree, tree, k))

	if not result:
		raise TestFailure("Result can't be None")
	return result.data


if __name__ == '__main__':
	exit(
		generic_test.generic_test_main("kth_node_in_tree.py",
									   "kth_node_in_tree.tsv",
									   find_kth_node_binary_tree_wrapper))
