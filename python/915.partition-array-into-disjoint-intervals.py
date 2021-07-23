#
# @lc app=leetcode id=915 lang=python3
#
# [915] Partition Array into Disjoint Intervals
#
# https://leetcode.com/problems/partition-array-into-disjoint-intervals/description/
#
# algorithms
# Medium (47.14%)
# Likes:    860
# Dislikes: 48
# Total Accepted:    51.1K
# Total Submissions: 106.6K
# Testcase Example:  '[5,0,3,8,6]'
#
# Given an array nums, partition it into two (contiguous) subarrays left and
# right so that:
# 
# 
# Every element in left is less than or equal to every element in right.
# left and right are non-empty.
# left has the smallest possible size.
# 
# 
# Return the length of left after such a partitioning.  It is guaranteed that
# such a partitioning exists.
# 
# 
# 
# Example 1:
# 
# 
# Input: nums = [5,0,3,8,6]
# Output: 3
# Explanation: left = [5,0,3], right = [8,6]
# 
# 
# 
# Example 2:
# 
# 
# Input: nums = [1,1,1,0,6,12]
# Output: 4
# Explanation: left = [1,1,1,0], right = [6,12]
# 
# 
# 
# 
# 
# Note:
# 
# 
# 2 <= nums.length <= 30000
# 0 <= nums[i] <= 10^6
# It is guaranteed there is at least one way to partition nums as
# described.
# 
# 
# 
# 
# 
# 
#

# @lc code=start
class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        leftMax = globalMax = nums[0]
        partition = 0

        for i in range(1, len(nums)):
            globalMax = max(globalMax, nums[i])
            if nums[i] < leftMax:  # If nums[i] < leftMax then nums[i] belong to left subarray, re-partition leftSubArr = nums[0..i]
                partition = i
                leftMax = globalMax

        return partition + 1
# @lc code=end

