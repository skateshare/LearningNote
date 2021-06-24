"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing
a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit,
return 0.
"""

# method 1: brutal force , time complexity = O(N^2)
prices = [7,1,5,3,6,4]
def sol1(prices):
    res = 0
    for b in range(len(prices)-1):
        for s in range(b+1, len(prices)):
            res = max(res, prices[s]-prices[b])
    return res

print(sol1(prices))

# method 2 : use DP
def sol2(prices):
    res = 0
    diff = 0
    acc = 0
    for i in range(len(prices)-1):
        diff = prices[i+1] - prices[i]
        acc = max(0, acc + diff)
        res = max(res, acc, diff)
    return res

print(sol2(prices))


