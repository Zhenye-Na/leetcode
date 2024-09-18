#
# @lc app=leetcode id=179 lang=python3
#
# [179] Largest Number
#
# https://leetcode.com/problems/largest-number/description/
#
# algorithms
# Medium (35.25%)
# Likes:    8295
# Dislikes: 695
# Total Accepted:    534.7K
# Total Submissions: 1.4M
# Testcase Example:  '[10,2]'
#
# Given a list of non-negative integers nums, arrange them such that they form
# the largest number and return it.
#
# Since the result may be very large, so you need to return a string instead of
# an integer.
#
#
# Example 1:
#
#
# Input: nums = [10,2]
# Output: "210"
#
#
# Example 2:
#
#
# Input: nums = [3,30,34,5,9]
# Output: "9534330"
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 10^9
#
#
#

# @lc code=start
from functools import cmp_to_key
from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        def compare(a, b):
            if str(a) + str(b) > str(b) + str(a):
                return -1
            else:
                return 1

        sorted_nums = sorted(nums, key=cmp_to_key(compare))
        res = "".join([str(num) for num in sorted_nums])

        if res.startswith("0"):
            return "0" + res.lstrip("0")
        return res


# @lc code=end
