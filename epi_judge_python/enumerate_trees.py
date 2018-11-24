import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook
from binary_tree_node import BinaryTreeNode


def generate_all_binary_trees(num_nodes):
	if not num_nodes:
		return [None]

	final = []

	for total_right_subtree_nodes in range(num_nodes):
		# '-1' for root node
		total_left_subtree_nodes = num_nodes - 1 - total_right_subtree_nodes
		left_subtree_nodes = generate_all_binary_trees(total_left_subtree_nodes)
		right_subtree_nodes = generate_all_binary_trees(total_right_subtree_nodes)

		final += [
			BinaryTreeNode(0, left, right) for
			left in left_subtree_nodes for right in right_subtree_nodes
		]

	return final


def serialize_structure(tree):
	result = []
	q = [tree]
	while q:
		a = q.pop(0)
		result.append(0 if not a else 1)
		if a:
			q.append(a.left)
			q.append(a.right)
	return result


@enable_executor_hook
def generate_all_binary_trees_wrapper(executor, num_nodes):
	result = executor.run(
		functools.partial(generate_all_binary_trees, num_nodes))

	return sorted(map(serialize_structure, result))


if __name__ == '__main__':
	exit(
		generic_test.generic_test_main("enumerate_trees.py",
									   'enumerate_trees.tsv',
									   generate_all_binary_trees_wrapper))
