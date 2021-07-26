#
# @lc app=leetcode id=600 lang=python3
#
# [600] Non-negative Integers without Consecutive Ones
#
# https://leetcode.com/problems/non-negative-integers-without-consecutive-ones/description/
#
# algorithms
# Hard (34.56%)
# Likes:    800
# Dislikes: 96
# Total Accepted:    23.8K
# Total Submissions: 63.6K
# Testcase Example:  '5'
#
# Given a positive integer n, return the number of the integers in the range
# [0, n] whose binary representations do not contain consecutive ones.
# 
# 
# Example 1:
# 
# 
# Input: n = 5
# Output: 5
# Explanation:
# Here are the non-negative integers <= 5 with their corresponding binary
# representations:
# 0 : 0
# 1 : 1
# 2 : 10
# 3 : 11
# 4 : 100
# 5 : 101
# Among them, only integer 3 disobeys the rule (two consecutive ones) and the
# other 5 satisfy the rule. 
# 
# 
# Example 2:
# 
# 
# Input: n = 1
# Output: 2
# 
# 
# Example 3:
# 
# 
# Input: n = 2
# Output: 3
# 
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 10^9
# 
# 
#

# @lc code=start
class Solution:
    def findIntegers(self, n: int) -> int:
        if n < 2:
            return n + 1
        
        bits = bin(n).replace('0b', '')
        bits = bits[::-1]
        k = len(bits)
        
        f = [0] * k
        f[0] = 1
        f[1] = 2
        for i in range(2, k):
            f[i] = f[i - 1] + f[i - 2]
        
        ans = 0
        for i in range(k - 1, -1, -1):
            if bits[i] == '1':
                ans += f[i]
                if i < k - 1 and bits[i + 1] == '1':
                    return ans

        ans += 1
        return ans
# @lc code=end

