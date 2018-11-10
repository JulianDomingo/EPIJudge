from test_framework import generic_test
from test_framework.test_failure import TestFailure


class Queue:
	SCALE_FACTOR = 2

	def __init__(self, capacity):
		self.a = [None] * capacity
		self.head = self.tail = self.cur_size = 0
		return


	def enqueue(self, x):
		# [1, 1, 1, 1]
		if self.cur_size == len(self.a):
			# Double capacity
			self.a = self.a[self.head:] + self.a[:self.head]
			self.head, self.tail = 0, self.cur_size
			self.a += [None] * (len(self.a) * Queue.SCALE_FACTOR - len(self.a))

		self.a[self.tail] = x
		self.tail = (self.tail + 1) % len(self.a)
		self.cur_size += 1

		return


	def dequeue(self):
		if not self.cur_size:
			raise IndexError('Empty queue!')

		self.cur_size -= 1
		to_return = self.a[self.head]
		self.head = (self.head + 1) % len(self.a)

		return to_return


	def size(self):
		return self.cur_size


def queue_tester(ops):
	q = Queue(1)

	for (op, arg) in ops:
		if op == 'Queue':
			q = Queue(arg)
		elif op == 'enqueue':
			q.enqueue(arg)
		elif op == 'dequeue':
			result = q.dequeue()
			if result != arg:
				raise TestFailure(
					"Dequeue: expected " + str(arg) + ", got " + str(result))
		elif op == 'size':
			result = q.size()
			if result != arg:
				raise TestFailure(
					"Size: expected " + str(arg) + ", got " + str(result))
		else:
			raise RuntimeError("Unsupported queue operation: " + op)


if __name__ == '__main__':
	exit(
		generic_test.generic_test_main("circular_queue.py",
									   'circular_queue.tsv', queue_tester))
