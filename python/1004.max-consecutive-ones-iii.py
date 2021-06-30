#
# @lc app=leetcode id=1004 lang=python3
#
# [1004] Max Consecutive Ones III
#
# https://leetcode.com/problems/max-consecutive-ones-iii/description/
#
# algorithms
# Medium (61.32%)
# Likes:    2593
# Dislikes: 40
# Total Accepted:    123.4K
# Total Submissions: 202.1K
# Testcase Example:  '[1,1,1,0,0,0,1,1,1,1,0]\n2'
#
# Given a binary array nums and an integer k, return the maximum number of
# consecutive 1's in the array if you can flip at most k 0's.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
# Output: 6
# Explanation: [1,1,1,0,0,1,1,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
# 
# Example 2:
# 
# 
# Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
# Output: 10
# Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is
# underlined.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^5
# nums[i] is either 0 or 1.
# 0 <= k <= nums.length
# 
# 
#

# @lc code=start
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        if not nums or len(nums) == 0:
            return 0

        left, right = 0, 0
        if nums[right] == 0:
            k -= 1

        n = len(nums)
        max_length = 0

        for left in range(n):

            while right + 1 < n and ( (k > 0) or nums[right + 1] == 1 ):
                if nums[right + 1] == 0:
                    k -= 1
                right += 1

            if k >= 0:
                max_length = max(max_length, right - left + 1)

            if nums[left] == 0:
                k += 1

        return max_length
# @lc code=end

