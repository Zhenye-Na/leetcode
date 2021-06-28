#
# @lc app=leetcode id=1209 lang=python3
#
# [1209] Remove All Adjacent Duplicates in String II
#
# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/description/
#
# algorithms
# Medium (57.31%)
# Likes:    1399
# Dislikes: 32
# Total Accepted:    88.2K
# Total Submissions: 150.2K
# Testcase Example:  '"abcd"\n2'
#
# You are given a string s and an integer k, a k duplicate removal consists of
# choosing k adjacent and equal letters from s and removing them, causing the
# left and the right side of the deleted substring to concatenate together.
# 
# We repeatedly make k duplicate removals on s until we no longer can.
# 
# Return the final string after all such duplicate removals have been made. It
# is guaranteed that the answer is unique.
# 
# 
# Example 1:
# 
# 
# Input: s = "abcd", k = 2
# Output: "abcd"
# Explanation: There's nothing to delete.
# 
# Example 2:
# 
# 
# Input: s = "deeedbbcccbdaa", k = 3
# Output: "aa"
# Explanation: 
# First delete "eee" and "ccc", get "ddbbbdaa"
# Then delete "bbb", get "dddaa"
# Finally delete "ddd", get "aa"
# 
# Example 3:
# 
# 
# Input: s = "pbbcggttciiippooaais", k = 2
# Output: "ps"
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 10^5
# 2 <= k <= 10^4
# s only contains lower case English letters.
# 
# 
#

# @lc code=start
from collections import defaultdict

# Improved Approach
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for char in s:
            if not stack or stack[-1][0] != char:
                stack.append([char, 1])
            else:
                _, times = stack[-1]
                if times + 1 == k:
                    stack.pop()
                else:
                    stack[-1][1] += 1

        res = ""
        while stack:
            char, times = stack.pop()
            res += char * times

        return res[::-1]




# Naive approach
# Use stack to store chars and hashmap to store the appearance

# Passed all the test case but too slow
# TLE
class Solution_TLE:
    def removeDuplicates(self, s: str, k: int) -> str:
        if not s or len(s) == 0 or k == 0:
            return ""

        stack = []
        l = len(s)

        counter = defaultdict(int)
        for i in range(l):

            counter[s[i]] += 1
            if counter[s[i]] >= k and stack[-1] == s[i]:
                d = 0
                prev_chars = set([stack[len(stack) - 1 - d] for d in range(k - 1)])
                if len(prev_chars) == 1 and list(prev_chars)[0] == s[i]:
                    for _ in range(k - 1):
                        stack.pop()
                    counter[s[i]] -= k
                    if counter[s[i]] == 0:
                        del counter[s[i]]
                else:
                    stack.append(s[i])

            else:
                stack.append(s[i])

        return "".join(stack)
# @lc code=end

