from test_framework import generic_test
from test_framework.test_failure import TestFailure
from collections import OrderedDict


class LruCache:
	def __init__(self, capacity):
		self.cache = OrderedDict()
		self._capacity = capacity


	def lookup(self, isbn):
		if isbn not in self.cache:
			return -1
		else:
			# Update access and return initial value
			mru = self.cache[isbn]
			del self.cache[isbn]
			self.cache[isbn] = mru
			return mru


	def insert(self, isbn, price):
		if isbn in self.cache:
			mru = self.cache[isbn]
			del self.cache[isbn]
			self.cache[isbn] = mru
		elif len(self.cache) == self._capacity:
			self.cache.popitem(last=False)
			self.cache[isbn] = price
		else:
			self.cache[isbn] = price


	def erase(self, isbn):
		if isbn not in self.cache:
			return False

		del self.cache[isbn]
		return True


def run_test(commands):
	if len(commands) < 1 or commands[0][0] != 'LruCache':
		raise RuntimeError('Expected LruCache as first command')

	cache = LruCache(commands[0][1])

	for cmd in commands[1:]:
		if cmd[0] == 'lookup':
			result = cache.lookup(cmd[1])
			if result != cmd[2]:
				raise TestFailure(
					'Lookup: expected ' + str(cmd[2]) + ', got ' + str(result))
		elif cmd[0] == 'insert':
			cache.insert(cmd[1], cmd[2])
		elif cmd[0] == 'erase':
			result = 1 if cache.erase(cmd[1]) else 0
			if result != cmd[2]:
				raise TestFailure(
					'Erase: expected ' + str(cmd[2]) + ', got ' + str(result))
		else:
			raise RuntimeError('Unexpected command ' + cmd[0])


if __name__ == '__main__':
	exit(
		generic_test.generic_test_main("lru_cache.py", 'lru_cache.tsv',
									   run_test))
