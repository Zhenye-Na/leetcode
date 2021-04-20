#
# @lc app=leetcode id=309 lang=python3
#
# [309] Best Time to Buy and Sell Stock with Cooldown
#
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/description/
#
# algorithms
# Medium (48.06%)
# Likes:    3499
# Dislikes: 112
# Total Accepted:    187.5K
# Total Submissions: 388.6K
# Testcase Example:  '[1,2,3,0,2]'
#
# You are given an array prices where prices[i] is the price of a given stock
# on the i^th day.
# 
# Find the maximum profit you can achieve. You may complete as many
# transactions as you like (i.e., buy one and sell one share of the stock
# multiple times) with the following restrictions:
# 
# 
# After you sell your stock, you cannot buy stock on the next day (i.e.,
# cooldown one day).
# 
# 
# Note: You may not engage in multiple transactions simultaneously (i.e., you
# must sell the stock before you buy again).
# 
# 
# Example 1:
# 
# 
# Input: prices = [1,2,3,0,2]
# Output: 3
# Explanation: transactions = [buy, sell, cooldown, buy, sell]
# 
# 
# Example 2:
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
# 1 <= prices.length <= 5000
# 0 <= prices[i] <= 1000
# 
# 
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # initialization
        profits = [[0 for _ in range(3)] for _ in range(len(prices))]

        # three states:
        #   hold, rest, sold
        profits[0][0] = - prices[0]
        profits[0][1] = 0
        profits[0][2] = 0

        for i in range(1, len(prices)):
            profits[i][0] = max(profits[i - 1][0], profits[i - 1][1] - prices[i])  # hold
            profits[i][1] = max(profits[i - 1][1], profits[i - 1][2])              # rest
            profits[i][2] = profits[i - 1][0] + prices[i]                          # sold

        return max(profits[-1])
# @lc code=end

