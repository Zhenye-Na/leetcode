#
# @lc app=leetcode id=1458 lang=python3
#
# [1458] Max Dot Product of Two Subsequences
#
# https://leetcode.com/problems/max-dot-product-of-two-subsequences/description/
#
# algorithms
# Hard (47.44%)
# Likes:    963
# Dislikes: 20
# Total Accepted:    30.7K
# Total Submissions: 58.1K
# Testcase Example:  '[2,1,-2,5]\n[3,0,-6]'
#
# Given two arrays nums1 and nums2.
# 
# Return the maximum dot product between non-empty subsequences of nums1 and
# nums2 with the same length.
# 
# A subsequence of a array is a new array which is formed from the original
# array by deleting some (can be none) of the characters without disturbing the
# relative positions of the remaining characters. (ie, [2,3,5] is a subsequence
# of [1,2,3,4,5] while [1,5,3] is not).
# 
# 
# Example 1:
# 
# 
# Input: nums1 = [2,1,-2,5], nums2 = [3,0,-6]
# Output: 18
# Explanation: Take subsequence [2,-2] from nums1 and subsequence [3,-6] from
# nums2.
# Their dot product is (2*3 + (-2)*(-6)) = 18.
# 
# Example 2:
# 
# 
# Input: nums1 = [3,-2], nums2 = [2,-6,7]
# Output: 21
# Explanation: Take subsequence [3] from nums1 and subsequence [7] from nums2.
# Their dot product is (3*7) = 21.
# 
# Example 3:
# 
# 
# Input: nums1 = [-1,-1], nums2 = [1,1]
# Output: -1
# Explanation: Take subsequence [-1] from nums1 and subsequence [1] from nums2.
# Their dot product is -1.
# 
# 
# Constraints:
# 
# 
# 1 <= nums1.length, nums2.length <= 500
# -1000 <= nums1[i], nums2[i] <= 1000
# 
# 
#

# @lc code=start
class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:

        # dp[i][j] represents the max dot product of nums1[:i] and nums2[:j]
        nums1 = ["#"] + nums1
        nums2 = ["#"] + nums2
        dp = [[-float('inf') for _ in range(len(nums2))] for _ in range(len(nums1))]

        for i in range(1, len(nums1)):
            for j in range(1, len(nums2)):
                dp[i][j] = max(
                    dp[i - 1][j],
                    dp[i][j - 1],
                    dp[i - 1][j - 1],
                    dp[i - 1][j - 1] + nums1[i] * nums2[j],
                    nums1[i] * nums2[j]
                )

        return dp[-1][-1]
# @lc code=end

