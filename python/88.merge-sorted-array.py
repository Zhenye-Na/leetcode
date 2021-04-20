#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#
# https://leetcode.com/problems/merge-sorted-array/description/
#
# algorithms
# Easy (40.60%)
# Likes:    3453
# Dislikes: 5054
# Total Accepted:    815.3K
# Total Submissions: 2M
# Testcase Example:  '[1,2,3,0,0,0]\n3\n[2,5,6]\n3'
#
# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as
# one sorted array.
# 
# The number of elements initialized in nums1 and nums2 are m and n
# respectively. You may assume that nums1 has a size equal to m + n such that
# it has enough space to hold additional elements from nums2.
# 
# 
# Example 1:
# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# Example 2:
# Input: nums1 = [1], m = 1, nums2 = [], n = 0
# Output: [1]
# 
# 
# Constraints:
# 
# 
# nums1.length == m + n
# nums2.length == n
# 0 <= m, n <= 200
# 1 <= m + n <= 200
# -10^9 <= nums1[i], nums2[i] <= 10^9
# 
# 
#

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1 = len(nums1) - 1
        for p1 in range(len(nums1) - 1, -1, -1):
            if nums1[p1] != 0:
                break

        p2 = len(nums2) - 1
        right = len(nums1) - 1
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[right] = nums1[p1]
                p1 -= 1
            else:
                nums1[right] = nums2[p2]
                p2 -= 1
            right -= 1

        if p2 > 0:
            for r in range(right, -1, -1):
                nums1[right] = nums2[p2]
                p2 -= 1







# @lc code=end

