A =  [12, 14, 41, 74, 79, 22, 16, 11, 24, 76, 101, 27, 60, 31, 0, 13, 53, 90, 89, 1, 4, 85, 9, 77, 43, 93, 51, 86, 35, 5, 67, 71, 21, 46, 56, 95, 66, 19, 20, 44, 73, 91, 61, 69, 83, 34, 17, 29, 58, 78, 36, 49, 99, 38, 96, 40, 92, 37, 33, 15, 47, 5, 23, 3, 26, 64, 52, 81, 82, 8, 28, 25, 32, 65, 68, 70, 72, 94, 63, 7, 55, 10, 45, 100, 84, 2, 54, 98, 50, 39, 6, 88, 48, 97, 57, 59, 87, 62, 75, 30, 18, 42]

for i in range(len(A)):
	# Second boolean statement is important for incorrectly determining
	# duplicate
	if A[A[i]] == A[i] and i != A[i]:
		dup = A[i]

	tmp = A[i]
	A[i], A[tmp] = A[tmp], A[i]

print(A)


# def dutch_flag_partition(pivot_index, A):
	# pivot_value = A[pivot_index]

	# smaller, larger = 0, len(A) - 1

	# for i in range(len(A)):
		# if A[i] < pivot_value:
			# A[i], A[smaller] = A[smaller], A[i]
			# smaller += 1


	# for j in reversed(range(len(A))):
		# if A[j] > pivot_value:
			# A[j], A[larger] = A[larger], A[j]
			# larger -= 1

	# print(str(A))

	# return


# A = [0, 1, 2, 0, 2, 1, 1]

# dutch_flag_partition(2, A)

# print(str(A))

# def rabin_karp(t, s):
	# if len(s) > len(t):
		# return -1

	# # TODO: You were on right track, but ord() doesn't take into consideration
	# # ordering of the string. Use O(1) hashing of the string s and compare the
	# # hashing of the current len(s) size window. If hashes match, you found the
	# # result

	# # Find the first occurrence of string 's' in text 't'
	# # Sliding window lmao
	# n = len(s)
	# st, end = 0, n

	# # We get the ord() sum of 's'. When we traverse through the string with
	# # sliding window of size len(s), we add the ord() of the new window suffix
	# # and subtract the ord() of the window prefix
	# # The result is the index of "st"

	# # Ex. s='ACAIBOWL', t='BOWL'
	# s_ord = sum([ord(c) for c in s])

	# print('ord() of {}: {}'.format(s, str(s_ord)))

	# # We initialize our window to the first len(s) characters in the string t
	# cur_ord = sum([ord(c) for c in t[:n]])

	# if cur_ord == s_ord:
		# return 0

	# while end < len(t):
		# cur_ord -= ord(t[st])
		# cur_ord += ord(t[end])
		# st, end = st + 1, end + 1

		# print("Testing string {} with score {}".format(t[st:end], str(cur_ord)))

		# if cur_ord == s_ord:
			# return st

	# return -1

# t = 'babababbaabaabbbbb'
# s = 'babba'
# rabin_karp(t, s)
