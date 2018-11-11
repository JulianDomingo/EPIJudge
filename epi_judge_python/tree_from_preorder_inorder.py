from test_framework import generic_test
from binary_tree_node import BinaryTreeNode


def binary_tree_from_preorder_inorder(preorder, inorder):
	if inorder:
		root_idx = inorder.index(preorder.pop(0))
		root = BinaryTreeNode(data=inorder[root_idx])

		# For an inorder serialized list, the left subtree of the current root
		# is always to the left of the index of current root, and the right
		# subtree of the current root is always to the right of the index + 1
		# of the current root
		root.left = binary_tree_from_preorder_inorder(preorder, inorder[:root_idx])
		root.right = binary_tree_from_preorder_inorder(preorder, inorder[root_idx + 1:])

		return root


if __name__ == '__main__':
	exit(
		generic_test.generic_test_main("tree_from_preorder_inorder.py",
									   'tree_from_preorder_inorder.tsv',
									   binary_tree_from_preorder_inorder))
