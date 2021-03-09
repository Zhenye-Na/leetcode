#
# @lc app=leetcode id=323 lang=python3
#
# [323] Number of Connected Components in an Undirected Graph
#
#
# Given n nodes labeled from 0 to n - 1 and a list of undirected edges
# (each edge is a pair of nodes), write a function to find the number of
# connected components in an undirected graph.
#
# Example 1:
#
# Input: n = 5 and edges = [[0, 1], [1, 2], [3, 4]]
#
#      0          3
#      |          |
#      1 --- 2    4
#
# Output: 2
# Example 2:
#
# Input: n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]]
#
#      0           4
#      |           |
#      1 --- 2 --- 3
#
# Output:  1
#
# Note:
#
# You can assume that no duplicate edges will appear in edges. Since all
# edges are undirected, [0, 1] is the same as [1, 0] and thus will not
# appear together in edges.

# @lc code=start
class UnionFind:

    def __init__(self, n):
        self.parent = {i : i for i in range(n)}
        self.size = n

    def find(self, node):
        path = []
        while node != self.parent[node]:
            path.append(node)
            node = self.parent[node]

        for point in path:
            self.parent[point] = node

        return node

    def union(self, node1, node2):
        parent1, parent2 = self.find(node1), self.find(node2)
        if parent1 != parent2:
            self.parent[max(parent1, parent2)] = min(parent1, parent2)
            self.size -= 1

    def get_size(self):
        return self.size

class Solution:
    def numOfComponent(self, n: int, edges :List[List[int]]) -> int:
        if not n or n < 0:
            return 0

        uf = UnionFind(n)
        for edge in edges:
            uf.union(edge[0], edge[1])

        return uf.get_size()

# @lc code=end

