#
# @lc app=leetcode id=2485 lang=python3
#
# [2485] Find the Pivot Integer
#
# https://leetcode.com/problems/find-the-pivot-integer/description/
#
# algorithms
# Easy (79.85%)
# Likes:    768
# Dislikes: 19
# Total Accepted:    89.8K
# Total Submissions: 109K
# Testcase Example:  '8'
#
# Given a positive integer n, find the pivot integer x such that:
# 
# 
# The sum of all elements between 1 and x inclusively equals the sum of all
# elements between x and n inclusively.
# 
# 
# Return the pivot integer x. If no such integer exists, return -1. It is
# guaranteed that there will be at most one pivot index for the given input.
# 
# 
# Example 1:
# 
# 
# Input: n = 8
# Output: 6
# Explanation: 6 is the pivot integer since: 1 + 2 + 3 + 4 + 5 + 6 = 6 + 7 + 8
# = 21.
# 
# 
# Example 2:
# 
# 
# Input: n = 1
# Output: 1
# Explanation: 1 is the pivot integer since: 1 = 1.
# 
# 
# Example 3:
# 
# 
# Input: n = 4
# Output: -1
# Explanation: It can be proved that no such integer exist.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 1000
# 
# 
#

# @lc code=start
class Solution:
    def pivotInteger(self, n: int) -> int:
        prefix_sums = self._computePrefixSum(n)
        suffix_sums = self._computeSuffixSum(n)

        for i in range(1, n + 1):
            if prefix_sums[i] == suffix_sums[n + 1 - i]:
                return i

        return -1

    def _computePrefixSum(self, n):
        prefix_sums = [0]
        for i in range(1, n + 1):
            prefix_sums.append(prefix_sums[-1] + i)

        return prefix_sums

    def _computeSuffixSum(self, n):
        suffix_sums = [0]
        for i in range(n, 0, -1):
            suffix_sums.append(suffix_sums[-1] + i)

        return suffix_sums
# @lc code=end

