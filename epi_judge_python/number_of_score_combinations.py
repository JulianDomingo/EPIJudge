from test_framework import generic_test


def num_combinations_for_final_score(final_score, individual_play_scores):
	# O(s * N), where s = number of score types, N = final_score

	# There is only 1 possible combination to achieve a score of 0.
	dp = [[1] + [0] * final_score for _ in range(len(individual_play_scores))]

	for i in range(len(individual_play_scores)):
		for j in range(1, final_score + 1):
			# T(N) = T(N - 1) + T(N - indiv_score_i)

			# T(N - 1) - not including current score i
			without_score_i = dp[i - 1][j] if i >= 1 else 0

			# T(N - indiv_score_i) - including current score i
			with_score_i = (dp[i][j - individual_play_scores[i]] if
							j - individual_play_scores[i] >= 0 else 0)

			dp[i][j] = with_score_i + without_score_i

	# By memoization, total combinations using all scoring types is in the
	# bottom right of the DP matrix.
	return dp[-1][-1]


if __name__ == '__main__':
	exit(
		generic_test.generic_test_main("number_of_score_combinations.py",
									   "number_of_score_combinations.tsv",
									   num_combinations_for_final_score))
