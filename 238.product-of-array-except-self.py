#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#
# https://leetcode.com/problems/product-of-array-except-self/description/
#
# algorithms
# Medium (61.28%)
# Likes:    7063
# Dislikes: 543
# Total Accepted:    735.8K
# Total Submissions: 1.2M
# Testcase Example:  '[1,2,3,4]'
#
# Given an integer array nums, return an array answer such that answer[i] is
# equal to the product of all the elements of nums except nums[i].
# 
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit
# integer.
# 
# 
# Example 1:
# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:
# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]
# 
# 
# Constraints:
# 
# 
# 2 <= nums.length <= 10^5
# -30 <= nums[i] <= 30
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit
# integer.
# 
# 
# 
# Follow up:
# 
# 
# Could you solve it in O(n) time complexity and without using division?
# Could you solve it with O(1) constant space complexity? (The output array
# does not count as extra space for space complexity analysis.)
# 
# 
#

# @lc code=start
from functools import reduce

# O(n^2) with division
# worst case since `reduce()` function
class Solution_WithDivision:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums or len(nums) == 0:
            return []

        nums.insert(0, 1)
        nums.append(1)

        n = len(nums)
        res = []
        left_prod, right_prod = 1, reduce((lambda x, y: x * y), nums[1:])
        for i in range(1, n - 1):
            left_prod *= nums[i - 1]
            right_prod = right_prod // nums[i] if nums[i] != 0 else reduce((lambda x, y: x * y), nums[i + 1:])

            res.append(left_prod * right_prod)
        return res


# Time O(n)
# Space O(n)
class Solution_Forward_Backward_Pass:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        f = [1]
        b = [1]
        n = len(nums)

        for i in range(1, len(nums)):
            tmp = f[-1] * nums[i - 1]
            f.append(tmp)

        for j in range(len(nums) - 1 - 1, -1, -1):
            tmp = b[-1] * nums[j + 1]
            b.append(tmp)

        res = []
        for i in range(len(nums)):
            res.append(f[i] * b[n - i - 1])

        return res


# Time O(n)
# Space O(1)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        f = [1]
        n = len(nums)

        for i in range(1, len(nums)):
            tmp = f[-1] * nums[i - 1]
            f.append(tmp)

        prev = 1
        for j in range(len(nums) - 1, -1, -1):
            f[j] = f[j] * prev
            prev *= nums[j]

        return f
# @lc code=end

