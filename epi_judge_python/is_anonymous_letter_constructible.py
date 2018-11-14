from test_framework import generic_test
from collections import Counter


def is_letter_constructible_from_magazine(letter_text, magazine_text):
	letter = Counter(letter_text)
	magazine = Counter(magazine_text)

	for letter_char, letter_freq in letter.items():
		if letter_char not in magazine or magazine[letter_char] < letter_freq:
			return False

	return True


if __name__ == '__main__':
	exit(
		generic_test.generic_test_main("is_anonymous_letter_constructible.py",
									   'is_anonymous_letter_constructible.tsv',
									   is_letter_constructible_from_magazine))
