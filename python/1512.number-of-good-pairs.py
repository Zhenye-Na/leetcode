#
# @lc app=leetcode id=1512 lang=python3
#
# [1512] Number of Good Pairs
#
# https://leetcode.com/problems/number-of-good-pairs/description/
#
# algorithms
# Easy (88.25%)
# Likes:    4325
# Dislikes: 206
# Total Accepted:    505.2K
# Total Submissions: 572.2K
# Testcase Example:  '[1,2,3,1,1,3]'
#
# Given an array of integers nums, return the number of good pairs.
# 
# A pair (i, j) is called good if nums[i] == nums[j] and i < j.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,2,3,1,1,3]
# Output: 4
# Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
# 
# 
# Example 2:
# 
# 
# Input: nums = [1,1,1,1]
# Output: 6
# Explanation: Each pair in the array are good.
# 
# 
# Example 3:
# 
# 
# Input: nums = [1,2,3]
# Output: 0
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 100
# 1 <= nums[i] <= 100
# 
# 
#

# @lc code=start
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        numbers = defaultdict(list)
        for i, num in enumerate(nums):
            numbers[num].append(i)

        pairs = 0
        for num in numbers:
            if len(numbers[num]) >= 2:
                n = len(numbers[num])
                pairs += (n - 1) * n // 2

        return pairs
# @lc code=end

