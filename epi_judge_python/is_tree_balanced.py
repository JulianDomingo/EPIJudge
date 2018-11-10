from test_framework import generic_test

#
#	  1
#	 /
#	2
#
#	  1
#	 / \
#	2	3

#
#	  1
#	 / \
#	3	4
#  /
# 2
#
#
#
#


def is_balanced_binary_tree(tree):
	if not tree:
		return True

	height, is_bal = helper(tree)

	return is_bal


def helper(root):
	if not root:
		return 0, True

	left_h, left_is_bal = helper(root.left)
	right_h, right_is_bal = helper(root.right)

	if not left_is_bal or not right_is_bal:
		return 0, False

	is_bal = abs(left_h - right_h) <= 1
	return max(left_h, right_h) + 1, is_bal






if __name__ == '__main__':
	exit(
		generic_test.generic_test_main("is_tree_balanced.py",
									   'is_tree_balanced.tsv',
									   is_balanced_binary_tree))
