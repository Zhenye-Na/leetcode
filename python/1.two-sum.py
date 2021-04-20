#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) < 2:
            return [-1, -1]

        nums_idx = [idx for idx, num in sorted(enumerate(nums), key=lambda x: x[1])]
        nums.sort()

        left, right = 0, len(nums) - 1
        while left + 1 <= right:
            if nums[left] + nums[right] == target:
                return sorted([nums_idx[left], nums_idx[right]])
            elif nums[left] + nums[right] > target:
                right -= 1
            else:
                left += 1

        return [-1, -1]

# @lc code=end

