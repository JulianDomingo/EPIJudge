import functools

from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def lca(node0, node1):
	# Get depths of node0 and node1
	# Traverse upwards the deeper node until both nodes are at same layer
	# First node where node0 and node1 are the same reference is the LCA

	# Get depth
	node0_depth = node1_depth = 0
	tmp0, tmp1 = node0, node1

	while tmp0:
		node0_depth += 1
		tmp0 = tmp0.parent

	while tmp1:
		node1_depth += 1
		tmp1 = tmp1.parent

	# Traverse deeper node abs(node0_depth - node1_depth)
	diff = abs(node1_depth - node0_depth)

	if node0_depth > node1_depth:
		while diff:
			node0 = node0.parent
			diff -= 1
	else:
		while diff:
			node1 = node1.parent
			diff -= 1

	# Traverse upwards in tandem
	while node0 is not node1:
		node0, node1 = node0.parent, node1.parent

	# Return either arbitrarily
	return node0

	# Initial attempt
	# if not node0 or not node1:
		# return None

	# while node0 is not node1:
		# if not node0.data:
			# return node0
		# elif not node1.data:
			# return node1

		# node0.data = node1.data = None
		# node0 = node0.parent if node0.parent else node0
		# node1 = node1.parent if node1.parent else node1

	# # Arbitrarily return node0 or node1
	# return node0


@enable_executor_hook
def lca_wrapper(executor, tree, node0, node1):
	result = executor.run(
		functools.partial(lca, must_find_node(tree, node0),
						  must_find_node(tree, node1)))

	if result is None:
		raise TestFailure("Result can't be None")
	return result.data


if __name__ == '__main__':
	exit(
		generic_test.generic_test_main("lowest_common_ancestor_with_parent.py",
									   'lowest_common_ancestor.tsv',
									   lca_wrapper))
