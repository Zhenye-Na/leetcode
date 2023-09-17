#
# @lc app=leetcode id=847 lang=python3
#
# [847] Shortest Path Visiting All Nodes
#
# https://leetcode.com/problems/shortest-path-visiting-all-nodes/description/
#
# algorithms
# Hard (54.81%)
# Likes:    3520
# Dislikes: 146
# Total Accepted:    77.4K
# Total Submissions: 126.1K
# Testcase Example:  '[[1,2,3],[0],[0],[0]]'
#
# You have an undirected, connected graph of n nodes labeled from 0 to n - 1.
# You are given an array graph where graph[i] is a list of all the nodes
# connected with node i by an edge.
# 
# Return the length of the shortest path that visits every node. You may start
# and stop at any node, you may revisit nodes multiple times, and you may reuse
# edges.
# 
# 
# Example 1:
# 
# 
# Input: graph = [[1,2,3],[0],[0],[0]]
# Output: 4
# Explanation: One possible path is [1,0,2,0,3]
# 
# 
# Example 2:
# 
# 
# Input: graph = [[1],[0,2,4],[1,3,4],[2],[1,2]]
# Output: 4
# Explanation: One possible path is [0,1,4,2,3]
# 
# 
# 
# Constraints:
# 
# 
# n == graph.length
# 1 <= n <= 12
# 0 <= graph[i].length < n
# graph[i] does not contain i.
# If graph[a] contains b, then graph[b] contains a.
# The input graph is always connected.
# 
# 
#

# @lc code=start
from collections import deque

class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:

        n = len(graph)
        steps = 0

        target =  (1 << n) - 1
        visited = [[0 for _ in range(1 << n)] for _ in range(n)]

        queue = deque([])
        for i in range(n):
            queue.append((i, 1 << i ))

        while queue:
            size = len(queue)
            for _ in range(size):
                node, state = queue.popleft()

                if visited[node][state]:
                    continue

                if state == target:
                    return steps

                visited[node][state] = 1
                for nexts in graph[node]:

                    queue.append((nexts, (1 << nexts) | state))

            steps += 1

        return -1
# @lc code=end

