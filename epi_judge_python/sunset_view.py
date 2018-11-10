from test_framework import generic_test
from collections import namedtuple

def examine_buildings_with_sunset(sequence):
	Building = namedtuple('Building', ('idx', 'height'))
	can_view = []

	for idx, cur_build_height in enumerate(sequence):
		while can_view and can_view[-1].height <= cur_build_height:
			can_view.pop()
		can_view.append(Building(idx, cur_build_height))

	# We reversed list since we MUST return in the order from West -> East.
	# However, the list was given to us in the order from East -> West.
	return [building.idx for building in reversed(can_view)]


def examine_buildings_with_sunset_wrapper(sequence):
	return examine_buildings_with_sunset(iter(sequence))


if __name__ == '__main__':
	exit(
		generic_test.generic_test_main("sunset_view.py", 'sunset_view.tsv',
									   examine_buildings_with_sunset))
