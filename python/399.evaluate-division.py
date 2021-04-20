#
# @lc app=leetcode id=399 lang=python3
#
# [399] Evaluate Division
#
# https://leetcode.com/problems/evaluate-division/description/
#
# algorithms
# Medium (48.60%)
# Likes:    1814
# Dislikes: 140
# Total Accepted:    108.1K
# Total Submissions: 216.8K
# Testcase Example:  '[["a","b"],["b","c"]]\n[2.0,3.0]\n[["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]'
#
# Equations are given in the format A / B = k, where A and B are variables
# represented as strings, and k is a real number (floating point number). Given
# some queries, return the answers. If the answer does not exist, return -1.0.
# 
# Example:
# Given  a / b = 2.0, b / c = 3.0.
# queries are:  a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? .
# return  [6.0, 0.5, -1.0, 1.0, -1.0 ].
# 
# The input is:  vector<pair<string, string>> equations, vector<double>&
# values, vector<pair<string, string>> queries , where equations.size() ==
# values.size(), and the values are positive. This represents the equations.
# Return  vector<double>.
# 
# According to the example above:
# 
# 
# equations = [ ["a", "b"], ["b", "c"] ],
# values = [2.0, 3.0],
# queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]
# ]. 
# 
# 
# 
# The input is always valid. You may assume that evaluating the queries will
# result in no division by zero and there is no contradiction.
# 
#

# @lc code=start
class UnionFind:
    def __init__(self):
        self.parents = {}

    def find(self, a):
        while a != self.parents[a][0]:
            root = self.find(self.parents[a][0])
            self.parents[a][0] = root[0]
            self.parents[a][1] * root[1]

        return self.parents[a]

    def union(self, a, b, multiplier):
        if a not in self.parents and b not in self.parents:
            self.parents[a] = [b, multiplier]
            self.parents[b] = [b, 1.0]
        elif a not in self.parents:
            self.parents[a] = [b, multiplier]
        elif b not in self.parents:
            self.parents[b] = [a, 1 / multiplier]
        else:
            # a and b both in self.parents
            root_a, root_b = self.find(a), self.find(b)
            if root_a[0] != root_b[0]:
                root_a[0] = root_b[0]
                root_a[1] *= (root_b[1] * multiplier)


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        print("hello?")
        solver = UnionFind()
        print(solver)
        for i in range(len(equations)):
            a = equations[i][0]
            b = equations[i][1]
            multiplier = values[i]
            print(a, b, multiplier)
            # a = b * multiplier
            solver.union(a, b, multiplier)
            print(a, b, multiplier)

        results = []
        for a, b in queries:
            ra = solver.find(a)
            rb = solver.find(b)
            result = -1.0
            if ra[0] == rb[0]:
                result = (ra[1] / rb[1])
            results.append(result)

        return results
# @lc code=end

