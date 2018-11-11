from test_framework import generic_test


def preorder_traversal(tree):
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
				tree = tree.right
			else:
				ip.right = tree
				res.append(tree.data)
				tree = tree.left

	return res


if __name__ == '__main__':
	exit(
		generic_test.generic_test_main("tree_preorder.py", 'tree_preorder.tsv',
									   preorder_traversal))
