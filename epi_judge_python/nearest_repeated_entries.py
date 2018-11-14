from test_framework import generic_test
import sys


def find_nearest_repetition(paragraph):
	# Treat each entry as a key in dictionary, and value as index at which it
	# occurs. If we encounter the entry again, we take the absolute difference
	# between the two indices.
	# We constantly compare the closest 2 occurrences of any entry to ensure
	# we are checking the minimum distance across all entries that have a
	# frequency > 1.
	#
	# O(N) time, O(C) space where C is the number of unique entries in paragraph
	d = dict()
	min_dist = sys.maxsize

	for entry_idx, entry in enumerate(paragraph):
		if entry in d:
			# Get distance only if encountering the entry the second+ time
			min_dist = min(min_dist, entry_idx - d[entry][1])

			# Update the latest occurrence so subsequent findings of entry
			# compares against a new location
			d[entry][0] += 1
			d[entry][1] = entry_idx
		else:
			# (Frequency, Distance)
			d[entry] = [1, entry_idx]

	return min_dist if min_dist != sys.maxsize else -1




if __name__ == '__main__':
	exit(
		generic_test.generic_test_main("nearest_repeated_entries.py",
									   'nearest_repeated_entries.tsv',
									   find_nearest_repetition))
