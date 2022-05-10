#
# @lc app=leetcode id=216 lang=python3
#
# [216] Combination Sum III
#
# https://leetcode.com/problems/combination-sum-iii/description/
#
# algorithms
# Medium (61.68%)
# Likes:    3120
# Dislikes: 76
# Total Accepted:    302.5K
# Total Submissions: 466.9K
# Testcase Example:  '3\n7'
#
# Find all valid combinations of k numbers that sum up to n such that the
# following conditions are true:
# 
# 
# Only numbers 1 through 9 are used.
# Each number is used at most once.
# 
# 
# Return a list of all possible valid combinations. The list must not contain
# the same combination twice, and the combinations may be returned in any
# order.
# 
# 
# Example 1:
# 
# 
# Input: k = 3, n = 7
# Output: [[1,2,4]]
# Explanation:
# 1 + 2 + 4 = 7
# There are no other valid combinations.
# 
# Example 2:
# 
# 
# Input: k = 3, n = 9
# Output: [[1,2,6],[1,3,5],[2,3,4]]
# Explanation:
# 1 + 2 + 6 = 9
# 1 + 3 + 5 = 9
# 2 + 3 + 4 = 9
# There are no other valid combinations.
# 
# 
# Example 3:
# 
# 
# Input: k = 4, n = 1
# Output: []
# Explanation: There are no valid combinations.
# Using 4 different numbers in the range [1,9], the smallest sum we can get is
# 1+2+3+4 = 10 and since 10 > 1, there are no valid combination.
# 
# 
# 
# Constraints:
# 
# 
# 2 <= k <= 9
# 1 <= n <= 60
# 
# 
#

# @lc code=start
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.res = []
        self.k = k
        numbers= [x for x in range(1, 10)]
        self.dfs(n, [], numbers, 0)
        return self.res
    
    def dfs(self, n, curr, numbers, i):
        if n == 0 and len(curr) == self.k:
            self.res.append(curr[:])
            return
        
        for idx in range(i, len(numbers)):
            if numbers[idx] <= n:
                curr.append(numbers[idx])
                self.dfs(n - numbers[idx], curr, numbers, idx + 1)
                curr.pop()
# @lc code=end

