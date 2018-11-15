from test_framework import generic_test
import collections


def find_all_substrings(s, words):
	def match_all_words(start_idx):
		string_to_freq = collections.Counter()

		# Step size of UNIT_SIZE since we are looking for the concatenations
		for i in range(start_idx, start_idx + len(words) * UNIT_SIZE, UNIT_SIZE):
			cur_word = s[i:i + UNIT_SIZE]
			freq = word_to_freq[cur_word]
			if not freq:
				# cur_word not in 'words' dictionary, so a concatenation including
				# this word starting at index 'start_idx' is not possible!
				return False
			else:
				string_to_freq[cur_word] += 1
				if string_to_freq[cur_word] > freq:
					# cur_word occurs too many times for a match to be possible
					# (Recall this problem indicated there may be duplicates of
					# a particular word in 'words' set)
					return False

		return True

	word_to_freq = collections.Counter(words)
	UNIT_SIZE = len(words[0])

	# Problem stated to return the starting index of all concatenation substrings
	return [
		# No point in going any further than range parameter since the substring
		# would be too large if it extended past this max range
		i for i in range(len(s) - UNIT_SIZE * len(words) + 1)
		if match_all_words(i)
	]


if __name__ == '__main__':
	exit(
		generic_test.generic_test_main(
			"string_decompositions_into_dictionary_words.py",
			'string_decompositions_into_dictionary_words.tsv',
			find_all_substrings))
