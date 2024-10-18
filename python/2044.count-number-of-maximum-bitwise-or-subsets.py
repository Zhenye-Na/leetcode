#
# @lc app=leetcode id=2044 lang=python3
#
# [2044] Count Number of Maximum Bitwise-OR Subsets
#
# https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets/description/
#
# algorithms
# Medium (78.34%)
# Likes:    756
# Dislikes: 36
# Total Accepted:    51K
# Total Submissions: 61.5K
# Testcase Example:  '[3,1]'
#
# Given an integer array nums, find the maximum possible bitwise OR of a subset
# of nums and return the number of different non-empty subsets with the maximum
# bitwise OR.
#
# An array a is a subset of an array b if a can be obtained from b by deleting
# some (possibly zero) elements of b. Two subsets are considered different if
# the indices of the elements chosen are different.
#
# The bitwise OR of an array a is equal to a[0] OR a[1] OR ... OR a[a.length -
# 1] (0-indexed).
#
#
# Example 1:
#
#
# Input: nums = [3,1]
# Output: 2
# Explanation: The maximum possible bitwise OR of a subset is 3. There are 2
# subsets with a bitwise OR of 3:
# - [3]
# - [3,1]
#
#
# Example 2:
#
#
# Input: nums = [2,2,2]
# Output: 7
# Explanation: All non-empty subsets of [2,2,2] have a bitwise OR of 2. There
# are 2^3 - 1 = 7 total subsets.
#
#
# Example 3:
#
#
# Input: nums = [3,2,1,5]
# Output: 6
# Explanation: The maximum possible bitwise OR of a subset is 7. There are 6
# subsets with a bitwise OR of 7:
# - [3,5]
# - [3,1,5]
# - [3,2,5]
# - [3,2,1,5]
# - [2,5]
# - [2,1,5]
#
#
# Constraints:
#
#
# 1 <= nums.length <= 16
# 1 <= nums[i] <= 10^5
#
#
#

# @lc code=start
from typing import List


class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_or = 0
        for num in nums:
            max_or |= num

        return self.count_subsets(nums, 0, 0, max_or)

    def count_subsets(
        self, nums: List[int], index: int, current_or: int, max_or: int
    ) -> int:
        if index == len(nums):
            return 1 if current_or == max_or else 0

        include = self.count_subsets(nums, index + 1, current_or | nums[index], max_or)
        exclude = self.count_subsets(nums, index + 1, current_or, max_or)

        return include + exclude


# @lc code=end
