#
# @lc app=leetcode id=1799 lang=python3
#
# [1799] Maximize Score After N Operations
#
# https://leetcode.com/problems/maximize-score-after-n-operations/description/
#
# algorithms
# Hard (45.83%)
# Likes:    1536
# Dislikes: 107
# Total Accepted:    55.3K
# Total Submissions: 94.8K
# Testcase Example:  '[1,2]'
#
# You are given nums, an array of positive integers of size 2 * n. You must
# perform n operations on this array.
# 
# In the i^th operation (1-indexed), you will:
# 
# 
# Choose two elements, x and y.
# Receive a score of i * gcd(x, y).
# Remove x and y from nums.
# 
# 
# Return the maximum score you can receive after performing n operations.
# 
# The function gcd(x, y) is the greatest common divisor of x and y.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,2]
# Output: 1
# Explanation: The optimal choice of operations is:
# (1 * gcd(1, 2)) = 1
# 
# 
# Example 2:
# 
# 
# Input: nums = [3,4,6,8]
# Output: 11
# Explanation: The optimal choice of operations is:
# (1 * gcd(3, 6)) + (2 * gcd(4, 8)) = 3 + 8 = 11
# 
# 
# Example 3:
# 
# 
# Input: nums = [1,2,3,4,5,6]
# Output: 14
# Explanation: The optimal choice of operations is:
# (1 * gcd(1, 5)) + (2 * gcd(2, 4)) + (3 * gcd(3, 6)) = 1 + 4 + 9 = 14
# 
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 7
# nums.length == 2 * n
# 1 <= nums[i] <= 10^6
# 
# 
#

# @lc code=start
import math

class Solution:
    def maxScore(self, nums: List[int]) -> int:
        self.nums = nums
        self.length = len(nums)
        self.scores = [[0 for _ in range(self.length // 2 + 1)] for _ in range(1 << self.length)]

        return self.dp((1 << self.length) - 1, 1)


    def dp(self, mask, k):
        # all the positions has been selected
        if mask == 0:
            return 0

        res = self.scores[mask][k]
        if res > 0:
            return res

        for i in range(self.length):
            for j in range(i + 1, self.length):
                if (mask & (1 << i)) and (mask & (1 << j)):
                    res = max(res, k * math.gcd(self.nums[i], self.nums[j]) + self.dp(mask ^ (1 << i) ^ (1 << j), k + 1))
                    self.scores[mask][k] = res
        
        return res
# @lc code=end

