def dutch_flag_partition(pivot_index, A):
	pivot_value = A[pivot_index]

	smaller, larger = 0, len(A) - 1

	for i in range(len(A)):
		if A[i] < pivot_value:
			A[i], A[smaller] = A[smaller], A[i]
			smaller += 1


	for j in reversed(range(len(A))):
		if A[j] > pivot_value:
			A[j], A[larger] = A[larger], A[j]
			larger -= 1

	print(str(A))

	return


A = [0, 1, 2, 0, 2, 1, 1]

dutch_flag_partition(2, A)

print(str(A))
