#
# @lc app=leetcode id=376 lang=python3
#
# [376] Wiggle Subsequence
#
# https://leetcode.com/problems/wiggle-subsequence/description/
#
# algorithms
# Medium (40.15%)
# Likes:    1585
# Dislikes: 76
# Total Accepted:    96.3K
# Total Submissions: 230.5K
# Testcase Example:  '[1,7,4,9,2,5]'
#
# Given an integer array nums, return the length of the longest wiggle
# sequence.
# 
# A wiggle sequence is a sequence where the differences between successive
# numbers strictly alternate between positive and negative. The first
# difference (if one exists) may be either positive or negative. A sequence
# with fewer than two elements is trivially a wiggle sequence.
# 
# 
# For example, [1, 7, 4, 9, 2, 5] is a wiggle sequence because the differences
# (6, -3, 5, -7, 3) are alternately positive and negative.
# In contrast, [1, 4, 7, 2, 5] and [1, 7, 4, 5, 5] are not wiggle sequences,
# the first because its first two differences are positive and the second
# because its last difference is zero.
# 
# 
# A subsequence is obtained by deleting some elements (eventually, also zero)
# from the original sequence, leaving the remaining elements in their original
# order.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,7,4,9,2,5]
# Output: 6
# Explanation: The entire sequence is a wiggle sequence.
# 
# 
# Example 2:
# 
# 
# Input: nums = [1,17,5,10,13,15,10,5,16,8]
# Output: 7
# Explanation: There are several subsequences that achieve this length. One is
# [1,17,10,13,10,16,8].
# 
# 
# Example 3:
# 
# 
# Input: nums = [1,2,3,4,5,6,7,8,9]
# Output: 2
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 1000
# 0 <= nums[i] <= 1000
# 
# 
# 
# Follow up: Could you solve this in O(n) time?
# 
#

# @lc code=start
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        # initialization
        length = [[1 for _ in range(2)] for _ in range(len(nums))]

        # state
        #   0: prev > curr
        #   1: prev < curr
        max_len = 1
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] > nums[i]:
                    length[i][0] = max(length[i][0], length[j][1] + 1)
                elif nums[j] < nums[i]:
                    length[i][1] = max(length[i][1], length[j][0] + 1)

            max_len = max(max_len, length[i][0], length[i][1])
        return max_len
# @lc code=end

