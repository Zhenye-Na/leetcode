#
# @lc app=leetcode id=743 lang=python3
#
# [743] Network Delay Time
#
# https://leetcode.com/problems/network-delay-time/description/
#
# algorithms
# Medium (46.34%)
# Likes:    6828
# Dislikes: 340
# Total Accepted:    407.5K
# Total Submissions: 775.3K
# Testcase Example:  '[[2,1,1],[2,3,1],[3,4,1]]\n4\n2'
#
# You are given a network of n nodes, labeled from 1 to n. You are also given
# times, a list of travel times as directed edges times[i] = (ui, vi, wi),
# where ui is the source node, vi is the target node, and wi is the time it
# takes for a signal to travel from source to target.
# 
# We will send a signal from a given node k. Return the minimum time it takes
# for all the n nodes to receive the signal. If it is impossible for all the n
# nodes to receive the signal, return -1.
# 
# 
# Example 1:
# 
# 
# Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
# Output: 2
# 
# 
# Example 2:
# 
# 
# Input: times = [[1,2,1]], n = 2, k = 1
# Output: 1
# 
# 
# Example 3:
# 
# 
# Input: times = [[1,2,1]], n = 2, k = 2
# Output: -1
# 
# 
# 
# Constraints:
# 
# 
# 1 <= k <= n <= 100
# 1 <= times.length <= 6000
# times[i].length == 3
# 1 <= ui, vi <= n
# ui != vi
# 0 <= wi <= 100
# All the pairs (ui, vi) are unique. (i.e., no multiple edges.)
# 
# 
#

# @lc code=start
from collections import defaultdict, deque

class Solution:
    def networkDelayTime(self, times, n, k):
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        distances = {node: float('inf') for node in range(1, n + 1)}
        distances[k] = 0

        queue = deque([(k, 0)])

        while queue:
            node, time = queue.popleft()
            if time > distances[node]:
                continue
            for neighbor, weight in graph[node]:
                if time + weight < distances[neighbor]:
                    distances[neighbor] = time + weight
                    queue.append((neighbor, time + weight))

        max_time = max(distances.values())
        return max_time if max_time < float('inf') else -1
# @lc code=end

