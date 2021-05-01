#
# @lc app=leetcode id=970 lang=python3
#
# [970] Powerful Integers
#
# https://leetcode.com/problems/powerful-integers/description/
#
# algorithms
# Easy (39.91%)
# Likes:    99
# Dislikes: 44
# Total Accepted:    35.7K
# Total Submissions: 84.4K
# Testcase Example:  '2\n3\n10'
#
# Given three integers x, y, and bound, return a list of all the powerful
# integers that have a value less than or equal to bound.
# 
# An integer is powerful if it can be represented as x^i + y^j for some
# integers i >= 0 and j >= 0.
# 
# You may return the answer in any order. In your answer, each value should
# occur at most once.
# 
# 
# Example 1:
# 
# 
# Input: x = 2, y = 3, bound = 10
# Output: [2,3,4,5,7,9,10]
# Explanation:
# 2 = 2^0 + 3^0
# 3 = 2^1 + 3^0
# 4 = 2^0 + 3^1
# 5 = 2^1 + 3^1
# 7 = 2^2 + 3^1
# 9 = 2^3 + 3^0
# 10 = 2^0 + 3^2
# 
# 
# Example 2:
# 
# 
# Input: x = 3, y = 5, bound = 15
# Output: [2,4,6,8,10,14]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= x, y <= 100
# 0 <= bound <= 10^6
# 
# 
#

# @lc code=start
class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        if bound < 2:
            return []

        res = []
        i, j = 0, 0
        if x != 1:
            while x ** i <= bound:
                i += 1
        else:
            i = 1
        max_i = i

        if y != 1:
            while y ** j <= bound:
                j += 1
        else:
            j = 1
        max_j = j

        seen = set([])
        for i in range(max_i):
            for j in range(max_j):
                total = x ** i + y ** j
                if total <= bound and total not in seen:
                    res.append(total)
                    seen.add(total)

        return res
# @lc code=end

