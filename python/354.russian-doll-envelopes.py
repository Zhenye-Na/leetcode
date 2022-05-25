#
# @lc app=leetcode id=354 lang=python3
#
# [354] Russian Doll Envelopes
#
# https://leetcode.com/problems/russian-doll-envelopes/description/
#
# algorithms
# Hard (38.58%)
# Likes:    3387
# Dislikes: 81
# Total Accepted:    143.6K
# Total Submissions: 370.9K
# Testcase Example:  '[[5,4],[6,4],[6,7],[2,3]]'
#
# You are given a 2D array of integers envelopes where envelopes[i] = [wi, hi]
# represents the width and the height of an envelope.
# 
# One envelope can fit into another if and only if both the width and height of
# one envelope are greater than the other envelope's width and height.
# 
# Return the maximum number of envelopes you can Russian doll (i.e., put one
# inside the other).
# 
# Note: You cannot rotate an envelope.
# 
# 
# Example 1:
# 
# 
# Input: envelopes = [[5,4],[6,4],[6,7],[2,3]]
# Output: 3
# Explanation: The maximum number of envelopes you can Russian doll is 3 ([2,3]
# => [5,4] => [6,7]).
# 
# 
# Example 2:
# 
# 
# Input: envelopes = [[1,1],[1,1],[1,1]]
# Output: 1
# 
# 
# 
# Constraints:
# 
# 
# 1 <= envelopes.length <= 10^5
# envelopes[i].length == 2
# 1 <= wi, hi <= 10^5
# 
# 
#

# @lc code=start
class Solution_DP:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], x[1]))
        n = len(envelopes)

        # f[i] represents length of longest increasing subsequence
        f =[1 for _ in range(n)]
        for i in range(n):
            for j in range(i):
                if envelopes[j][1] < envelopes[i][1] and envelopes[j][0] < envelopes[i][0]:
                    f[i] = max(f[i], f[j] + 1)

        return max(f)


class Solution_Greedy:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        return self.greedy_lis([x[1] for x in envelopes])
        
    def greedy_lis(self, nums: List[int]) -> int:
        res = []
        for num in nums:
            idx = bisect_left(res, num)
            if idx == len(res):
                res.append(num)
            else:
                res[idx] = num

        return len(res)
# @lc code=end

