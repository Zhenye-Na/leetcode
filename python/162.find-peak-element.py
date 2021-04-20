#
# @lc app=leetcode id=162 lang=python3
#
# [162] Find Peak Element
#


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        start, end = 0, len(nums) - 1
        while (start + 1 < end):
            P = (start + end) // 2

            # A[mid] is one of peaks
            if nums[P] > nums[P - 1] and nums[P] > nums[P + 1]:
                return P
            # Ascending area
            elif nums[P] > nums[P - 1] and nums[P] < nums[P + 1]:
                start = P
            # Descending area
            else:
                end = P

        return start if nums[start] >= nums[end] else end
