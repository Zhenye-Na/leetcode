#
# @lc app=leetcode id=77 lang=python3
#
# [77] Combinations
#
# https://leetcode.com/problems/combinations/description/
#
# algorithms
# Medium (57.08%)
# Likes:    2094
# Dislikes: 80
# Total Accepted:    351.4K
# Total Submissions: 609.1K
# Testcase Example:  '4\n2'
#
# Given two integers n and k, return all possible combinations of k numbers out
# of 1 ... n.
# 
# You may return the answer in any order.
# 
# 
# Example 1:
# 
# 
# Input: n = 4, k = 2
# Output:
# [
# ⁠ [2,4],
# ⁠ [3,4],
# ⁠ [2,3],
# ⁠ [1,2],
# ⁠ [1,3],
# ⁠ [1,4],
# ]
# 
# 
# Example 2:
# 
# 
# Input: n = 1, k = 1
# Output: [[1]]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 20
# 1 <= k <= n
# 
# 
#

# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if n == k:
            return [[i for i in range(1, n + 1)]]

        self.res = []
        self._dfs(n, k, 1, [])
        return self.res

    def _dfs(self, n, k, start, curr):
        if len(curr) == k:
            self.res.append(curr[:])
            return

        if start > n:
            return

        for i in range(start, n + 1):
            curr.append(i)
            self._dfs(n, k, i + 1, curr)
            curr.pop()
# @lc code=end

