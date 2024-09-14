#
# @lc app=leetcode id=2419 lang=python3
#
# [2419] Longest Subarray With Maximum Bitwise AND
#
# https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and/description/
#
# algorithms
# Medium (48.70%)
# Likes:    643
# Dislikes: 58
# Total Accepted:    59.1K
# Total Submissions: 104.4K
# Testcase Example:  '[1,2,3,3,2,2]'
#
# You are given an integer array nums of size n.
#
# Consider a non-empty subarray from nums that has the maximum possible bitwise
# AND.
#
#
# In other words, let k be the maximum value of the bitwise AND of any subarray
# of nums. Then, only subarrays with a bitwise AND equal to k should be
# considered.
#
#
# Return the length of the longest such subarray.
#
# The bitwise AND of an array is the bitwise AND of all the numbers in it.
#
# A subarray is a contiguous sequence of elements within an array.
#
#
# Example 1:
#
#
# Input: nums = [1,2,3,3,2,2]
# Output: 2
# Explanation:
# The maximum possible bitwise AND of a subarray is 3.
# The longest subarray with that value is [3,3], so we return 2.
#
#
# Example 2:
#
#
# Input: nums = [1,2,3,4]
# Output: 1
# Explanation:
# The maximum possible bitwise AND of a subarray is 4.
# The longest subarray with that value is [4], so we return 1.
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^6
#
#
#


# @lc code=start
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_num = max(nums)
        max_len = 0
        current_len = 0

        for num in nums:
            if num == max_num:
                current_len += 1
                max_len = max(max_len, current_len)
            else:
                current_len = 0

        return max_len


# @lc code=end
