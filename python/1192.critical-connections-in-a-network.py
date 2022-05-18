#
# @lc app=leetcode id=1192 lang=python3
#
# [1192] Critical Connections in a Network
#
# https://leetcode.com/problems/critical-connections-in-a-network/description/
#
# algorithms
# Hard (51.74%)
# Likes:    3797
# Dislikes: 146
# Total Accepted:    152.1K
# Total Submissions: 289.5K
# Testcase Example:  '4\n[[0,1],[1,2],[2,0],[1,3]]'
#
# There are n servers numbered from 0 to n - 1 connected by undirected
# server-to-server connections forming a network where connections[i] = [ai,
# bi] represents a connection between servers ai and bi. Any server can reach
# other servers directly or indirectly through the network.
# 
# A critical connection is a connection that, if removed, will make some
# servers unable to reach some other server.
# 
# Return all critical connections in the network in any order.
# 
# 
# Example 1:
# 
# 
# Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
# Output: [[1,3]]
# Explanation: [[3,1]] is also accepted.
# 
# 
# Example 2:
# 
# 
# Input: n = 2, connections = [[0,1]]
# Output: [[0,1]]
# 
# 
# 
# Constraints:
# 
# 
# 2 <= n <= 10^5
# n - 1 <= connections.length <= 10^5
# 0 <= ai, bi <= n - 1
# ai != bi
# There are no repeated connections.
# 
# 
#

# @lc code=start
from collections import defaultdict

class Solution:
    def __init__(self):
        self.graph = defaultdict(set)
        self.res = []


    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        # create graph
        self.build_graph(connections)

        # create steps array
        self.steps = [-1] * n

        # dfs
        self.dfs(0, -1, 0)
        return self.res


    def dfs(self, node, parent, step):

        self.steps[node] = step + 1

        for child in self.graph[node]:
            
            if child == parent:
                continue

            elif self.steps[child] == -1:
                self.steps[node] = min(
                    self.steps[node],
                    self.dfs(child, node, step + 1)
                )

            else:
                self.steps[node] = min(
                    self.steps[node],
                    self.steps[child]
                )


        if self.steps[node] == step + 1 and node != 0:
            self.res.append([parent, node])

        return self.steps[node]


    def build_graph(self, connections):
        for u, v in connections:
            self.graph[u].add(v)
            self.graph[v].add(u)
# @lc code=end

