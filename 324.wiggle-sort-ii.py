#
# @lc app=leetcode id=324 lang=python3
#
# [324] Wiggle Sort II
#
# https://leetcode.com/problems/wiggle-sort-ii/description/
#
# algorithms
# Medium (30.59%)
# Likes:    1341
# Dislikes: 654
# Total Accepted:    96.8K
# Total Submissions: 314.6K
# Testcase Example:  '[1,5,1,1,6,4]'
#
# Given an integer array nums, reorder it such that nums[0] < nums[1] > nums[2]
# < nums[3]....
# 
# You may assume the input array always has a valid answer.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,5,1,1,6,4]
# Output: [1,6,1,5,1,4]
# Explanation: [1,4,1,5,1,6] is also accepted.
# 
# 
# Example 2:
# 
# 
# Input: nums = [1,3,2,2,3,1]
# Output: [2,3,1,3,1,2]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 5 * 10^4
# 0 <= nums[i] <= 5000
# It is guaranteed that there will be an answer for the given input nums.
# 
# 
# 
# Follow Up: Can you do it in O(n) time and/or in-place with O(1) extra space?
#

# @lc code=start
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        res = []
        n = len(nums)
        flag = 0
        smaller = (n - 1) // 2
        larger = n - 1

        for _ in range(n):
            if flag == 0:
                res.append(nums[smaller])
                smaller -= 1
            else:
                res.append(nums[larger])
                larger -= 1

            flag = 1 - flag

        for i in range(n):
            nums[i] = res[i]
# @lc code=end

