#
# @lc app=leetcode id=997 lang=python3
#
# [997] Find the Town Judge
#
# https://leetcode.com/problems/find-the-town-judge/description/
#
# algorithms
# Easy (49.91%)
# Likes:    2903
# Dislikes: 227
# Total Accepted:    244.7K
# Total Submissions: 487.6K
# Testcase Example:  '2\n[[1,2]]'
#
# In a town, there are n people labeled from 1 to n. There is a rumor that one
# of these people is secretly the town judge.
# 
# If the town judge exists, then:
# 
# 
# The town judge trusts nobody.
# Everybody (except for the town judge) trusts the town judge.
# There is exactly one person that satisfies properties 1 and 2.
# 
# 
# You are given an array trust where trust[i] = [ai, bi] representing that the
# person labeled ai trusts the person labeled bi.
# 
# Return the label of the town judge if the town judge exists and can be
# identified, or return -1 otherwise.
# 
# 
# Example 1:
# 
# 
# Input: n = 2, trust = [[1,2]]
# Output: 2
# 
# 
# Example 2:
# 
# 
# Input: n = 3, trust = [[1,3],[2,3]]
# Output: 3
# 
# 
# Example 3:
# 
# 
# Input: n = 3, trust = [[1,3],[2,3],[3,1]]
# Output: -1
# 
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 1000
# 0 <= trust.length <= 10^4
# trust[i].length == 2
# All the pairs of trust are unique.
# ai != bi
# 1 <= ai, bi <= n
# 
# 
#

# @lc code=start
from collections import defaultdict

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1 and not trust:
            return 1

        # key is someone who is trusted
        # value is number of ppl who turst him/her
        trustee = defaultdict(int)

        # key is ppl
        # value is list of ppl who he/she trusts
        trusters = defaultdict(list)

        for a, b in trust:
            trustee[b] += 1
            trusters[a].append(b)

        for i in range(1, n + 1):
            if trustee.get(i, -1) == n - 1 and i not in trusters:
                return i

        return -1
# @lc code=end

