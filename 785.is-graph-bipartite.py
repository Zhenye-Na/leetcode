#
# @lc app=leetcode id=785 lang=python3
#
# [785] Is Graph Bipartite?
#
from collections import deque

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        if not graph or len(graph) == 0:
            return False

        n = len(graph)
        visited = [0 for _ in range(n)]
        color = [0 for _ in range(n)]

        for i in range(n):
            if len(graph[i]) > 0 and visited[i] == 0:
                visited[i] = 1
                color[i] = 1
                queue = deque([i])

                while queue:
                    node = queue.popleft()
                    for neighbor in graph[node]:
                        if visited[neighbor]:
                            if color[node] == color[neighbor]:
                                return False
                        else:
                            visited[neighbor] = 1
                            color[neighbor] = - color[node]
                            queue.append(neighbor)

        return True
