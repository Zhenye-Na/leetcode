#
# @lc app=leetcode id=367 lang=python3
#
# [367] Valid Perfect Square
#
# https://leetcode.com/problems/valid-perfect-square/description/
#
# algorithms
# Easy (42.01%)
# Likes:    1197
# Dislikes: 194
# Total Accepted:    266.6K
# Total Submissions: 631.4K
# Testcase Example:  '16'
#
# Given a positive integer num, write a function which returns True if num is a
# perfect square else False.
# 
# Follow up: Do not use any built-in library function such as sqrt.
# 
# 
# Example 1:
# Input: num = 16
# Output: true
# Example 2:
# Input: num = 14
# Output: false
# 
# 
# Constraints:
# 
# 
# 1 <= num <= 2^31 - 1
# 
# 
#

# @lc code=start
# Binary Search
#   O(log(n))
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        start, end = 1, num
        while start + 1 < end:
            mid = start + (end - start) // 2
            if mid * mid == num:
                return True
            elif mid * mid > num:
                end = mid
            else:
                start = mid

        return start * start == num or end * end == num


class Solution_Sqrt:
    def isPerfectSquare(self, num: int) -> bool:
        return int(sqrt(num)) == sqrt(num)
# @lc code=end

