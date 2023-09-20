#
# @lc app=leetcode id=1658 lang=python3
#
# [1658] Minimum Operations to Reduce X to Zero
#
# https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/description/
#
# algorithms
# Medium (33.31%)
# Likes:    4401
# Dislikes: 88
# Total Accepted:    126.6K
# Total Submissions: 331.1K
# Testcase Example:  '[1,1,4,2,3]\n5'
#
# You are given an integer array nums and an integer x. In one operation, you
# can either remove the leftmost or the rightmost element from the array nums
# and subtract its value from x. Note that this modifies the array for future
# operations.
# 
# Return the minimum number of operations to reduce x to exactly 0 if it is
# possible, otherwise, return -1.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,1,4,2,3], x = 5
# Output: 2
# Explanation: The optimal solution is to remove the last two elements to
# reduce x to zero.
# 
# 
# Example 2:
# 
# 
# Input: nums = [5,6,7,8,9], x = 4
# Output: -1
# 
# 
# Example 3:
# 
# 
# Input: nums = [3,2,20,1,1,3], x = 10
# Output: 5
# Explanation: The optimal solution is to remove the last three elements and
# the first two elements (5 operations in total) to reduce x to zero.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^4
# 1 <= x <= 10^9
# 
# 
#

# @lc code=start
# O(n^2) Prefix Sum (TLE)
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:

        prefix_sum = [0]
        for num in nums:
            prefix_sum.append(prefix_sum[-1] + num)

        total = sum(nums)
        ops = len(nums) + 1
        for i in range(len(nums) + 1):
            for j in range(i, len(nums) + 1):

                curr = prefix_sum[j] - prefix_sum[i]
                if total - curr == x:                    

                    step = len(nums) - (j - i)
                    if step < ops:
                        ops = step

        return ops if ops != len(nums) + 1 else -1

# O(n) Sliding Window
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        
        target = sum(nums) - x
        if target < 0:
            return -1

        left = 0
        ops = len(nums) + 1
        running_sum = 0
        for right in range(len(nums)):

            running_sum += nums[right]
            while running_sum > target and left <= right:
                running_sum -= nums[left]
                left += 1

            if running_sum == target:
                ops = min(ops, len(nums) - (right - left + 1))

        return ops if ops != len(nums) + 1 else -1
# @lc code=end

