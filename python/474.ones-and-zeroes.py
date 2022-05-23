#
# @lc app=leetcode id=474 lang=python3
#
# [474] Ones and Zeroes
#
# https://leetcode.com/problems/ones-and-zeroes/description/
#
# algorithms
# Medium (43.60%)
# Likes:    3255
# Dislikes: 346
# Total Accepted:    118.2K
# Total Submissions: 260.7K
# Testcase Example:  '["10","0001","111001","1","0"]\n5\n3'
#
# You are given an array of binary strings strs and two integers m and n.
# 
# Return the size of the largest subset of strs such that there are at most m
# 0's and n 1's in the subset.
# 
# A set x is a subset of a set y if all elements of x are also elements of
# y.
# 
# 
# Example 1:
# 
# 
# Input: strs = ["10","0001","111001","1","0"], m = 5, n = 3
# Output: 4
# Explanation: The largest subset with at most 5 0's and 3 1's is {"10",
# "0001", "1", "0"}, so the answer is 4.
# Other valid but smaller subsets include {"0001", "1"} and {"10", "1", "0"}.
# {"111001"} is an invalid subset because it contains 4 1's, greater than the
# maximum of 3.
# 
# 
# Example 2:
# 
# 
# Input: strs = ["10","0","1"], m = 1, n = 1
# Output: 2
# Explanation: The largest subset is {"0", "1"}, so the answer is 2.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= strs.length <= 600
# 1 <= strs[i].length <= 100
# strs[i] consists only of digits '0' and '1'.
# 1 <= m, n <= 100
# 
# 
#

# @lc code=start
from collections import Counter

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        f = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        for s in strs:
            zeros, ones = s.count("0"), s.count("1")

            for i in range(m, zeros - 1, -1):
                for j in range(n, ones - 1, -1):
                    f[i][j] = max(f[i][j], f[i - zeros][j - ones] + 1)

        return f[m][n]
# @lc code=end

