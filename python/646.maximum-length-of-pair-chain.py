#
# @lc app=leetcode id=646 lang=python3
#
# [646] Maximum Length of Pair Chain
#
# https://leetcode.com/problems/maximum-length-of-pair-chain/description/
#
# algorithms
# Medium (54.11%)
# Likes:    3269
# Dislikes: 118
# Total Accepted:    151.7K
# Total Submissions: 264.6K
# Testcase Example:  '[[1,2],[2,3],[3,4]]'
#
# You are given an array of n pairs pairs where pairs[i] = [lefti, righti] and
# lefti < righti.
# 
# A pair p2 = [c, d] follows a pair p1 = [a, b] if b < c. A chain of pairs can
# be formed in this fashion.
# 
# Return the length longest chain which can be formed.
# 
# You do not need to use up all the given intervals. You can select pairs in
# any order.
# 
# 
# Example 1:
# 
# 
# Input: pairs = [[1,2],[2,3],[3,4]]
# Output: 2
# Explanation: The longest chain is [1,2] -> [3,4].
# 
# 
# Example 2:
# 
# 
# Input: pairs = [[1,2],[7,8],[4,5]]
# Output: 3
# Explanation: The longest chain is [1,2] -> [4,5] -> [7,8].
# 
# 
# 
# Constraints:
# 
# 
# n == pairs.length
# 1 <= n <= 1000
# -1000 <= lefti < righti <= 1000
# 
# 
#

# @lc code=start
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        if not pairs:
            return 0

        pairs.sort(key=lambda x: x[1])
        prev = -1001
        count = 0

        for idx in range(len(pairs)):
            if pairs[idx][0] > prev:
                prev = pairs[idx][1]
                count += 1

        return count
# @lc code=end

