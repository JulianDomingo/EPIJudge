from test_framework import generic_test


def inorder_traversal(tree):
	res = []

	while tree:
		if not tree.left:
			res.append(tree.data)
			tree = tree.right
		else:
			# Find inorder predecessor
			ip = tree.left
			while ip and ip.right and ip.right is not tree:
				ip = ip.right

			if ip.right is tree:
				ip.right = None
				res.append(tree.data)
				tree = tree.right
			else:
				ip.right = tree
				tree = tree.left

	return res


if __name__ == '__main__':
	exit(
		generic_test.generic_test_main("tree_inorder.py", 'tree_inorder.tsv',
									   inorder_traversal))
