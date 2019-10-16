#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums or len(nums) == 0:
            return 0

        left, right = 0, 0
        while right < len(nums):
            if nums[right] == nums[left]:
                right += 1
            else:
                left += 1
                nums[left] = nums[right]
                right += 1

        return left + 1

# @lc code=end

