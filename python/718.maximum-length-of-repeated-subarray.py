#
# @lc app=leetcode id=718 lang=python3
#
# [718] Maximum Length of Repeated Subarray
#
# https://leetcode.com/problems/maximum-length-of-repeated-subarray/description/
#
# algorithms
# Medium (50.94%)
# Likes:    2640
# Dislikes: 63
# Total Accepted:    123.6K
# Total Submissions: 241K
# Testcase Example:  '[1,2,3,2,1]\n[3,2,1,4,7]'
#
# Given two integer arrays nums1 and nums2, return the maximum length of a
# subarray that appears in both arrays.
# 
# 
# Example 1:
# 
# 
# Input: nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]
# Output: 3
# Explanation: The repeated subarray with maximum length is [3,2,1].
# 
# 
# Example 2:
# 
# 
# Input: nums1 = [0,0,0,0,0], nums2 = [0,0,0,0,0]
# Output: 5
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums1.length, nums2.length <= 1000
# 0 <= nums1[i], nums2[i] <= 100
# 
# 
#

# @lc code=start
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:        
        nums1 = ["#"] + nums1
        nums2 = ["#"] + nums2
        max_len = 0

        # dp initialization
        # f[i][j] represents the length of the maximum length of
        # a subarray that appears in nums1[i:], nums2[j:]
        l1, l2 = len(nums1), len(nums2)
        f = [[0 for _ in range(l2)] for _ in range(l1)]
        
        for i in range(1, l1):
            for j in range(1, l2):
                if nums1[i] == nums2[j]:
                    f[i][j] = f[i - 1][j - 1] + 1

                    max_len = max(max_len, f[i][j])
                    
        return max_len
# @lc code=end

