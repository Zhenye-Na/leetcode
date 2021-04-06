#
# @lc app=leetcode id=228 lang=python3
#
# [228] Summary Ranges
#
# https://leetcode.com/problems/summary-ranges/description/
#
# algorithms
# Easy (42.18%)
# Likes:    969
# Dislikes: 698
# Total Accepted:    210.2K
# Total Submissions: 492.5K
# Testcase Example:  '[0,1,2,4,5,7]'
#
# You are given a sorted unique integer array nums.
# 
# Return the smallest sorted list of ranges that cover all the numbers in the
# array exactly. That is, each element of nums is covered by exactly one of the
# ranges, and there is no integer x such that x is in one of the ranges but not
# in nums.
# 
# Each range [a,b] in the list should be output as:
# 
# 
# "a->b" if a != b
# "a" if a == b
# 
# 
# 
# Example 1:
# 
# 
# Input: nums = [0,1,2,4,5,7]
# Output: ["0->2","4->5","7"]
# Explanation: The ranges are:
# [0,2] --> "0->2"
# [4,5] --> "4->5"
# [7,7] --> "7"
# 
# 
# Example 2:
# 
# 
# Input: nums = [0,2,3,4,6,8,9]
# Output: ["0","2->4","6","8->9"]
# Explanation: The ranges are:
# [0,0] --> "0"
# [2,4] --> "2->4"
# [6,6] --> "6"
# [8,9] --> "8->9"
# 
# 
# Example 3:
# 
# 
# Input: nums = []
# Output: []
# 
# 
# Example 4:
# 
# 
# Input: nums = [-1]
# Output: ["-1"]
# 
# 
# Example 5:
# 
# 
# Input: nums = [0]
# Output: ["0"]
# 
# 
# 
# Constraints:
# 
# 
# 0 <= nums.length <= 20
# -2^31 <= nums[i] <= 2^31 - 1
# All the values of nums are unique.
# nums is sorted in ascending order.
# 
# 
#

# @lc code=start
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums or len(nums) == 0:
            return []
        
        start = 0
        res = []
        for i in range(len(nums)):
            if i + 1 >= len(nums) or nums[i] + 1 != nums[i + 1]:
                first = nums[start]
                second = nums[i]
                res.append(str(first) + "->" + str(second) if first != second else str(first))
                start = i + 1

        return res
# @lc code=end

