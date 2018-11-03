import collections

from test_framework import generic_test
from test_framework.test_failure import PropertyName

Rectangle = collections.namedtuple('Rectangle', ('x', 'y', 'width', 'height'))


def intersect_rectangle(R1, R2):
	# First determine if an intersection exists.
	if (R1.x + R1.width  < R2.x or R2.y + R2.width	< R1.x or
		R1.y + R1.height < R2.y or R2.y + R2.height < R1.y):
		return Rectangle(0, 0, -1, -1)

	# We know an intersection exists at this point!



def intersect_rectangle_wrapper(R1, R2):
	return intersect_rectangle(Rectangle(*R1), Rectangle(*R2))


def res_printer(prop, value):
	def fmt(x):
		return [x[0], x[1], x[2], x[3]] if x else None

	if prop in (PropertyName.EXPECTED, PropertyName.RESULT):
		return fmt(value)
	else:
		return value


if __name__ == '__main__':
	exit(
		generic_test.generic_test_main(
			"rectangle_intersection.py",
			'rectangle_intersection.tsv',
			intersect_rectangle_wrapper,
			res_printer=res_printer))
