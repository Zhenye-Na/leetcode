#
# @lc app=leetcode id=795 lang=python3
#
# [795] Number of Subarrays with Bounded Maximum
#
# https://leetcode.com/problems/number-of-subarrays-with-bounded-maximum/description/
#
# algorithms
# Medium (48.43%)
# Likes:    1143
# Dislikes: 78
# Total Accepted:    40.2K
# Total Submissions: 77.7K
# Testcase Example:  '[2,1,4,3]\n2\n3'
#
# We are given an array nums of positive integers, and two positive integers
# left and right (left <= right).
# 
# Return the number of (contiguous, non-empty) subarrays such that the value of
# the maximum array element in that subarray is at least left and at most
# right.
# 
# 
# Example:
# Input: 
# nums = [2, 1, 4, 3]
# left = 2
# right = 3
# Output: 3
# Explanation: There are three subarrays that meet the requirements: [2], [2,
# 1], [3].
# 
# 
# Note:
# 
# 
# left, right, and nums[i] will be an integer in the range [0, 10^9].
# The length of nums will be in the range of [1, 50000].
# 
# 
#

# @lc code=start
class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        i = 0
        curr = 0
        res = 0

        for j in range(len(nums)):
            if left <= nums[j] <= right:
                curr = j - i + 1
                res += j - i + 1
            elif nums[j] < left:
                res += curr
            else:
                i = j + 1
                curr = 0
        
        return res
# @lc code=end

