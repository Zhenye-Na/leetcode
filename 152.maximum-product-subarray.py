#
# @lc app=leetcode id=152 lang=python3
#
# [152] Maximum Product Subarray
#
# https://leetcode.com/problems/maximum-product-subarray/description/
#
# algorithms
# Medium (32.65%)
# Likes:    6324
# Dislikes: 205
# Total Accepted:    451.4K
# Total Submissions: 1.4M
# Testcase Example:  '[2,3,-2,4]'
#
# Given an integer array nums, find a contiguous non-empty subarray within the
# array that has the largest product, and return the product.
# 
# It is guaranteed that the answer will fit in a 32-bit integer.
# 
# A subarray is a contiguous subsequence of the array.
# 
# 
# Example 1:
# 
# 
# Input: nums = [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
# 
# 
# Example 2:
# 
# 
# Input: nums = [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 2 * 10^4
# -10 <= nums[i] <= 10
# 
# 
#

# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)

        curr_max, curr_min = 1, 1
        for num in nums:
            if num == 0:
                curr_max, curr_min = 1, 1
                continue
            
            # update curr_max and curr_min
            prev_max = curr_max
            curr_max = max(num * curr_max, num * curr_min, num)
            curr_min = min(num * prev_max, num * curr_min, num)

            res = max(res, curr_max)

        return res


    def get_max_prod_subarry(self, nums):
        total_max, total_min = 1, 1
        curr_max, curr_min = 1, 1
        start_max, end_max = 0, 0
        start_single_max = 0

        n = len(nums)
        for i, num in enumerate(nums):
            choices = sorted([(curr_max * num, 1), (curr_min * num, 2), (num, 3)], key=lambda x: x[0])
            curr_max = choices[-1][0]
            curr_min = choices[0][0]

            if choices[-1][1] == 3:
                # num itself is the largest
                start_single_max = i

            if total_max < curr_max:
                total_max = curr_max
                start_max = start_single_max
                end_max = i
            if total_min > curr_min:
                total_min = curr_min

        return nums[start_max:end_max + 1]
# @lc code=end

