#
# @lc app=leetcode id=89 lang=python3
#
# [89] Gray Code
#
# https://leetcode.com/problems/gray-code/description/
#
# algorithms
# Medium (51.23%)
# Likes:    1007
# Dislikes: 1952
# Total Accepted:    198.2K
# Total Submissions: 377K
# Testcase Example:  '2'
#
# An n-bit gray code sequence is a sequence of 2^n integers where:
# 
# 
# Every integer is in the inclusive range [0, 2^n - 1],
# The first integer is 0,
# An integer appears no more than once in the sequence,
# The binary representation of every pair of adjacent integers differs by
# exactly one bit, and
# The binary representation of the first and last integers differs by exactly
# one bit.
# 
# 
# Given an integer n, return any valid n-bit gray code sequence.
# 
# 
# Example 1:
# 
# 
# Input: n = 2
# Output: [0,1,3,2]
# Explanation:
# The binary representation of [0,1,3,2] is [00,01,11,10].
# - 00 and 01 differ by one bit
# - 01 and 11 differ by one bit
# - 11 and 10 differ by one bit
# - 10 and 00 differ by one bit
# [0,2,3,1] is also a valid gray code sequence, whose binary representation is
# [00,10,11,01].
# - 00 and 10 differ by one bit
# - 10 and 11 differ by one bit
# - 11 and 01 differ by one bit
# - 01 and 00 differ by one bit
# 
# 
# Example 2:
# 
# 
# Input: n = 1
# Output: [0,1]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 16
# 
# 
#

# @lc code=start
class Solution:
    def grayCode(self, n: int) -> List[int]:
        gray_code = [0]
        if n == 0:
            return gray_code

        for i in range(n):
            length = len(gray_code)
            for j in range(length - 1, -1, -1):
                gray_code.append( gray_code[j] | (1 << i) )

        return gray_code
# @lc code=end

# 16/16 cases passed (104 ms)
# Your runtime beats 83.07 % of python3 submissions
# Your memory usage beats 66.48 % of python3 submissions (21.5 MB)
