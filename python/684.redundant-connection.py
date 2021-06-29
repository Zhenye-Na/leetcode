#
# @lc app=leetcode id=684 lang=python3
#
# [684] Redundant Connection
#
# https://leetcode.com/problems/redundant-connection/description/
#
# algorithms
# Medium (59.56%)
# Likes:    2496
# Dislikes: 264
# Total Accepted:    148.8K
# Total Submissions: 249K
# Testcase Example:  '[[1,2],[1,3],[2,3]]'
#
# In this problem, a tree is an undirected graph that is connected and has no
# cycles.
# 
# You are given a graph that started as a tree with n nodes labeled from 1 to
# n, with one additional edge added. The added edge has two different vertices
# chosen from 1 to n, and was not an edge that already existed. The graph is
# represented as an array edges of length n where edges[i] = [ai, bi] indicates
# that there is an edge between nodes ai and bi in the graph.
# 
# Return an edge that can be removed so that the resulting graph is a tree of n
# nodes. If there are multiple answers, return the answer that occurs last in
# the input.
# 
# 
# Example 1:
# 
# 
# Input: edges = [[1,2],[1,3],[2,3]]
# Output: [2,3]
# 
# 
# Example 2:
# 
# 
# Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
# Output: [1,4]
# 
# 
# 
# Constraints:
# 
# 
# n == edges.length
# 3 <= n <= 1000
# edges[i].length == 2
# 1 <= ai < bi <= edges.length
# ai != bi
# There are no repeated edges.
# The given graph is connected.
# 
# 
#

# @lc code=start
class UnionFind:

    def __init__(self, n):
        self.parent = {i: i for i in range(1, n + 1)}

    def find(self, node):
        path = []
        while node != self.parent[node]:
            path.append(node)
            node = self.parent[node]

        for p in path:
            self.parent[p] = node

        return node

    def union(self, node1, node2):
        parent1, parent2 = self.find(node1), self.find(node2)
        if parent1 != parent2:
            self.parent[max(parent1, parent2)] = min(parent1, parent2)
            return False

        return True



class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        if not edges or len(edges) == 0:
            return [0, 0]

        ans = []
        max_node = -1
        for edge in edges:
            max_node = max(max_node, max(edge))

        uf = UnionFind(max_node)
        for edge in edges:
            res = uf.union(edge[0], edge[1])
            if res:
                ans.append(edge)

        return ans.pop() if ans else [0, 0]
# @lc code=end

