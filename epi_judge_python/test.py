A = [64, 249, 366, 449, 198, 291, 51, 136, 251, 374, 410, 429, 302, 182, 282, 32, 139, 184, 35, 278, 364, 132, 484, 174, 62, 189, 236, 144, 246, 99, 312, 317, 310, 145, 377, 12, 173, 318, 350, 0, 273, 99, 73, 495, 323, 48, 473, 269, 3, 14, 425, 213, 419, 420, 296, 375, 373, 103, 458, 290, 8, 262, 270, 458, 103, 380, 147, 30, 442, 24, 59, 153, 357, 77, 143, 376, 504, 412, 236, 5, 95, 475, 246, 315, 189, 271, 115, 143, 464, 422, 467, 242, 183, 442, 159, 349, 491, 212, 426, 246, 269, 155, 276, 314, 404, 50, 112, 271, 496, 238, 476, 283, 178, 494, 65, 105, 268, 115, 70, 243, 3, 88, 421, 327, 392, 303, 100, 6, 12, 51, 103, 312, 86, 83, 339, 128, 501, 214, 411, 84, 242, 492, 497, 159, 149, 112, 63, 126, 64, 400, 32, 378, 184, 199, 82, 131, 247, 344, 450, 418, 41, 101, 270, 164, 163, 205, 336, 338, 312, 421, 102, 113, 191, 271, 122, 119, 332, 157, 380, 274, 298, 241, 433, 112, 408, 302, 481, 261, 313, 227, 178, 155, 68, 301, 211, 102, 304, 358, 370, 3, 207, 99, 138, 427, 508, 252, 230, 3, 271, 434, 407, 52, 168, 58, 75, 179, 163, 206, 501, 60, 136, 139, 195, 56, 412, 449, 333, 416, 248, 467, 73, 483, 490, 316, 432, 255, 268, 124, 226, 53, 426, 348, 21, 132, 55, 501, 242, 349, 447, 427, 495, 428, 100, 282, 72, 391, 139, 368, 216, 363, 244, 207, 169, 485, 396, 176, 208, 341, 232, 214, 237, 116, 221, 183, 368, 447, 181, 277, 253, 370, 250, 99, 362, 207, 110, 197, 103, 127, 161, 100, 437, 157, 312, 221, 336, 350, 79, 56, 150, 165, 53, 496, 311, 460, 152, 39, 154, 18, 459, 361, 46, 84, 246, 173, 2, 466, 336, 480, 382, 127, 332, 153, 425, 325, 239, 255, 116, 94, 140, 105, 52, 84, 452, 412, 81, 312, 146, 255, 51, 418, 321, 175, 129, 257, 412, 232, 338, 275, 66, 408, 401, 303, 90, 275, 292, 39, 52, 2, 411, 466, 236, 343, 437, 218, 455, 189, 315, 508, 309, 217, 15, 384, 105, 502, 148, 202, 479, 71, 377, 461, 497, 149, 319, 401, 195, 224, 252, 210, 333, 382, 111, 271, 169, 295, 87, 312, 441, 197, 235, 337, 140, 350, 380, 209, 370, 78, 186, 16, 95, 149, 126, 14, 498, 440, 356, 281, 347, 477, 345, 8, 0, 81, 290, 8, 268, 357, 0, 292, 153, 38, 394, 141, 230, 91, 218, 4, 445, 345, 393, 248, 248, 248, 57, 86, 142, 225, 174, 232, 344, 77, 254, 149, 67, 346, 105, 238, 142, 342, 65, 65, 275, 291, 196, 427, 215, 128, 507, 401, 190, 376, 219, 384, 281, 211, 142, 59, 235, 13, 34, 174, 463, 180, 135, 289, 254, 244, 23, 182, 272, 173, 108, 48, 493, 502, 295, 315, 181, 28, 85, 351, 253, 343, 222, 28, 102, 208, 12, 447]

def even_odd(A):
	next_even = 0

	for i in range(1, len(A)):
		if not A[i] & 1:
			# Found even, swap with next_even
			A[next_even], A[i] = A[i], A[next_even]
			next_even += 1


	for i in range(len(A)):
		A[i] = "odd" if A[i] & 1 else "even"

	for i in A:
		print(i)

	return

even_odd(A)
