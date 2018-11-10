from test_framework import generic_test
from collections import deque, namedtuple


def binary_tree_depth_order(tree):
	res = []

	if not tree:
		return res

	res = []
	cur_depth_nodes = [tree]

	while cur_depth_nodes:
		res.append([node.data for node in cur_depth_nodes])

		# Update cur_depth_nodes to store all nodes in i + 1 layer
		cur_depth_nodes = [
			# Recall that for more than one loop in list comprehension, the
			# outer loop precedes the inner loop(s).

			# This reads out to be "add child to list if child exists from a
			# previous layer node 'cur_node', for ALL 'cur_node' in
			# 'cur_depth_nodes' list."
			child for cur_node in cur_depth_nodes
				  for child    in (cur_node.left, cur_node.right)
				  if child
		]

	return res




if __name__ == '__main__':
	exit(
		generic_test.generic_test_main("tree_level_order.py",
									   "tree_level_order.tsv",
									   binary_tree_depth_order))
