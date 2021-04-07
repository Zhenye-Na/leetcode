#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#
# https://leetcode.com/problems/palindrome-number/description/
#
# algorithms
# Easy (49.55%)
# Likes:    3196
# Dislikes: 1722
# Total Accepted:    1.2M
# Total Submissions: 2.4M
# Testcase Example:  '121'
#
# Given an integer x, return true if x is palindrome integer.
# 
# An integer is a palindrome when it reads the same backward as forward. For
# example, 121 is palindrome while 123 is not.
# 
# 
# Example 1:
# 
# 
# Input: x = 121
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it
# becomes 121-. Therefore it is not a palindrome.
# 
# 
# Example 3:
# 
# 
# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
# 
# 
# Example 4:
# 
# 
# Input: x = -101
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# -2^31 <= x <= 2^31 - 1
# 
# 
# 
# Follow up: Could you solve it without converting the integer to a string?
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        reversed_x = 0
        num = x

        while num > 0:
            reversed_x = reversed_x * 10 + num % 10
            num = num // 10

        return reversed_x == x



class Solution_HashMap:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        hashmap = {}

        n = self.get_digits(x)
        curr = n - 1
        for _ in range(n):
            num = x % 10
            if n - curr - 1 in hashmap:
                if hashmap[n - curr - 1] != num:
                    return False
            else:
                hashmap[curr] = num
            
            x = x // 10
            curr -= 1

        return True


    def get_digits(self, x):
        count = 0
        while x != 0:
            x = x // 10
            count += 1
        return count
# @lc code=end

