#
# @lc app=leetcode id=123 lang=python3
#
# [123] Best Time to Buy and Sell Stock III
#
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/description/
#
# algorithms
# Hard (39.74%)
# Likes:    3278
# Dislikes: 85
# Total Accepted:    277.6K
# Total Submissions: 695.1K
# Testcase Example:  '[3,3,5,0,0,3,1,4]'
#
# Say you have an array for which the i^th element is the price of a given
# stock on day i.
# 
# Design an algorithm to find the maximum profit. You may complete at most two
# transactions.
# 
# Note: You may not engage in multiple transactions at the same time (i.e., you
# must sell the stock before you buy again).
# 
# 
# Example 1:
# 
# 
# Input: prices = [3,3,5,0,0,3,1,4]
# Output: 6
# Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit =
# 3-0 = 3.
# Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 =
# 3.
# 
# Example 2:
# 
# 
# Input: prices = [1,2,3,4,5]
# Output: 4
# Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit =
# 5-1 = 4.
# Note that you cannot buy on day 1, buy on day 2 and sell them later, as you
# are engaging multiple transactions at the same time. You must sell before
# buying again.
# 
# 
# Example 3:
# 
# 
# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max profit = 0.
# 
# 
# Example 4:
# 
# 
# Input: prices = [1]
# Output: 0
# 
# 
# 
# Constraints:
# 
# 
# 1 <= prices.length <= 10^5
# 0 <= prices[i] <= 10^5
# 
# 
#

# @lc code=start

# Dynamic_Programming
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # initialization
        # there are four states
        #   buy stock 1, sell stock 1, buy stock 2, sell stock2
        dp = [[0 for _ in range(4)] for _ in range(len(prices))]
        dp[0][0] = -prices[0]
        dp[0][2] = -prices[0]

        for i in range(1, len(prices)):
            dp[i][0] = max(0            - prices[i], dp[i - 1][0])
            dp[i][1] = max(dp[i - 1][0] + prices[i], dp[i - 1][1])
            dp[i][2] = max(dp[i - 1][1] - prices[i], dp[i - 1][2])
            dp[i][3] = max(dp[i - 1][2] + prices[i], dp[i - 1][3])

        return max(dp[-1])



# Forward and Backward traversal
# Time O(n)
# Space O(n)
class Solution_TwoPass:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) == 0:
            return 0

        l = len(prices)
        forward_profits, backward_profits = [0] * l, [0] * l

        min_price = prices[0]
        for i in range(l):
            min_price = min(prices[i], min_price)
            forward_profits[i] = max(forward_profits[i - 1], prices[i] - min_price)

        max_price = prices[-1]
        for j in range(l - 2, -1, -1):
            max_price = max(prices[j], max_price)
            backward_profits[j] = max(max_price - prices[j], backward_profits[j + 1])

        max_profit = 0
        for i in range(l):
            max_profit = max(max_profit, forward_profits[i] + backward_profits[i])

        return max_profit
# @lc code=end

