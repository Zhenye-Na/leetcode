#
# @lc app=leetcode id=1545 lang=python3
#
# [1545] Find Kth Bit in Nth Binary String
#
# https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/description/
#
# algorithms
# Medium (59.30%)
# Likes:    1123
# Dislikes: 69
# Total Accepted:    75.4K
# Total Submissions: 116.3K
# Testcase Example:  '3\n1'
#
# Given two positive integers n and k, the binary string Sn is formed as
# follows:
#
#
# S1 = "0"
# Si = Si - 1 + "1" + reverse(invert(Si - 1)) for i > 1
#
#
# Where + denotes the concatenation operation, reverse(x) returns the reversed
# string x, and invert(x) inverts all the bits in x (0 changes to 1 and 1
# changes to 0).
#
# For example, the first four strings in the above sequence are:
#
#
# S1 = "0"
# S2 = "011"
# S3 = "0111001"
# S4 = "011100110110001"
#
#
# Return the k^th bit in Sn. It is guaranteed that k is valid for the given
# n.
#
#
# Example 1:
#
#
# Input: n = 3, k = 1
# Output: "0"
# Explanation: S3 is "0111001".
# The 1^st bit is "0".
#
#
# Example 2:
#
#
# Input: n = 4, k = 11
# Output: "1"
# Explanation: S4 is "011100110110001".
# The 11^th bit is "1".
#
#
#
# Constraints:
#
#
# 1 <= n <= 20
# 1 <= k <= 2^n - 1
#
#
#


# @lc code=start
class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        full_string = self.generate_string(n)

        return full_string[k - 1]

    def invert(self, s: str) -> str:
        return "".join("1" if char == "0" else "0" for char in s)

    def generate_string(self, n: int) -> str:
        if n == 1:
            return "0"

        prev = self.generate_string(n - 1)

        return prev + "1" + self.invert(prev)[::-1]

# @lc code=end
