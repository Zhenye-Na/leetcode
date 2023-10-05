#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#
# https://leetcode.com/problems/majority-element/description/
#
# algorithms
# Easy (60.83%)
# Likes:    8372
# Dislikes: 313
# Total Accepted:    1.1M
# Total Submissions: 1.8M
# Testcase Example:  '[3,2,3]'
#
# Given an array nums of size n, return the majority element.
# 
# The majority element is the element that appears more than ⌊n / 2⌋ times. You
# may assume that the majority element always exists in the array.
# 
# 
# Example 1:
# Input: nums = [3,2,3]
# Output: 3
# Example 2:
# Input: nums = [2,2,1,1,1,2,2]
# Output: 2
# 
# 
# Constraints:
# 
# 
# n == nums.length
# 1 <= n <= 5 * 10^4
# -2^31 <= nums[i] <= 2^31 - 1
# 
# 
# 
# Follow-up: Could you solve the problem in linear time and in O(1) space?
#

# @lc code=start
class Solution_Misra_Gries:
    def majorityElement(self, nums: List[int]) -> int:
        key, count = None, 0
        for num in nums:
            if not key:
                key, count = num, 1
            else:
                if key == num:
                    count += 1
                else:
                    count -= 1

            if count == 0:
                key = None

        return key


class Solution_HashMap:
    def majorityElement(self, nums: List[int]) -> int:
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)
# @lc code=end

