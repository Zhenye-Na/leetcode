#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#
# https://leetcode.com/problems/generate-parentheses/description/
#
# algorithms
# Medium (64.94%)
# Likes:    7249
# Dislikes: 314
# Total Accepted:    695.6K
# Total Submissions: 1.1M
# Testcase Example:  '3'
#
# Given n pairs of parentheses, write a function to generate all combinations
# of well-formed parentheses.
# 
# 
# Example 1:
# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:
# Input: n = 1
# Output: ["()"]
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 8
# 
# 
#

# @lc code=start

# during each iteration, left Parenthesis <= right Parenthesis, all the time

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.res = []
        self._dfs(n, n, "", 2 * n)
        return self.res


    def _dfs(self, left_count, right_count, curr, target_length):
        if len(curr) == target_length:
            self.res.append(curr)

        if left_count > 0:
            self._dfs(left_count - 1, right_count, curr + "(", target_length)

        if left_count < right_count:
            self._dfs(left_count, right_count - 1, curr + ")", target_length)
# @lc code=end

