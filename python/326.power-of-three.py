#
# @lc app=leetcode id=326 lang=python3
#
# [326] Power of Three
#
# https://leetcode.com/problems/power-of-three/description/
#
# algorithms
# Easy (42.06%)
# Likes:    146
# Dislikes: 21
# Total Accepted:    343.3K
# Total Submissions: 809.9K
# Testcase Example:  '27'
#
# Given an integer n, return true if it is a power of three. Otherwise, return
# false.
# 
# An integer n is a power of three, if there exists an integer x such that n ==
# 3^x.
# 
# 
# Example 1:
# Input: n = 27
# Output: true
# Example 2:
# Input: n = 0
# Output: false
# Example 3:
# Input: n = 9
# Output: true
# Example 4:
# Input: n = 45
# Output: false
# 
# 
# Constraints:
# 
# 
# -2^31 <= n <= 2^31 - 1
# 
# 
# 
# Follow up: Could you solve it without loops/recursion?
#

# @lc code=start
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        elif n == 1:
            return True
        elif n % 3 == 0:
            return self.isPowerOfThree(n // 3)
        
        return False
# @lc code=end

