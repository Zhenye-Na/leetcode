#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#
# https://leetcode.com/problems/sqrtx/description/
#
# algorithms
# Easy (34.89%)
# Likes:    1884
# Dislikes: 2286
# Total Accepted:    696.7K
# Total Submissions: 2M
# Testcase Example:  '4'
#
# Given a non-negative integer x, compute and return the square root of x.
# 
# Since the return type is an integer, the decimal digits are truncated, and
# only the integer part of the result is returned.
# 
# 
# Example 1:
# 
# 
# Input: x = 4
# Output: 2
# 
# 
# Example 2:
# 
# 
# Input: x = 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since the decimal part
# is truncated, 2 is returned.
# 
# 
# Constraints:
# 
# 
# 0 <= x <= 2^31 - 1
# 
# 
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 0:
            return -1
        if x == 0:
            return 0

        start, end = 1, x
        
        while start + 1 < end:
            
            mid = (end - start) // 2 + start
            mul = mid * mid

            if mul < x:
                start = mid
            elif mul > x:
                end = mid
            elif mul == x:
                return mid

        if start * start <= x:
            return start
        else:
            return end
# @lc code=end

