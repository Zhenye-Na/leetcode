#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if nums is None or len(nums) == 0:
            return -1

        start, end = 0, len(nums) - 1
        while (start + 1 < end):
            mid = (end + start) // 2

            if (nums[start] < nums[mid]):
                if nums[start] <= target and target <= nums[mid]:
                    end = mid
                else:
                    start = mid
            else:
                if nums[end] >= target and nums[mid] <= target:
                    start = mid
                else:
                    end = mid


        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        return -1

