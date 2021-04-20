#
# @lc app=leetcode id=785 lang=python3
#
# [785] Is Graph Bipartite?
#
# https://leetcode.com/problems/is-graph-bipartite/description/
#
# algorithms
# Medium (48.23%)
# Likes:    2420
# Dislikes: 219
# Total Accepted:    184.3K
# Total Submissions: 378.9K
# Testcase Example:  '[[1,2,3],[0,2],[0,1,3],[0,2]]'
#
# There is an undirected graph with n nodes, where each node is numbered
# between 0 and n - 1. You are given a 2D array graph, where graph[u] is an
# array of nodes that node u is adjacent to. More formally, for each v in
# graph[u], there is an undirected edge between node u and node v. The graph
# has the following properties:
# 
# 
# There are no self-edges (graph[u] does not contain u).
# There are no parallel edges (graph[u] does not contain duplicate values).
# If v is in graph[u], then u is in graph[v] (the graph is undirected).
# The graph may not be connected, meaning there may be two nodes u and v such
# that there is no path between them.
# 
# 
# A graph is bipartite if the nodes can be partitioned into two independent
# sets A and B such that every edge in the graph connects a node in set A and a
# node in set B.
# 
# Return true if and only if it is bipartite.
# 
# 
# Example 1:
# 
# 
# Input: graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
# Output: false
# Explanation: There is no way to partition the nodes into two independent sets
# such that every edge connects a node in one and a node in the other.
# 
# Example 2:
# 
# 
# Input: graph = [[1,3],[0,2],[1,3],[0,2]]
# Output: true
# Explanation: We can partition the nodes into two sets: {0, 2} and {1, 3}.
# 
# 
# Constraints:
# 
# 
# graph.length == n
# 1 <= n <= 100
# 0 <= graph[u].length < n
# 0 <= graph[u][i] <= n - 1
# graph[u] does not contain u.
# All the values of graph[u] are unique.
# If graph[u] contains v, then graph[v] contains u.
# 
# 
#

# @lc code=start
from collections import deque

class Solution_BFS:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        if not graph or len(graph) == 0:
            return True

        n = len(graph)
        visited = [0 for _ in range(n)]
        color = [0 for _ in range(n)]

        for i in range(n):
            if visited[i] == 0 and len(graph[i]) >= 1:
                queue = deque([i])
                colors[i] = 1

            while queue:
                node = queue.popleft()
                neighbors = graph[node]
                
                for neighbor in neighbors:
                    if visited[neighbor] == 1:
                        if colors[neighbor] == colors[node]:
                            return False
                    else:
                        colors[neighbor] = - colors[node]
                        queue.append(neighbor)
                        visited[neighbor] = 1

        return True



class UnionFind:

    def __init__(self, n):
        self.leader = {}
        for i in range(n):
            self.leader[i] = i

    def find(self, a):
        path = []
        while a != self.leader[a]:
            path.append(a)
            a = self.leader[a]

        for node in path:
            self.leader[node] = a

        return a


    def union(self, a, b):
        leader_a, leader_b = self.find(a), self.find(b)
        if leader_a != leader_b:
            self.leader[leader_a] = leader_b


class Solution_UnionFind:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        if not graph or len(graph) == 0:
            return True

        n = len(graph)
        uf = UnionFind(n)

        for i in range(n):
            if len(graph[i]) <= 0:
                continue

            leader_i, leader_child = uf.find(i), uf.find(graph[i][0])
            if leader_i == leader_child:
                return False

            # union neighbors
            for j in range(1, len(graph[i])):
                leader_j = uf.find(graph[i][j])
                if leader_j == leader_i:
                    return False

                uf.union(leader_child, graph[i][j])

        return True

# @lc code=end

