#
# @lc app=leetcode id=1359 lang=python3
#
# [1359] Count All Valid Pickup and Delivery Options
#
# https://leetcode.com/problems/count-all-valid-pickup-and-delivery-options/description/
#
# algorithms
# Hard (55.48%)
# Likes:    667
# Dislikes: 88
# Total Accepted:    27.3K
# Total Submissions: 47.6K
# Testcase Example:  '1'
#
# Given n orders, each order consist in pickup and delivery services. 
# 
# Count all valid pickup/delivery possible sequences such that delivery(i) is
# always after of pickup(i). 
# 
# Since the answer may be too large, return it modulo 10^9 + 7.
# 
# 
# Example 1:
# 
# 
# Input: n = 1
# Output: 1
# Explanation: Unique order (P1, D1), Delivery 1 always is after of Pickup 1.
# 
# 
# Example 2:
# 
# 
# Input: n = 2
# Output: 6
# Explanation: All possible orders: 
# (P1,P2,D1,D2), (P1,P2,D2,D1), (P1,D1,P2,D2), (P2,P1,D1,D2), (P2,P1,D2,D1) and
# (P2,D2,P1,D1).
# This is an invalid order (P1,D2,P2,D1) because Pickup 2 is after of Delivery
# 2.
# 
# 
# Example 3:
# 
# 
# Input: n = 3
# Output: 90
# 
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 500
# 
# 
#

# @lc code=start
class Solution:
    def countOrders(self, n: int) -> int:
        # f[i] represents number combinations of i orders
        f = [0 for _ in range(n + 1)]
        f[0] = 1

        for i in range(1, n + 1):
            f[i] = (f[i - 1] * (2 * i - 1) * i) % (10 ** 9 + 7)

        return f[-1]


class Solution:
    def countOrders(self, n: int) -> int:

        # dp[i] means that number of sequence for total of i pick-ups and deliveries
        dp = [0 for _ in range(n)]
        dp[0] = 1

        for i in range(1, n):
            dp[i] = int((dp[i - 1] * (1 + 2 * i + 1) * (2 * i + 1) / 2) % (10 ** 9 + 7))

        return dp[-1]

# [p1 ... pi, d1 ... di]
#  pj   2 * i for dj
#       2i - 1
#       ..

#     1

#  ^  p3, P1, p3 P2,D2,D1  p3

class Solution:
    def countOrders(self, n: int) -> int:

        dp = [0 for _ in range(2)]
        dp[0] = 1

        for i in range(1, n):
            dp[i % 2] = int((dp[(i - 1) % 2] * (1 + 2 * i + 1) * (2 * i + 1) / 2) % (10 ** 9 + 7))

        return dp[(n + 1) % 2]
# @lc code=end

