#
# @lc app=leetcode id=454 lang=python3
#
# [454] 4Sum II
#
# https://leetcode.com/problems/4sum-ii/description/
#
# algorithms
# Medium (54.53%)
# Likes:    1814
# Dislikes: 83
# Total Accepted:    155.6K
# Total Submissions: 284.9K
# Testcase Example:  '[1,2]\n[-2,-1]\n[-1,2]\n[0,2]'
#
# Given four lists A, B, C, D of integer values, compute how many tuples (i, j,
# k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.
# 
# To make problem a bit easier, all A, B, C, D have same length of N where 0 ≤
# N ≤ 500. All integers are in the range of -2^28 to 2^28 - 1 and the result is
# guaranteed to be at most 2^31 - 1.
# 
# Example:
# 
# 
# Input:
# A = [ 1, 2]
# B = [-2,-1]
# C = [-1, 2]
# D = [ 0, 2]
# 
# Output:
# 2
# 
# Explanation:
# The two tuples are:
# 1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
# 2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0
# 
# 
# 
# 
#

# @lc code=start
class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        if not A or not B or not C or not D:
            return 0

        sum_mapping = {}

        for i in range(len(A)):
            for j in range(len(B)):
                running_sum = A[i] + B[j]
                sum_mapping[-running_sum] = sum_mapping.get(-running_sum, 0) + 1  # value is how many ways to add up to - running_sum


        res = 0
        for i in range(len(C)):
            for j in range(len(D)):
                running_sum = C[i] + D[j]
                if running_sum in sum_mapping:
                    res += sum_mapping[running_sum]

        return res


# @lc code=end

