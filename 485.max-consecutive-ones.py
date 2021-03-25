#
# @lc app=leetcode id=485 lang=python3
#
# [485] Max Consecutive Ones
#
# https://leetcode.com/problems/max-consecutive-ones/description/
#
# algorithms
# Easy (53.13%)
# Likes:    1158
# Dislikes: 380
# Total Accepted:    371.9K
# Total Submissions: 705.5K
# Testcase Example:  '[1,0,1,1,0,1]'
#
# Given a binary array, find the maximum number of consecutive 1s in this
# array.
# 
# Example 1:
# 
# Input: [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive
# 1s.
# ⁠   The maximum number of consecutive 1s is 3.
# 
# 
# 
# Note:
# 
# The input array will only contain 0 and 1.
# The length of input array is a positive integer and will not exceed 10,000
# 
# 
#

# @lc code=start
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if not nums or len(nums) == 0:
            return 0
        
        max_count = 0
        curr_count = 0
        for num in nums:
            if num == 1:
                curr_count += 1
                max_count = max(max_count, curr_count)
            else:
                curr_count = 0
        
        return max_count 
# @lc code=end

