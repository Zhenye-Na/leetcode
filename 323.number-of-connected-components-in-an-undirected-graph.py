#
# @lc app=leetcode id=323 lang=python3
#
# [323] Number of Connected Components in an Undirected Graph
#

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


class Solution:
    def numOfComponent(self, n: int, edges :List[List[int]]) -> int:
        if not n or n < 0:
            return 0

        uf = UnionFind(n)
        for edge in edges:
            uf.union(edge[0], edge[1])

        return uf.size

