from test_framework import generic_test


def buy_and_sell_stock_twice(prices):
	fw_min, bw_max = float('inf'), float('-inf')
	profit_list = [0] * len(prices)
	max_value = max_profit = 0

	# Compute max profit moving forward (1st day sale)
	for i, price in enumerate(prices):
		fw_min = min(fw_min, price)
		max_profit = max(max_profit, price - fw_min)
		profit_list[i] = max_profit

	# Compute max profit moving backward (2nd day sale)
	# Find maximum profit if we make the second buy on that day.
	for i in range(len(prices[:-1]), 1, -1):
		max_value = max(max_value, prices[i])
		max_profit = max(max_profit,
						 max_value - prices[i] + profit_list[i - 1])

	# Return max in profit_list (which contains merged sum from fw and bw iteration)
	return max_profit



# def buy_and_sell_stock_twice(prices):
	# if not prices or len(prices) <= 1:
		# return 0

	# max_profit = 0

	# for i in range(0, len(prices)):
		# max_profit = max(max_profit, find_profit(0, i, prices) + find_profit(i, len(prices), prices))

	# return max_profit


# def find_profit(s, e, prices):
	# max_loc, min_loc = 0, prices[s]

	# for i in range(s, e):
		# max_loc = max(max_loc, prices[i] - min_loc)
		# min_loc = min(min_loc, prices[i])

	# return max_loc


if __name__ == '__main__':
	exit(
		generic_test.generic_test_main("buy_and_sell_stock_twice.py",
									   "buy_and_sell_stock_twice.tsv",
									   buy_and_sell_stock_twice))
