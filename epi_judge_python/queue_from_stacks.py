from test_framework import generic_test


class Queue:
	# Using stacks, one holds all elements enqueued. When we dequeue, we must
	# pop everything from the stack and place it in a temp stack.
	#
	# The primary problem with this approach is there is no point in placing
	# the elements from temp stack BACK to elems stack, as every subsequent
	# dequeue after the first is trivial if popped from the temp stack (until
	# the temp stack is empty)
	#
	def __init__(self):
		self.elems = []
		self.temp = []


	def enqueue(self, x):
		self.elems.append(x)


	def dequeue(self):
		if not len(self.elems) and not len(self.temp):
			raise IndexError('Queue is empty!')

		if not len(self.temp):
			# No existing elements in temp, push them to temp so subsequent
			# dequeues can take O(1) time
			while len(self.elems):
				self.temp.append(self.elems.pop())

		return self.temp.pop()


def queue_tester(ops):
	from test_framework.test_failure import TestFailure

	try:
		q = Queue()

		for (op, arg) in ops:
			if op == 'Queue':
				q = Queue()
			elif op == 'enqueue':
				q.enqueue(arg)
			elif op == 'dequeue':
				result = q.dequeue()
				if result != arg:
					raise TestFailure("Dequeue: expected " + str(arg) +
									  ", got " + str(result))
			else:
				raise RuntimeError("Unsupported queue operation: " + op)
	except IndexError:
		raise TestFailure('Unexpected IndexError exception')


if __name__ == '__main__':
	exit(
		generic_test.generic_test_main("queue_from_stacks.py",
									   'queue_from_stacks.tsv', queue_tester))
