#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#
# https://leetcode.com/problems/median-of-two-sorted-arrays/description/
#
# algorithms
# Hard (30.86%)
# Likes:    9316
# Dislikes: 1441
# Total Accepted:    872.2K
# Total Submissions: 2.8M
# Testcase Example:  '[1,3]\n[2]'
#
# Given two sorted arrays nums1 and nums2 of size m and n respectively, return
# the median of the two sorted arrays.
# 
# 
# Example 1:
# 
# 
# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.
# 
# 
# Example 2:
# 
# 
# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
# 
# 
# Example 3:
# 
# 
# Input: nums1 = [0,0], nums2 = [0,0]
# Output: 0.00000
# 
# 
# Example 4:
# 
# 
# Input: nums1 = [], nums2 = [1]
# Output: 1.00000
# 
# 
# Example 5:
# 
# 
# Input: nums1 = [2], nums2 = []
# Output: 2.00000
# 
# 
# 
# Constraints:
# 
# 
# nums1.length == m
# nums2.length == n
# 0 <= m <= 1000
# 0 <= n <= 1000
# 1 <= m + n <= 2000
# -10^6 <= nums1[i], nums2[i] <= 10^6
# 
# 
# 
# Follow up: The overall run time complexity should be O(log (m+n)).
#

# @lc code=start


class Solution_QuickSelect:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        nums = nums1[:] + nums2[:]
        length = len(nums)
        if length % 2 == 0:
            return (self._quick_select(nums, 0, length - 1, length // 2 + 1) + self._quick_select(nums, 0, length - 1, (length - 1) // 2 + 1)) / 2
        else:
            return self._quick_select(nums, 0, length - 1, length // 2 + 1)

    def _quick_select(self, nums, start, end, k):
        left, right = start, end
        pivot = nums[(left + right) // 2]

        while left <= right:
            while left <= right and nums[left] > pivot:
                left += 1
            while left <= right and nums[right] < pivot:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        if start + k - 1 <= right:
            return self._quick_select(nums, start, right, k)
        if start + k - 1 >= left:
            return self._quick_select(nums, left, end, k - (left - start))

        return nums[right + 1]


class Solution_BinarySearch:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)

        if (m + n) % 2 != 0:
            return self.findK(nums1, 0, nums2, 0, (m + n) // 2 + 1)
        else:
            return ( self.findK(nums1, 0, nums2, 0, (m + n) // 2) + self.findK(nums1, 0, nums2, 0, (m + n) // 2 + 1) ) / 2

    def findK(self, nums1, idx1, nums2, idx2, k):

        if idx1 >= len(nums1):
            return nums2[idx2 + k - 1]

        if idx2 >= len(nums2):
            return nums1[idx1 + k - 1]

        # base case
        if k == 1:
            return min(nums1[idx1], nums2[idx2])

        val1 = float('inf')
        val2 = float('inf')

        if idx1 + k // 2 - 1 < len(nums1):
            val1 = nums1[idx1 + k // 2 - 1]
        
        if idx2 + k // 2 - 1 < len(nums2):
            val2 = nums2[idx2 + k // 2 - 1]

        if val1 > val2:
            return self.findK(nums1, idx1, nums2, idx2 + k // 2, k - (k // 2))
        else:
            return self.findK(nums1, idx1 + k // 2, nums2, idx2, k - (k // 2))


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)

        l1, l2 = len(nums1), len(nums2)
        left, right = 0, l1
        while left <= right:
            position_x = (left + right) // 2
            position_y = (l1 + l2 + 1) // 2 - position_x

            max_left_x = nums1[position_x - 1] if position_x != 0 else float('-inf')
            max_left_y = nums2[position_y - 1] if position_y != 0 else float('-inf')

            min_right_x = nums1[position_x] if position_x < l1 else float('inf')
            min_right_y = nums2[position_y] if position_y < l2 else float('inf')

            if (max_left_x <= min_right_y and max_left_y <= min_right_x):
                # we found the partition
                if (l1 + l2) % 2 == 0:
                    return (max(max_left_x, max_left_y) + min(min_right_x, min_right_y)) / 2
                else:
                    return max(max_left_x, max_left_y)

            elif max_left_x > min_right_y:
                # we should move left
                right = position_x - 1

            else:
                left = position_x + 1

        return 0
# @lc code=end

