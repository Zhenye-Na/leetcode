#
# @lc app=leetcode id=191 lang=python3
#
# [191] Number of 1 Bits
#
# https://leetcode.com/problems/number-of-1-bits/description/
#
# algorithms
# Easy (55.62%)
# Likes:    3284
# Dislikes: 824
# Total Accepted:    748.9K
# Total Submissions: 1.2M
# Testcase Example:  '00000000000000000000000000001011'
#
# Write a function that takes an unsigned integer and returns the number of '1'
# bits it has (also known as the Hamming weight).
# 
# Note:
# 
# 
# Note that in some languages, such as Java, there is no unsigned integer type.
# In this case, the input will be given as a signed integer type. It should not
# affect your implementation, as the integer's internal binary representation
# is the same, whether it is signed or unsigned.
# In Java, the compiler represents the signed integers using 2's complement
# notation. Therefore, in Example 3, the input represents the signed integer.
# -3.
# 
# 
# 
# Example 1:
# 
# 
# Input: n = 00000000000000000000000000001011
# Output: 3
# Explanation: The input binary string 00000000000000000000000000001011 has a
# total of three '1' bits.
# 
# 
# Example 2:
# 
# 
# Input: n = 00000000000000000000000010000000
# Output: 1
# Explanation: The input binary string 00000000000000000000000010000000 has a
# total of one '1' bit.
# 
# 
# Example 3:
# 
# 
# Input: n = 11111111111111111111111111111101
# Output: 31
# Explanation: The input binary string 11111111111111111111111111111101 has a
# total of thirty one '1' bits.
# 
# 
# 
# Constraints:
# 
# 
# The input must be a binary string of length 32.
# 
# 
# 
# Follow up: If this function is called many times, how would you optimize it?
#

# @lc code=start
class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            res += (n & 1)
            n = n >> 1

        return res


class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count("1")
# @lc code=end

