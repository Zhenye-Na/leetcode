#
# @lc app=leetcode id=386 lang=python3
#
# [386] Lexicographical Numbers
#
# https://leetcode.com/problems/lexicographical-numbers/description/
#
# algorithms
# Medium (53.81%)
# Likes:    724
# Dislikes: 91
# Total Accepted:    64K
# Total Submissions: 117.6K
# Testcase Example:  '13'
#
# Given an integer n, return all the numbers in the range [1, n] sorted in
# lexicographical order.
# 
# 
# Example 1:
# Input: n = 13
# Output: [1,10,11,12,13,2,3,4,5,6,7,8,9]
# Example 2:
# Input: n = 2
# Output: [1,2]
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 5 * 10^4
# 
# 
# 
# Follow up: Could you optimize your solution to use O(n) runtime and O(1)
# space?
# 
#

# @lc code=start
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res = []
        curr_num = 1

        for i in range(n):
            res.append(curr_num)

            if curr_num * 10 <= n:
                curr_num *= 10
            else:
                while curr_num >= n:
                    curr_num = curr_num // 10

                curr_num += 1
                while curr_num % 10 == 0:
                    curr_num = curr_num // 10

        return res
# @lc code=end

