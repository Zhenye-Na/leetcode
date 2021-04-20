#
# @lc app=leetcode id=301 lang=python3
#
# [301] Remove Invalid Parentheses
#
# https://leetcode.com/problems/remove-invalid-parentheses/description/
#
# algorithms
# Hard (44.46%)
# Likes:    3255
# Dislikes: 151
# Total Accepted:    258.9K
# Total Submissions: 577.9K
# Testcase Example:  '"()())()"'
#
# Given a string s that contains parentheses and letters, remove the minimum
# number of invalid parentheses to make the input string valid.
# 
# Return all the possible results. You may return the answer in any order.
# 
# 
# Example 1:
# 
# 
# Input: s = "()())()"
# Output: ["(())()","()()()"]
# 
# 
# Example 2:
# 
# 
# Input: s = "(a)())()"
# Output: ["(a())()","(a)()()"]
# 
# 
# Example 3:
# 
# 
# Input: s = ")("
# Output: [""]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 25
# s consists of lowercase English letters and parentheses '(' and ')'.
# There will be at most 20 parentheses in s.
# 
# 
#

# @lc code=start
# DFS without pruning
# Runtime: 7544 ms
# Memory Usage: 14.6 MB
class Solution_DFS_WithoutPruning:

    def removeInvalidParentheses(self, s: str) -> List[str]:
        
        max_len = self._get_max_length(s)
        res = []
        self._dfs(max_len, s, res, [], 0)
        return res


    def _get_max_length(self, s):
        stack = []
        length = 0
        for i, char in enumerate(s):
            if char not in "()":
                length += 1
            elif char == "(":
                stack.append(char)
            else:
                if stack and stack[-1] == "(":
                    stack.pop()
                    length += 2

        return length


    def _dfs(self, length, s, res, curr, start):
        if len(curr) == length:
            if self.valid(curr[:]):
                tmp = "".join(curr[:])
                if tmp not in res:
                    res.append(tmp)
            return

        if len(curr) > length:
            return

        for i in range(start, len(s)):
            curr.append(s[i])
            self._dfs(length, s, res, curr, i + 1)
            curr.pop()


    def valid(self, s: str) -> bool:
        if not s or len(s) == 0:
            return True

        stack = []
        for i in range(len(s)):
            if s[i] not in "()":
                continue

            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                stack.append(s[i])
            else:
                if len(stack) == 0:
                    return False

                if ( s[i] == ')' and stack[-1] != '(' ) or ( s[i] == ']' and stack[-1] != '[' ) or ( s[i] == '}' and stack[-1] != '{' ):
                    return False

                stack.pop()

        return len(stack) == 0


# DFS with pruning
# Runtime: 80 ms
# Memory Usage: 14.3 MB
class Solution:

    def __init__(self):
        self.res = []

    def removeInvalidParentheses(self, s: str) -> List[str]:
        max_len = self._get_max_length(s)

        self.dfs(s, "", max_len, 0, 0)
        return self.res


    def dfs(self, s, curr, max_len, i, left_count):
        if len(curr) > max_len or left_count < 0:
            return

        if i == len(s):
            if len(curr) == max_len and left_count == 0:
                self.res.append(curr[:])
            return

        # dfs with pruning
        #   https://www.youtube.com/watch?v=NWAseBzZj-c&ab_channel=HuifengGuan

        # if s[i] == curr[-1]:
        #     have to select s[i]
        # else: # s[i] != curr[-1]
        #     we can select s[i]
        #     we can skip s[i] (dont add s[i] to curr)

        if s[i] != "(" and s[i] != ")":
            self.dfs(s, curr + s[i], max_len, i + 1, left_count)
        else:
            self.dfs(s, curr + s[i], max_len, i + 1, left_count + (1 if s[i] == "(" else -1))
            if len(curr) == 0 or s[i] != curr[-1]:
                self.dfs(s, curr, max_len, i + 1, left_count)


    def _get_max_length(self, s):
        stack = []
        length = 0
        for i, char in enumerate(s):
            if char not in "()":
                length += 1
            elif char == "(":
                stack.append(char)
            else:
                if stack and stack[-1] == "(":
                    stack.pop()
                    length += 2

        return length
# @lc code=end

