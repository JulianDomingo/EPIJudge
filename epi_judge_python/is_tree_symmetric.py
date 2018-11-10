from test_framework import generic_test


def is_symmetric(tree):
	if not tree or not tree.left and not tree.right:
		return True

	return helper(tree.left, tree.right)


def helper(left, right):
	if not left and not right:
		# Reached end of checking, know we are symmetric
		return True

	# If only once is none, invalid symmetric
	if not left and right or left and not right:
		return False

	# Know we have 2 children at this point, so check their value and their
	# respective subtrees
	# Check if left's right subtree is equal to right's left subtree and vice
	# versa
	return (left.data == right.data and helper(left.left, right.right) and
										helper(left.right, right.left))


if __name__ == '__main__':
	exit(
		generic_test.generic_test_main("is_tree_symmetric.py",
									   'is_tree_symmetric.tsv', is_symmetric))
