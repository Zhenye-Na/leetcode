#
# @lc app=leetcode id=2366 lang=python3
#
# [2366] Minimum Replacements to Sort the Array
#
# https://leetcode.com/problems/minimum-replacements-to-sort-the-array/description/
#
# algorithms
# Hard (54.11%)
# Likes:    1878
# Dislikes: 62
# Total Accepted:    59.4K
# Total Submissions: 109.7K
# Testcase Example:  '[3,9,3]'
#
# You are given a 0-indexed integer array nums. In one operation you can
# replace any element of the array with any two elements that sum to it.
# 
# 
# For example, consider nums = [5,6,7]. In one operation, we can replace
# nums[1] with 2 and 4 and convert nums to [5,2,4,7].
# 
# 
# Return the minimum number of operations to make an array that is sorted in
# non-decreasing order.
# 
# 
# Example 1:
# 
# 
# Input: nums = [3,9,3]
# Output: 2
# Explanation: Here are the steps to sort the array in non-decreasing order:
# - From [3,9,3], replace the 9 with 3 and 6 so the array becomes [3,3,6,3]
# - From [3,3,6,3], replace the 6 with 3 and 3 so the array becomes [3,3,3,3,3]
# There are 2 steps to sort the array in non-decreasing order. Therefore, we
# return 2.
# 
# 
# 
# Example 2:
# 
# 
# Input: nums = [1,2,3,4,5]
# Output: 0
# Explanation: The array is already in non-decreasing order. Therefore, we
# return 0. 
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^9
# 
# 
#

# @lc code=start
class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:

        if not nums or len(nums) == 0:
            return 0

        ops = 0
        last_num = nums[-1]
        l = len(nums) - 2
        while l >= 0:
            if nums[l] <= last_num:
                last_num = nums[l]
            else:
                # nums[l] > nums[r]
                k = nums[l] // last_num
                d = nums[l] % last_num

                # we dont need any further adjustment
                if d == 0:
                    ops += k - 1
                    l -= 1
                    continue

                # calculate value
                p = (last_num - d) // ( k + 1)
                d2 = d + p * k
                last_num -= p

                # check if we need to do adjustment
                if d2 < last_num:
                    d2 = (d2 + (k - 1) * last_num) // k

                last_num = d2
                ops += k

            l -= 1

        return ops
# @lc code=end

