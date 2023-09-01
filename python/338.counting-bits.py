#
# @lc app=leetcode id=338 lang=python3
#
# [338] Counting Bits
#
# https://leetcode.com/problems/counting-bits/description/
#
# algorithms
# Medium (70.26%)
# Likes:    3772
# Dislikes: 207
# Total Accepted:    348.3K
# Total Submissions: 493.3K
# Testcase Example:  '2'
#
# Given an integer num, return an array of the number of 1's in the binary
# representation of every number in the range [0, num].
# 
# 
# Example 1:
# 
# 
# Input: num = 2
# Output: [0,1,1]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
# 
# 
# Example 2:
# 
# 
# Input: num = 5
# Output: [0,1,1,2,1,2]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
# 3 --> 11
# 4 --> 100
# 5 --> 101
# 
# 
# 
# Constraints:
# 
# 
# 0 <= num <= 10^5
# 
# 
# 
# Follow up:
# 
# 
# It is very easy to come up with a solution with run time O(32n). Can you do
# it in linear time O(n) and possibly in a single pass?
# Could you solve it in O(n) space complexity?
# Can you do it without using any built-in function (i.e., like
# __builtin_popcount in C++)?
# 
# 
#

# @lc code=start
class Solution:
    def countBits(self, num: int) -> List[int]:
        res = []
        for n in range(0, num + 1):
            count = 0
            while n != 0:
                if n < len(res):
                    count += res[n]
                    break
                if n & 1 == 1:
                    count += 1
                n = n >> 1

            res.append(count)
        return res


class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        
        for i in range(n + 1):
            total = 0
            while i > 0:
                total += i & 1
                i = i >> 1
        
            res.append(total)
        
        return res
# @lc code=end

