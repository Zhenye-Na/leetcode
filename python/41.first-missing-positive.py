#
# @lc app=leetcode id=41 lang=python3
#
# [41] First Missing Positive
#
# https://leetcode.com/problems/first-missing-positive/description/
#
# algorithms
# Hard (29.96%)
# Likes:    2180
# Dislikes: 654
# Total Accepted:    250.8K
# Total Submissions: 837.3K
# Testcase Example:  '[1,2,0]'
#
# Given an unsorted integer array, find the smallest missing positive integer.
# 
# Example 1:
# 
# 
# Input: [1,2,0]
# Output: 3
# 
# 
# Example 2:
# 
# 
# Input: [3,4,-1,1]
# Output: 2
# 
# 
# Example 3:
# 
# 
# Input: [7,8,9,11,12]
# Output: 1
# 
# 
# Note:
# 
# Your algorithm should run in O(n) time and uses constant extra space.
# 
#

# @lc code=start

# resources
#   https://www.youtube.com/watch?v=9SnkdYXNIzM&ab_channel=MichaelMuinos

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if not nums or len(nums) == 0:
            return 1

        # Step 1
        l = len(nums)
        containsOne = False
        for i in range(l):
            if nums[i] == 1:
                containsOne = True
            
            elif nums[i] <= 0 or nums[i] > l:
                nums[i] = 1

        # if we do not see an One, we directly return 1
        if not containsOne:
            return 1

        # Step 2
        for i in range(l):
            if nums[abs(nums[i]) - 1] > 0:
                nums[abs(nums[i]) - 1] *= -1

        # Step 3
        for i in range(l):
            if nums[i] > 0:
                return i + 1
        return l + 1
# @lc code=end

