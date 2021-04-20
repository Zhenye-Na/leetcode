#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#
# https://leetcode.com/problems/add-binary/description/
#
# algorithms
# Easy (46.70%)
# Likes:    2566
# Dislikes: 331
# Total Accepted:    572.1K
# Total Submissions: 1.2M
# Testcase Example:  '"11"\n"1"'
#
# Given two binary strings a and b, return their sum as a binary string.
# 
# 
# Example 1:
# Input: a = "11", b = "1"
# Output: "100"
# Example 2:
# Input: a = "1010", b = "1011"
# Output: "10101"
# 
# 
# Constraints:
# 
# 
# 1 <= a.length, b.length <= 10^4
# a and b consist only of '0' or '1' characters.
# Each string does not contain leading zeros except for the zero itself.
# 
# 
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) < len(b):
            a = "0" * (len(b) - len(a)) + a
        else:
            b = "0" * (len(a) - len(b)) + b

        last_pointer = len(a) - 1
        mark = 0
        res = []
        while last_pointer >= 0:
            tmp = int(a[last_pointer]) + int(b[last_pointer]) + mark
            if tmp >= 2:
                mark = tmp // 2
                res.insert(0, str(tmp % 2))
            else:
                res.insert(0, str(tmp))
                mark = 0


            last_pointer -= 1

        if last_pointer == -1 and mark != 0:
            res.insert(0, str(mark))

        return "".join(res)
        
# @lc code=end

