#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#
# https://leetcode.com/problems/3sum/description/
#
# algorithms
# Medium (27.84%)
# Likes:    9956
# Dislikes: 1022
# Total Accepted:    1.2M
# Total Submissions: 4.4M
# Testcase Example:  '[-1,0,1,2,-1,-4]'
#
# Given an integer array nums, return all the triplets [nums[i], nums[j],
# nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] +
# nums[k] == 0.
# 
# Notice that the solution set must not contain duplicate triplets.
# 
# 
# Example 1:
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Example 2:
# Input: nums = []
# Output: []
# Example 3:
# Input: nums = [0]
# Output: []
# 
# 
# Constraints:
# 
# 
# 0 <= nums.length <= 3000
# -10^5 <= nums[i] <= 10^5
# 
# 
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(
            [(num, idx) for idx, num in enumerate(nums)],
            key=lambda x: (x[0], x[1])
        )

        res = set([])
        for k in range(len(sorted_nums) - 1, -1, -1):
            combination = self.twoSum(sorted_nums[0:k] + sorted_nums[k + 1:], - sorted_nums[k][0])
            if len(combination) == 0:
                continue

            for i, j in combination:
                choice = tuple(sorted([nums[i], nums[j], sorted_nums[k][0]]))
                if choice not in res and i != j != k:
                    res.add(choice)

        return list([list(comb) for comb in res])


    def twoSum(self, nums, target):
        left, right = 0, len(nums) - 1
        res = []

        while left <= right:
            if nums[left][0] + nums[right][0] == target:
                res.append((nums[left][1], nums[right][1]))
                left += 1
                while left < right and nums[left - 1][0] == nums[left][0]:
                    left += 1
                
                right -= 1
                while left < right and nums[right + 1][0] == nums[right][0]:
                    right -= 1

            elif nums[left][0] + nums[right][0] > target:
                right -= 1
            else:
                left += 1

        return res
# @lc code=end

