#
# @lc app=leetcode id=1186 lang=python3
#
# [1186] Maximum Subarray Sum with One Deletion
#
# https://leetcode.com/problems/maximum-subarray-sum-with-one-deletion/description/
#
# algorithms
# Medium (38.55%)
# Likes:    754
# Dislikes: 29
# Total Accepted:    21.2K
# Total Submissions: 54.7K
# Testcase Example:  '[1,-2,0,3]'
#
# Given an array of integers, return the maximum sum for a non-empty subarray
# (contiguous elements) with at most one element deletion. In other words, you
# want to choose a subarray and optionally delete one element from it so that
# there is still at least one element left and the sum of the remaining
# elements is maximum possible.
# 
# Note that the subarray needs to be non-empty after deleting one element.
# 
# 
# Example 1:
# 
# 
# Input: arr = [1,-2,0,3]
# Output: 4
# Explanation: Because we can choose [1, -2, 0, 3] and drop -2, thus the
# subarray [1, 0, 3] becomes the maximum value.
# 
# Example 2:
# 
# 
# Input: arr = [1,-2,-2,3]
# Output: 3
# Explanation: We just choose [3] and it's the maximum sum.
# 
# 
# Example 3:
# 
# 
# Input: arr = [-1,-1,-1,-1]
# Output: -1
# Explanation: The final subarray needs to be non-empty. You can't choose [-1]
# and delete -1 from it, then get an empty subarray to make the sum equals to
# 0.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= arr.length <= 10^5
# -10^4 <= arr[i] <= 10^4
# 
# 
#

# @lc code=start
class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        if not arr or len(arr) == 0:
            return 0

        n = len(arr)

        # initialization
        # f[i][0] represents we keep arr[i] in the selected subarray, ended with arr[i]
        # f[i][1] represents we drop arr[i] in the selected subarray
        f = [[-sys.maxsize for _ in range(2)] for _ in range(n)]
        f[0][0] = arr[0]

        for i in range(1, n):
            f[i][0] = max(f[i - 1][0] + arr[i], arr[i])
            f[i][1] = max(f[i - 1][0] + 0, f[i - 1][1] + arr[i])

        return max([max(_f) for _f in f])
# @lc code=end

