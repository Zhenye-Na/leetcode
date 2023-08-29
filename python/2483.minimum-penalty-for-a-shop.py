#
# @lc app=leetcode id=2483 lang=java
#
# [2483] Minimum Penalty for a Shop
#
# https://leetcode.com/problems/minimum-penalty-for-a-shop/description/
#
# algorithms
# Medium (51.12%)
# Likes:    104
# Dislikes: 1
# Total Accepted:    7.2K
# Total Submissions: 14.1K
# Testcase Example:  '"YYNY"'
#
# You are given the customer visit log of a shop represented by a 0-indexed
# string customers consisting only of characters 'N' and 'Y':
# 
# 
# if the i^th character is 'Y', it means that customers come at the i^th
# hour
# whereas 'N' indicates that no customers come at the i^th hour.
# 
# 
# If the shop closes at the j^th hour (0 <= j <= n), the penalty is calculated
# as follows:
# 
# 
# For every hour when the shop is open and no customers come, the penalty
# increases by 1.
# For every hour when the shop is closed and customers come, the penalty
# increases by 1.
# 
# 
# Return the earliest hour at which the shop must be closed to incur a minimum
# penalty.
# 
# Note that if a shop closes at the j^th hour, it means the shop is closed at
# the hour j.
# 
# 
# Example 1:
# 
# 
# Input: customers = "YYNY"
# Output: 2
# Explanation: 
# - Closing the shop at the 0^th hour incurs in 1+1+0+1 = 3 penalty.
# - Closing the shop at the 1^st hour incurs in 0+1+0+1 = 2 penalty.
# - Closing the shop at the 2^nd hour incurs in 0+0+0+1 = 1 penalty.
# - Closing the shop at the 3^rd hour incurs in 0+0+1+1 = 2 penalty.
# - Closing the shop at the 4^th hour incurs in 0+0+1+0 = 1 penalty.
# Closing the shop at 2^nd or 4^th hour gives a minimum penalty. Since 2 is
# earlier, the optimal closing time is 2.
# 
# 
# Example 2:
# 
# 
# Input: customers = "NNNNN"
# Output: 0
# Explanation: It is best to close the shop at the 0^th hour as no customers
# arrive.
# 
# Example 3:
# 
# 
# Input: customers = "YYYY"
# Output: 4
# Explanation: It is best to close the shop at the 4^th hour as customers
# arrive at each hour.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= customers.length <= 10^5
# customers consists only of characters 'Y' and 'N'.
# 
# 
#

# @lc code=start
class Solution_TwoPointers:
    def bestClosingTime(self, customers: str) -> int:

        if not customers or len(customers) == 0:
            return 0

        min_penalty, earliest_time = len(customers), len(customers)
        for i in range(len(customers) + 1):
            left, right = i - 1, i + 1
            curr_penalty = 0
            
            if 0 <= i < len(customers) and customers[i] == 'Y':
                curr_penalty += 1
            while left >= 0:
                if customers[left] == 'N':
                    curr_penalty += 1
                left -= 1
            while right < len(customers):
                if customers[right] == 'Y':
                    curr_penalty += 1
                right += 1
            
            if curr_penalty < min_penalty:
                min_penalty = curr_penalty
                earliest_time = i

        return earliest_time

class Solution:
    def bestClosingTime(self, customers: str) -> int:

        prefix_sum = self.getPrefixedSum(customers)
        suffix_sum = self.getSuffixedSum(customers)

        min_p, min_t = len(customers), len(customers)
        for i in range(len(customers) + 1):

            curr_p = prefix_sum[i] + (1 if 0 <= i < len(customers) and customers[i] == 'Y' else 0) + suffix_sum[len(customers)] - suffix_sum[i]

            if curr_p < min_p:
                min_p = curr_p
                min_t = i

        return min_t

    def getPrefixedSum(self, customers):
        prefix_sum = [0]
        for i in range(len(customers) + 1):
            if i >= len(customers):
                prefix_sum.append(prefix_sum[-1])
                continue

            if customers[i] == 'N':
                prefix_sum.append(prefix_sum[-1] + 1)
            else:
                prefix_sum.append(prefix_sum[-1])

        return prefix_sum

    def getSuffixedSum(self, customers):
        suffix_sum = [0]
        for i in range(len(customers)):
            if i >= len(customers):
                suffix_sum.append(suffix_sum[-1])
                continue

            if customers[i] == 'Y':
                suffix_sum.append(suffix_sum[-1] + 1)
            else:
                suffix_sum.append(suffix_sum[-1])

        return suffix_sum
#     Y   Y    N   Y
#   | 
#       |
#           | <- close here
#               |
#                     |
# prefix sum 0
# current value: 0
# suffix sum i + 1 1

# @lc code=end

