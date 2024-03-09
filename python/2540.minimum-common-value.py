#
# @lc app=leetcode id=2540 lang=python3
#
# [2540] Minimum Common Value
#
# https://leetcode.com/problems/minimum-common-value/description/
#
# algorithms
# Easy (51.62%)
# Likes:    310
# Dislikes: 4
# Total Accepted:    32.1K
# Total Submissions: 62.5K
# Testcase Example:  '[1,2,3]\n[2,4]'
#
# Given two integer arrays nums1 and nums2, sorted in non-decreasing order,
# return the minimum integer common to both arrays. If there is no common
# integer amongst nums1 and nums2, return -1.
# 
# Note that an integer is said to be common to nums1 and nums2 if both arrays
# have at least one occurrence of that integer.
# 
# 
# Example 1:
# 
# 
# Input: nums1 = [1,2,3], nums2 = [2,4]
# Output: 2
# Explanation: The smallest element common to both arrays is 2, so we return
# 2.
# 
# 
# Example 2:
# 
# 
# Input: nums1 = [1,2,3,6], nums2 = [2,3,4,5]
# Output: 2
# Explanation: There are two common elements in the array 2 and 3 out of which
# 2 is the smallest, so 2 is returned.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums1.length, nums2.length <= 10^5
# 1 <= nums1[i], nums2[j] <= 10^9
# Both nums1 and nums2 are sorted in non-decreasing order.
# 
# 
#

# @lc code=start
class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        i, j = 0, 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                return nums1[i]

            while i + 1 < len(nums1) and nums1[i] == nums1[i + 1]:
                i += 1

            while j + 1 < len(nums2) and nums2[j] == nums2[j + 1]:
                j += 1

            if nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1

        return -1
# @lc code=end