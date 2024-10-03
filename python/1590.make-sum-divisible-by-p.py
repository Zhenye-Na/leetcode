#
# @lc app=leetcode id=1590 lang=python3
#
# [1590] Make Sum Divisible by P
#
# https://leetcode.com/problems/make-sum-divisible-by-p/description/
#
# algorithms
# Medium (28.32%)
# Likes:    1566
# Dislikes: 70
# Total Accepted:    32.5K
# Total Submissions: 109.7K
# Testcase Example:  '[3,1,4,2]\n6'
#
# Given an array of positive integers nums, remove the smallest subarray
# (possibly empty) such that the sum of the remaining elements is divisible by
# p. It is not allowed to remove the whole array.
#
# Return the length of the smallest subarray that you need to remove, or -1 if
# it's impossible.
#
# A subarray is defined as a contiguous block of elements in the array.
#
#
# Example 1:
#
#
# Input: nums = [3,1,4,2], p = 6
# Output: 1
# Explanation: The sum of the elements in nums is 10, which is not divisible by
# 6. We can remove the subarray [4], and the sum of the remaining elements is
# 6, which is divisible by 6.
#
#
# Example 2:
#
#
# Input: nums = [6,3,5,2], p = 9
# Output: 2
# Explanation: We cannot remove a single element to get a sum divisible by 9.
# The best way is to remove the subarray [5,2], leaving us with [6,3] with sum
# 9.
#
#
# Example 3:
#
#
# Input: nums = [1,2,3], p = 3
# Output: 0
# Explanation: Here the sum is 6. which is already divisible by 3. Thus we do
# not need to remove anything.
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^9
# 1 <= p <= 10^9
#
#
#


# @lc code=start
from typing import List


class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total_sum = sum(nums)
        remainder = total_sum % p
        if remainder == 0:
            return 0

        prefix_map = {0: -1}
        current_sum = 0
        min_len = len(nums)

        for i, num in enumerate(nums):
            current_sum += num
            mod_value = current_sum % p

            # We are looking for a previous prefix sum such that:
            # (current_sum - prefix_sum) % p == remainder
            target = (mod_value - remainder) % p

            if target in prefix_map:
                min_len = min(min_len, i - prefix_map[target])

            prefix_map[mod_value] = i

        return min_len if min_len != len(nums) else -1


# @lc code=end
