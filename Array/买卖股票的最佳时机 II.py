# 给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
# 设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。
# 注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。


def max_profit(prices):
    if prices is None:
        return 0

    begin_price = prices[0]
    result = 0
    for p in prices:
        if p > begin_price:
            result += p - begin_price
        begin_price = p

    return result


# best
def max_profit2(prices):
    total = 0
    for i in range(1, len(prices)):
        if prices[i - 1] < prices[i]:
            total += prices[i] - prices[i - 1]
    return total


print(max_profit2([1, 2, 3, 4, 5]))
