#
# @lc app=leetcode id=415 lang=python3
#
# [415] Add Strings
#
# https://leetcode.com/problems/add-strings/description/
#
# algorithms
# Easy (49.48%)
# Likes:    2189
# Dislikes: 431
# Total Accepted:    351.6K
# Total Submissions: 702.5K
# Testcase Example:  '"11"\n"123"'
#
# Given two non-negative integers, num1 and num2 represented as string, return
# the sum of num1 and num2 as a string.
# 
# You must solve the problem without using any built-in library for handling
# large integers (such as BigInteger). You must also not convert the inputs to
# integers directly.
# 
# 
# Example 1:
# 
# 
# Input: num1 = "11", num2 = "123"
# Output: "134"
# 
# 
# Example 2:
# 
# 
# Input: num1 = "456", num2 = "77"
# Output: "533"
# 
# 
# Example 3:
# 
# 
# Input: num1 = "0", num2 = "0"
# Output: "0"
# 
# 
# 
# Constraints:
# 
# 
# 1 <= num1.length, num2.length <= 10^4
# num1 and num2 consist of only digits.
# num1 and num2 don't have any leading zeros except for the zero itself.
# 
# 
#

# @lc code=start
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if not num1 and not num2:
            return ""
        
        if len(num1) == 0:
            return num2
        
        if len(num2) == 0:
            return num1
        
        l1, l2 = len(num1), len(num2)
        if l1 < l2:
            num1 = "0" * (l2 - l1) + num1
        if l1 > l2:
            num2 = "0" * (l1 - l2) + num2
        
        l = len(num1)
        res, carry = [], "0"
        i = 0
        for i in range(l - 1, -1, -1):
            d1, d2 = num1[i], num2[i]
            d = str(int(d1) + int(d2) + int(carry))
            if len(d) == 1:
                res.append(d)
                carry = "0"
            else:
                res.append(d[-1])
                carry = d[0]

        if carry == "0":
            return "".join(res[::-1])
        else:
            return "".join([carry] + res[::-1])
# @lc code=end

