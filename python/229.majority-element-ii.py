#
# @lc app=leetcode id=229 lang=python3
#
# [229] Majority Element II
#
# https://leetcode.com/problems/majority-element-ii/description/
#
# algorithms
# Medium (47.08%)
# Likes:    8456
# Dislikes: 375
# Total Accepted:    496.8K
# Total Submissions: 1M
# Testcase Example:  '[3,2,3]'
#
# Given an integer array of size n, find all elements that appear more than ⌊
# n/3 ⌋ times.
# 
# 
# Example 1:
# 
# 
# Input: nums = [3,2,3]
# Output: [3]
# 
# 
# Example 2:
# 
# 
# Input: nums = [1]
# Output: [1]
# 
# 
# Example 3:
# 
# 
# Input: nums = [1,2]
# Output: [1,2]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 5 * 10^4
# -10^9 <= nums[i] <= 10^9
# 
# 
# 
# Follow up: Could you solve the problem in linear time and in O(1) space?
# 
#

# @lc code=start

# Your runtime beats 84.77 % of python3 submissions
# Your memory usage beats 84.36 % of python3 submissions (17.7 MB)
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counts = Counter(nums)
        n = len(nums)

        res = []
        for num in counts:
            if counts[num] > n // 3:
                res.append(num)

        return res
# @lc code=end

