#
# @lc app=leetcode id=31 lang=python3
#
# [31] Next Permutation
#
# https://leetcode.com/problems/next-permutation/description/
#
# algorithms
# Medium (33.29%)
# Likes:    5095
# Dislikes: 1749
# Total Accepted:    486.4K
# Total Submissions: 1.4M
# Testcase Example:  '[1,2,3]'
#
# Implement next permutation, which rearranges numbers into the
# lexicographically next greater permutation of numbers.
# 
# If such an arrangement is not possible, it must rearrange it as the lowest
# possible order (i.e., sorted in ascending order).
# 
# The replacement must be in place and use only constant extra memory.
# 
# 
# Example 1:
# Input: nums = [1,2,3]
# Output: [1,3,2]
# Example 2:
# Input: nums = [3,2,1]
# Output: [1,2,3]
# Example 3:
# Input: nums = [1,1,5]
# Output: [1,5,1]
# Example 4:
# Input: nums = [1]
# Output: [1]
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 100
# 
# 
#

# @lc code=start
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums or len(nums) == 0:
            return

        i = len(nums) - 1
        while i > 0 and nums[i - 1] >= nums[i]:
            i -= 1
        
        # after the while loop, i will point to the largest element in
        # in the decreasing sequence
        if i <= 0:
            nums.sort()
            return

        pivot = nums[i - 1]
        j = len(nums) - 1
        while j > i and nums[j] <= pivot:
            j -= 1

        nums[i - 1], nums[j] = nums[j], nums[i - 1]
        left, right = i, len(nums) - 1
        while left <= right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
# @lc code=end

