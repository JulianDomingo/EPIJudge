from test_framework import generic_test


def sum_root_to_leaf(tree, partial_path_sum=0):
	res = [0]
	helper(0, res, tree)
	return res[0]


def helper(cur, res, root):
	if not root:
		return
	if leaf(root):
		cur <<= 1
		cur |= root.data
		res[0] += b2d(cur)
	else:
		cur <<= 1
		cur |= root.data
		helper(cur, res, root.left)
		helper(cur, res, root.right)


def b2d(val):
	res = 0
	exp = 0
	while val:
		res += (val & 1) << exp
		val >>= 1
		exp += 1

	return res


def leaf(cur):
	return not cur.left and not cur.right


if __name__ == '__main__':
	exit(
		generic_test.generic_test_main(
			"sum_root_to_leaf.py", 'sum_root_to_leaf.tsv', sum_root_to_leaf))
