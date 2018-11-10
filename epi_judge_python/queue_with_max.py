from test_framework import generic_test
from test_framework.test_failure import TestFailure
from collections import deque


class QueueWithMax:
	# There is no point in keeping previously record maxmiums if they are smaller
	# than a value we are about to enqueue in the enqueue() function. Thus, we
	# want to purge them from the maximums deque before appending the larger
	# value 'x'
	# To avoid having index errors though, we only remove a value from the
	# maximums deque if the value at the head of the maximums dequeu is EQUAL
	# to the current maximum. Otherwise, this indicates the value we're popping
	# was a value that we DID NOT record in our maximums deque.
	def __init__(self):
		self.deque = deque()
		self.maximums = deque()


	def enqueue(self, x):
		self.deque.append(x)

		if self.maximums:
			while self.maximums and self.maximums[-1] < x:
				self.maximums.pop()

		self.maximums.append(x)
		return


	def dequeue(self):
		if not self.deque:
			raise IndexError('Queue is empty!')

		if self.deque[0] == self.maximums[0]:
			self.maximums.popleft()

		return self.deque.popleft()


	def max(self):
		if not self.maximums:
			raise IndexError('Queue is empty!')

		return self.maximums[0]


def queue_tester(ops):

	try:
		q = QueueWithMax()

		for (op, arg) in ops:
			if op == 'QueueWithMax':
				q = QueueWithMax()
			elif op == 'enqueue':
				q.enqueue(arg)
			elif op == 'dequeue':
				result = q.dequeue()
				if result != arg:
					raise TestFailure("Dequeue: expected " + str(arg) +
									  ", got " + str(result))
			elif op == 'max':
				result = q.max()
				if result != arg:
					raise TestFailure(
						"Max: expected " + str(arg) + ", got " + str(result))
			else:
				raise RuntimeError("Unsupported queue operation: " + op)
	except IndexError:
		raise TestFailure('Unexpected IndexError exception')


if __name__ == '__main__':
	exit(
		generic_test.generic_test_main("queue_with_max.py",
									   'queue_with_max.tsv', queue_tester))
