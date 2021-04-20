#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
#
# algorithms
# Easy (51.35%)
# Likes:    7743
# Dislikes: 346
# Total Accepted:    1.2M
# Total Submissions: 2.3M
# Testcase Example:  '[7,1,5,3,6,4]'
#
# You are given an array prices where prices[i] is the price of a given stock
# on the i^th day.
# 
# You want to maximize your profit by choosing a single day to buy one stock
# and choosing a different day in the future to sell that stock.
# 
# Return the maximum profit you can achieve from this transaction. If you
# cannot achieve any profit, return 0.
# 
# 
# Example 1:
# 
# 
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit =
# 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you
# must buy before you sell.
# 
# 
# Example 2:
# 
# 
# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit =
# 0.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= prices.length <= 10^5
# 0 <= prices[i] <= 10^4
# 
# 
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) == 0:
            return 0

        max_profit, min_price = 0, max(prices)
        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)

        return max_profit

# @lc code=end

