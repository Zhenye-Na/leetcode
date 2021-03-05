# Graph Valid Tree

# Description
# Given n nodes labeled from 0 to n - 1 and a list of undirected edges
# (each edge is a pair of nodes), write a function to check whether these
# edges make up a valid tree.

# You can assume that no duplicate edges will appear in edges. Since all
# edges are undirected, [0, 1] is the same as [1, 0] and thus will not
# appear together in edges.


# Example

# Example 1:

# Input: n = 5 edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
# Output: true.

# Example 2:

# Input: n = 5 edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
# Output: false.

from collections import defaultdict, deque

class Solution_BFS:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def __init__(self):
        self.neighbors = defaultdict(list)

    def validTree(self, n, edges):
        # write your code here
        if n - 1 != len(edges):
            return False

        self._build_neighbors(edges)
        queue = deque([0])
        seen = set([0])

        while queue:
            node = queue.popleft()
            for neighbor in self.neighbors[node]:
                if neighbor not in seen:
                    queue.append(neighbor)
                    seen.add(neighbor)

        return len(seen) == n


    def _build_neighbors(self, edges):
        for start, end in edges:
            self.neighbors[start].append(end)
            self.neighbors[end].append(start)


class UnionFind():
    def __init__(self, n):
        self.father = {}
        for i in range(n):
            self.father[i] = i
        self.count = n


    def find(self, other):
        path = []
        while other != self.father[other]:
            path.append(other)
            other = self.father[other]

        for p in path:
            self.father[p] = other

        return other

    def union(self, a, b):
        father_a = self.find(a)
        father_b = self.find(b)
        if father_a != father_b:
            self.father[father_a] = father_b
            self.count -= 1


class Solution_UnionFind:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def validTree(self, n, edges):
        # write your code here
        if n - 1 != len(edges):
            return False

        uf = UnionFind(n)
        for start, end in edges:
            uf.union(start, end)

        return uf.count == 1