from test_framework import generic_test


def shortest_equivalent_path(path):
	# Delete names preceding a '..', if no name precedes a '..', then the '..'
	# is needed
	#
	# Natural to process the string from left-to-right, splitting on forward
	# slashes. We record directory and file names. Since names are processed in
	# a LIFO order, it is natural to store them in a stack.

	# If the string begins with '/', we CANNOT go up it, so we record that in
	# the stack (before iterating through the path name).

	stack = []

	# Account for absolute paths (starting with '/')
	if path[0] == '/':
		stack.append(path[0])

	for token in (token for token in path.split('/') if token not in ['.', '']):
		if token == '..':
			# Pop the preceding name, since it's unnecessary
			if not len(stack) or len(stack) > 0 and stack[-1] == '..':
				stack.append(token)
			elif stack[-1] == '/':
				raise ValueError('Path error!')
			else:
				stack.pop()
		else:
			stack.append(token)

	# Avoid extra '/'
	res = '/'.join(stack)
	if res.startswith('//'):
		res = res[1:]

	return res


if __name__ == '__main__':
	exit(
		generic_test.generic_test_main("directory_path_normalization.py",
									   'directory_path_normalization.tsv',
									   shortest_equivalent_path))
