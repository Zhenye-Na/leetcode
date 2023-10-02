#
# @lc app=leetcode id=2104 lang=python3
#
# [2104] Sum of Subarray Ranges
#
# https://leetcode.com/problems/sum-of-subarray-ranges/description/
#
# algorithms
# Medium (60.93%)
# Likes:    2071
# Dislikes: 102
# Total Accepted:    78.7K
# Total Submissions: 129.2K
# Testcase Example:  '[1,2,3]'
#
# You are given an integer array nums. The range of a subarray of nums is the
# difference between the largest and smallest element in the subarray.
# 
# Return the sum of all subarray ranges of nums.
# 
# A subarray is a contiguous non-empty sequence of elements within an array.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,2,3]
# Output: 4
# Explanation: The 6 subarrays of nums are the following:
# [1], range = largest - smallest = 1 - 1 = 0 
# [2], range = 2 - 2 = 0
# [3], range = 3 - 3 = 0
# [1,2], range = 2 - 1 = 1
# [2,3], range = 3 - 2 = 1
# [1,2,3], range = 3 - 1 = 2
# So the sum of all ranges is 0 + 0 + 0 + 1 + 1 + 2 = 4.
# 
# Example 2:
# 
# 
# Input: nums = [1,3,3]
# Output: 4
# Explanation: The 6 subarrays of nums are the following:
# [1], range = largest - smallest = 1 - 1 = 0
# [3], range = 3 - 3 = 0
# [3], range = 3 - 3 = 0
# [1,3], range = 3 - 1 = 2
# [3,3], range = 3 - 3 = 0
# [1,3,3], range = 3 - 1 = 2
# So the sum of all ranges is 0 + 0 + 0 + 2 + 0 + 2 = 4.
# 
# 
# Example 3:
# 
# 
# Input: nums = [4,-2,-3,4,1]
# Output: 59
# Explanation: The sum of all subarray ranges of nums is 59.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 1000
# -10^9 <= nums[i] <= 10^9
# 
# 
# 
# Follow-up: Could you find a solution with O(n) time complexity?
# 
#

# @lc code=start
class Solution_MonotonicStack:
    def subArrayRanges(self, nums: List[int]) -> int:
        res = 0

        stack = []
        min_nums = [-float('inf')] + nums + [-float('inf')]
        for idx, num in enumerate(min_nums):
            if len(stack) == 0:
                stack.append(idx)
            else:
                while stack and min_nums[stack[-1]] > num: # monotonic increasing stack
                    pos = stack.pop()
                    left = stack[-1] if stack else -1
                    res -= min_nums[pos] * (idx - pos) * (pos - left)
                stack.append(idx)


        stack = []
        max_nums = [float('inf')] + nums + [float('inf')]
        for idx, num in enumerate(max_nums):
            if len(stack) == 0:
                stack.append(idx)
            else:
                while stack and max_nums[stack[-1]] < num: # monotonic decreasing stack
                    pos = stack.pop()
                    left = stack[-1] if stack else -1
                    res += max_nums[pos] * (idx - pos) * (pos - left)
                stack.append(idx)

        return res

class Solution_On2:
    def subArrayRanges(self, nums: List[int]) -> int:
        
        n = len(nums)
        total = 0
        for left in range(n):

            min_val, max_val = math.inf, -math.inf
            for right in range(left, n):
                
                min_val = min(min_val, nums[right])
                max_val = max(max_val, nums[right])

                total += (max_val - min_val)

        return total
# @lc code=end

