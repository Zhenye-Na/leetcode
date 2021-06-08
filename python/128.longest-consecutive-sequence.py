#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#
# https://leetcode.com/problems/longest-consecutive-sequence/description/
#
# algorithms
# Hard (46.11%)
# Likes:    5652
# Dislikes: 270
# Total Accepted:    439.7K
# Total Submissions: 931.5K
# Testcase Example:  '[100,4,200,1,3,2]'
#
# Given an unsorted array of integers nums, return the length of the longest
# consecutive elements sequence.
# 
# You must write an algorithm that runs in O(n) time.
# 
# 
# Example 1:
# 
# 
# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4].
# Therefore its length is 4.
# 
# 
# Example 2:
# 
# 
# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9
# 
# 
# 
# Constraints:
# 
# 
# 0 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9
# 
# 
#

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest, s = 0, set(nums)
        for num in nums:
            cur_longest, j = 1, 1
            while num - j in s: 
                s.remove(num - j)
                cur_longest, j = cur_longest + 1, j + 1
            j = 1
            while num + j in s: 
                s.remove(num + j)
                cur_longest, j = cur_longest + 1, j + 1
            longest = max(longest, cur_longest)
        return longest
# @lc code=end

