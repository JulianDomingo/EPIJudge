from test_framework import generic_test
from binary_tree_node import BinaryTreeNode


def binary_tree_from_preorder_inorder(preorder, inorder):
	# Generate subtrees recursively by keep track of the indices. This is linear
	# time, since we traverse each element only once.
	inorder_node_idxs = {data: idx for data, idx in enumerate(inorder)}

	preorder_iter = iter(preorder)

	def helper(start, end):
		if start > end:
			return None

		# Find current subtree root in inorder list
		root_val = next(preorder_iter)
		root = BinaryTreeNode()
		root.data = root_val
		root_idx = inorder_node_idxs[root_val]

		# In an inorder list, the left subtree ENDS at the left of the root,
		# and the right subtree STARTS at the right of the root.

		# Generate left subtree
		root.left = helper(start, root_idx - 1)

		# Generate right subtree
		root.right = helper(root_idx + 1, end)

		return root

	return helper(0, len(inorder) - 1)


if __name__ == '__main__':
	exit(
		generic_test.generic_test_main("tree_from_preorder_inorder.py",
									   'tree_from_preorder_inorder.tsv',
									   binary_tree_from_preorder_inorder))
