#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#
# https://leetcode.com/problems/coin-change/description/
#
# algorithms
# Medium (36.98%)
# Likes:    6540
# Dislikes: 190
# Total Accepted:    614.2K
# Total Submissions: 1.6M
# Testcase Example:  '[1,2,5]\n11'
#
# You are given an integer array coins representing coins of different
# denominations and an integer amount representing a total amount of money.
# 
# Return the fewest number of coins that you need to make up that amount. If
# that amount of money cannot be made up by any combination of the coins,
# return -1.
# 
# You may assume that you have an infinite number of each kind of coin.
# 
# 
# Example 1:
# 
# 
# Input: coins = [1,2,5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1
# 
# 
# Example 2:
# 
# 
# Input: coins = [2], amount = 3
# Output: -1
# 
# 
# Example 3:
# 
# 
# Input: coins = [1], amount = 0
# Output: 0
# 
# 
# Example 4:
# 
# 
# Input: coins = [1], amount = 1
# Output: 1
# 
# 
# Example 5:
# 
# 
# Input: coins = [1], amount = 2
# Output: 2
# 
# 
# 
# Constraints:
# 
# 
# 1 <= coins.length <= 12
# 1 <= coins[i] <= 2^31 - 1
# 0 <= amount <= 10^4
# 
# 
#

# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not coins or len(coins) == 0 or amount == 0:
            return 0

        # dp initialization
        # f[i] represents the fewest number of coins that need to make up for $ i
        f = [sys.maxsize for _ in range(amount + 1)]
        f[0] = 0

        for i in range(1, len(f)):
            for coin in coins:
                if i >= coin and f[i - coin] != sys.maxsize:
                    f[i] = min(f[i], f[i - coin] + 1)

        return f[-1] if f[-1] != sys.maxsize else -1  
# @lc code=end

