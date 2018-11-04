from test_framework import generic_test


def plus_one(A):
	# In-place modification
	carry = 0

	for i in reversed(range(len(A))):
		if A[i] != 9:
			# Just increment regularly
			A[i] += 1
			carry &= 0
			break

		else:
			A[i] = 0
			carry |= 1

	# Check if the MSD ended up having a carry over. If it did, need to add a
	# new MSD of value 1
	if carry:
		A.insert(0, 1)

	return A



if __name__ == '__main__':
	exit(
		generic_test.generic_test_main("int_as_array_increment.py",
									   "int_as_array_increment.tsv", plus_one))
