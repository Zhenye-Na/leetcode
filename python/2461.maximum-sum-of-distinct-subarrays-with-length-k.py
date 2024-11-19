#
# @lc app=leetcode id=2461 lang=python3
#
# [2461] Maximum Sum of Distinct Subarrays With Length K
#
# https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/description/
#
# algorithms
# Medium (34.24%)
# Likes:    1581
# Dislikes: 31
# Total Accepted:    99.3K
# Total Submissions: 261.7K
# Testcase Example:  '[1,5,4,2,9,9,9]\n3'
#
# You are given an integer array nums and an integer k. Find the maximum
# subarray sum of all the subarrays of nums that meet the following
# conditions:
#
#
# The length of the subarray is k, and
# All the elements of the subarray are distinct.
#
#
# Return the maximum subarray sum of all the subarrays that meet the
# conditions. If no subarray meets the conditions, return 0.
#
# A subarray is a contiguous non-empty sequence of elements within an array.
#
#
# Example 1:
#
#
# Input: nums = [1,5,4,2,9,9,9], k = 3
# Output: 15
# Explanation: The subarrays of nums with length 3 are:
# - [1,5,4] which meets the requirements and has a sum of 10.
# - [5,4,2] which meets the requirements and has a sum of 11.
# - [4,2,9] which meets the requirements and has a sum of 15.
# - [2,9,9] which does not meet the requirements because the element 9 is
# repeated.
# - [9,9,9] which does not meet the requirements because the element 9 is
# repeated.
# We return 15 because it is the maximum subarray sum of all the subarrays that
# meet the conditions
#
#
# Example 2:
#
#
# Input: nums = [4,4,4], k = 3
# Output: 0
# Explanation: The subarrays of nums with length 3 are:
# - [4,4,4] which does not meet the requirements because the element 4 is
# repeated.
# We return 0 because no subarrays meet the conditions.
#
#
#
# Constraints:
#
#
# 1 <= k <= nums.length <= 10^5
# 1 <= nums[i] <= 10^5
#
#
#


# @lc code=start
from typing import List
import sys


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        if not nums or len(nums) < k:
            return 0

        max_total = -sys.maxsize - 1
        i, running_sum = 0, 0
        seen = set()

        for j in range(len(nums)):
            running_sum += nums[j]
            seen.add(nums[j])

            if j - i + 1 > k:
                running_sum -= nums[i]
                if nums[i] in seen:
                    seen.remove(nums[i])
                i += 1

            if j - i + 1 == k and len(seen) == k:
                max_total = max(max_total, running_sum)

        return max_total if max_total != -sys.maxsize - 1 else 0


# @lc code=end
