#
# @lc app=leetcode id=258 lang=python3
#
# [258] Add Digits
#
# https://leetcode.com/problems/add-digits/description/
#
# algorithms
# Easy (59.28%)
# Likes:    1763
# Dislikes: 1499
# Total Accepted:    408.6K
# Total Submissions: 673K
# Testcase Example:  '38'
#
# Given an integer num, repeatedly add all its digits until the result has only
# one digit, and return it.
# 
# 
# Example 1:
# 
# 
# Input: num = 38
# Output: 2
# Explanation: The process is
# 38 --> 3 + 8 --> 11
# 11 --> 1 + 1 --> 2 
# Since 2 has only one digit, return it.
# 
# 
# Example 2:
# 
# 
# Input: num = 0
# Output: 0
# 
# 
# 
# Constraints:
# 
# 
# 0 <= num <= 2^31 - 1
# 
# 
# 
# Follow up: Could you do it without any loop/recursion in O(1) runtime?
# 
#

# @lc code=start
class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        return 9 if num % 9 == 0 else num % 9
# @lc code=end

