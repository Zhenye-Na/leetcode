#
# @lc app=leetcode id=1192 lang=python3
#
# [1192] Critical Connections in a Network
#
# https://leetcode.com/problems/critical-connections-in-a-network/description/
#
# algorithms
# Hard (49.95%)
# Likes:    2317
# Dislikes: 119
# Total Accepted:    108.2K
# Total Submissions: 212.7K
# Testcase Example:  '4\n[[0,1],[1,2],[2,0],[1,3]]'
#
# There are n servers numbered from 0 to n-1 connected by undirected
# server-to-server connections forming a network where connections[i] = [a, b]
# represents a connection between servers a and b. Any server can reach any
# other server directly or indirectly through the network.
# 
# A critical connection is a connection that, if removed, will make some server
# unable to reach some other server.
# 
# Return all critical connections in the network in any order.
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
# Output: [[1,3]]
# Explanation: [[3,1]] is also accepted.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 10^5
# n-1 <= connections.length <= 10^5
# connections[i][0] != connections[i][1]
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
        self.steps = [-1] * len(connections)

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

