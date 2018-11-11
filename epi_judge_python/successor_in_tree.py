import functools

from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node
from test_framework.test_utils import enable_executor_hook


def find_successor(node):
	if node.right:
		# Successor is the leftmost node in right subtree
		res = node.right
		while res.left:
			res = res.left

		return res

	else:
		# Successor is the first node s.t. node.parent.right is NOT node
		while node.parent and node.parent.right is node:
			node = node.parent

		# Account for last node in inorder traversal not needed since
		# 'parent' field for nodes without parent is -1.
		return node.parent


@enable_executor_hook
def find_successor_wrapper(executor, tree, node_idx):
	node = must_find_node(tree, node_idx)

	result = executor.run(functools.partial(find_successor, node))

	return result.data if result else -1


if __name__ == '__main__':
	exit(
		generic_test.generic_test_main("successor_in_tree.py",
									   'successor_in_tree.tsv',
									   find_successor_wrapper))
