#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#
# https://leetcode.com/problems/maximum-subarray/description/
#
# algorithms
# Easy (47.59%)
# Likes:    11086
# Dislikes: 529
# Total Accepted:    1.3M
# Total Submissions: 2.8M
# Testcase Example:  '[-2,1,-3,4,-1,2,1,-5,4]'
#
# Given an integer array nums, find the contiguous subarray (containing at
# least one number) which has the largest sum and return its sum.
# 
# 
# Example 1:
# 
# 
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# 
# 
# Example 2:
# 
# 
# Input: nums = [1]
# Output: 1
# 
# 
# Example 3:
# 
# 
# Input: nums = [5,4,-1,7,8]
# Output: 23
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 3 * 10^4
# -10^5 <= nums[i] <= 10^5
# 
# 
# 
# Follow up: If you have figured out the O(n) solution, try coding another
# solution using the divide and conquer approach, which is more subtle.
#

# @lc code=start
import sys
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums or len(nums) == 0:
            return 0

        prefix_sum = 0
        running_max, running_min = -sys.maxsize, 0

        for num in nums:
            prefix_sum += num
            running_max = max(running_max, prefix_sum - running_min)
            running_min = min(prefix_sum, running_min)

        return running_max
# @lc code=end

