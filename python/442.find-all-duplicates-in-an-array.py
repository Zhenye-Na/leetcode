#
# @lc app=leetcode id=442 lang=python3
#
# [442] Find All Duplicates in an Array
#
# https://leetcode.com/problems/find-all-duplicates-in-an-array/description/
#
# algorithms
# Medium (73.61%)
# Likes:    9676
# Dislikes: 352
# Total Accepted:    628.6K
# Total Submissions: 849.3K
# Testcase Example:  '[4,3,2,7,8,2,3,1]'
#
# Given an integer array nums of length n where all the integers of nums are in
# the range [1, n] and each integer appears once or twice, return an array of
# all the integers that appears twice.
# 
# You must write an algorithm that runs in O(n) time and uses only constant
# extra space.
# 
# 
# Example 1:
# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [2,3]
# Example 2:
# Input: nums = [1,1,2]
# Output: [1]
# Example 3:
# Input: nums = [1]
# Output: []
# 
# 
# Constraints:
# 
# 
# n == nums.length
# 1 <= n <= 10^5
# 1 <= nums[i] <= n
# Each element in nums appears once or twice.
# 
# 
#

# @lc code=start
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        nums = ["#"] + nums
        for i in range(1, len(nums)):
            while i != nums[i]:
                if nums[i] == nums[nums[i]]:
                    break

                tmp = nums[i]
                nums[i] = nums[nums[i]]
                nums[tmp] = tmp

        res = []
        for i in range(1, len(nums)):
            if i != nums[i]:
                res.append(nums[i])

        return res
# @lc code=end

# nums = [1, 2, 3, 4, 3, 2, 7, 8]
