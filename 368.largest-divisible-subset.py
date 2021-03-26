#
# @lc app=leetcode id=368 lang=python3
#
# [368] Largest Divisible Subset
#
# https://leetcode.com/problems/largest-divisible-subset/description/
#
# algorithms
# Medium (38.22%)
# Likes:    1778
# Dislikes: 90
# Total Accepted:    109.6K
# Total Submissions: 285.6K
# Testcase Example:  '[1,2,3]'
#
# Given a set of distinct positive integers nums, return the largest subset
# answer such that every pair (answer[i], answer[j]) of elements in this subset
# satisfies:
# 
# 
# answer[i] % answer[j] == 0, or
# answer[j] % answer[i] == 0
# 
# 
# If there are multiple solutions, return any of them.
# 
#   
# Example 1:
# 
# 
# Input: nums = [1,2,3]
# Output: [1,2]
# Explanation: [1,3] is also accepted.
# 
# 
# Example 2:
# 
# 
# Input: nums = [1,2,4,8]
# Output: [1,2,4,8]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 1000
# 1 <= nums[i] <= 2 * 10^9
# All the integers in nums are unique.
# 
# 
#

# @lc code=start
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums or len(nums) == 0:
            return []

        # since we are doing a "subset" question
        # sorting does not make any differences
        nums.sort()
        n = len(nums)

        # initilization
        # f[i] represents the size of LDS ended with nums[i]
        f = [1 for _ in range(n)]
        for i in range(1, n):
            for j in range(i):
                # since we have already sorted,
                # then nums[j] % nums[i] will never equals zero
                # unless nums[i] == nums[j]
                if nums[i] % nums[j] == 0:
                    f[i] = max(f[i], f[j] + 1)

        # extract result from dp array
        max_size = max(f)
        max_idx = f.index(max_size) # since we can return one of the largest
        prev_num, prev_size = nums[max_idx], f[max_idx]
        res = [prev_num]
        for curr_idx in range(max_idx, -1, -1):
            if prev_num % nums[curr_idx] == 0 and f[curr_idx] == prev_size - 1:
                # update
                res.append(nums[curr_idx])
                prev_num = nums[curr_idx]
                prev_size = f[curr_idx]

        return res[::-1]
# @lc code=end

