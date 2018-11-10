import functools

from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node, strip_parent_link
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def lca(tree, node0, node1):
	def helper(tree, n1, n2):
		if not tree:
			return 0, None

		# If both reside in one subtree, then the current node must be LCA.
		# Since this is a recursive call, we are guaranteed we get the CLOSEST
		# LCA.
		left_num, l_anc = helper(tree.left, n1, n2)
		if left_num == 2:
			return left_num, l_anc

		right_num, r_anc = helper(tree.right, n1, n2)
		if right_num == 2:
			return right_num, r_anc

		# '(n1, n2).count(tree) checks whether n1 or n2 are the current node,
		# incrementing if they are'
		# Obviously, if either left_num or right_num are > 0, (n1, n2).count(tree)
		# can never exceed 1.
		num_tot = left_num + right_num + (n1, n2).count(tree)

		ancestor = tree if num_tot == 2 else None
		return num_tot, ancestor

	cnt, anc = helper(tree, node0, node1)
	return anc


@enable_executor_hook
def lca_wrapper(executor, tree, key1, key2):
	strip_parent_link(tree)
	result = executor.run(
		functools.partial(lca, tree, must_find_node(tree, key1),
						  must_find_node(tree, key2)))

	if result is None:
		raise TestFailure("Result can't be None")
	return result.data


if __name__ == '__main__':
	exit(
		generic_test.generic_test_main("lowest_common_ancestor.py",
									   'lowest_common_ancestor.tsv',
									   lca_wrapper))
