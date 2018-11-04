from test_framework import generic_test


def buy_and_sell_stock_once(prices):
	cur_min, idx, res = prices[0], 1, 0.0

	for i in range(1, len(prices)):
		res = max(res, prices[i] - cur_min)
		cur_min = min(cur_min, prices[i])

	return res


if __name__ == '__main__':
	exit(
		generic_test.generic_test_main("buy_and_sell_stock.py",
									   "buy_and_sell_stock.tsv",
									   buy_and_sell_stock_once))
