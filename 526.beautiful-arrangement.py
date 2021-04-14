#
# @lc app=leetcode id=526 lang=python3
#
# [526] Beautiful Arrangement
#
# https://leetcode.com/problems/beautiful-arrangement/description/
#
# algorithms
# Medium (61.70%)
# Likes:    1234
# Dislikes: 217
# Total Accepted:    89.6K
# Total Submissions: 144.2K
# Testcase Example:  '2'
#
# Suppose you have n integers labeled 1 through n. A permutation of those n
# integers perm (1-indexed) is considered a beautiful arrangement if for every
# i (1 <= i <= n), either of the following is true:
# 
# 
# perm[i] is divisible by i.
# i is divisible by perm[i].
# 
# 
# Given an integer n, return the number of the beautiful arrangements that you
# can construct.
# 
# 
# Example 1:
# 
# 
# Input: n = 2
# Output: 2
# Explanation: 
# The first beautiful arrangement is [1,2]:
# ⁠   - perm[1] = 1 is divisible by i = 1
# ⁠   - perm[2] = 2 is divisible by i = 2
# The second beautiful arrangement is [2,1]:
# ⁠   - perm[1] = 2 is divisible by i = 1
# ⁠   - i = 2 is divisible by perm[2] = 1
# 
# 
# Example 2:
# 
# 
# Input: n = 1
# Output: 1
# 
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 15
# 
# 
#

# @lc code=start
# DFS
class Solution:
    def countArrangement(self, n: int) -> int:
        self.count = 0
        self.res = []
        self.dfs([0], n, 1)
        return self.count


    def dfs(self, curr, n, start):
        if len(curr) == n + 1:
            self.count += 1
            self.res.append(curr[:])
            return

        next_idx = len(curr)
        for num in range(1, n + 1):
            if (num % next_idx == 0 or next_idx % num == 0) and num not in curr:
                curr.append(num)
                self.dfs(curr, n, start)
                curr.pop()


    def print_out(self):
        return self.res
# @lc code=end

