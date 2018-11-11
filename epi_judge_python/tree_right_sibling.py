import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook
from collections import deque


class BinaryTreeNode:
	def __init__(self, data=None):
		self.data = data
		self.left = None
		self.right = None
		self.next = None  # Populates this field.


def is_leaf(node):
	return not node.left and not node.right


def construct_right_sibling(tree):
	if not tree:
		return

	# There are precisely 2^height total nodes in each layer, where layer of
	# root is 0. If we perform a BFS on the perfect binary tree, we know
	# precisely the number of nodes each layer will have, so we pop a total of
	# 2^height total nodes from the queue at each iteration and process their
	# .next fields to be the subsequent node in the popped list. We then add
	# all the previous layer's children to the queue and repeat the process
	# until the leaf layer is reached.
	num_nodes_in_layer = 1

	q = deque()
	q.append(tree)

	while len(q):
		layer_nodes = []

		# Obtain all nodes in current layer
		for _ in range(num_nodes_in_layer):
			layer_nodes.append(q.popleft())

		# Set next fields
		for i in range(len(layer_nodes) - 1):
			layer_nodes[i].next = layer_nodes[i + 1]

		# Don't add if current layer is leaf layer
		if is_leaf(layer_nodes[0]):
			break

		# Add current layer's child nodes
		for node in layer_nodes:
			q.append(node.left)
			q.append(node.right)

		# Update layer size
		num_nodes_in_layer <<= 1

	return


def traverse_next(node):
	while node:
		yield node
		node = node.next
	raise StopIteration


def traverse_left(node):
	while node:
		yield node
		node = node.left
	raise StopIteration


def clone_tree(original):
	if not original:
		return None
	cloned = BinaryTreeNode(original.data)
	cloned.left, cloned.right = clone_tree(original.left), clone_tree(
		original.right)
	return cloned


@enable_executor_hook
def construct_right_sibling_wrapper(executor, tree):
	cloned = clone_tree(tree)

	executor.run(functools.partial(construct_right_sibling, cloned))

	return [[n.data for n in traverse_next(level)]
			for level in traverse_left(cloned)]


if __name__ == '__main__':
	exit(
		generic_test.generic_test_main("tree_right_sibling.py",
									   'tree_right_sibling.tsv',
									   construct_right_sibling_wrapper))
