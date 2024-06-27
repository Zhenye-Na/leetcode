#
# @lc app=leetcode id=1791 lang=python3
#
# [1791] Find Center of Star Graph
#
# https://leetcode.com/problems/find-center-of-star-graph/description/
#
# algorithms
# Easy (83.49%)
# Likes:    1513
# Dislikes: 159
# Total Accepted:    226.2K
# Total Submissions: 266.7K
# Testcase Example:  '[[1,2],[2,3],[4,2]]'
#
# There is an undirected star graph consisting of n nodes labeled from 1 to n.
# A star graph is a graph where there is one center node and exactly n - 1
# edges that connect the center node with every other node.
# 
# You are given a 2D integer array edges where each edges[i] = [ui, vi]
# indicates that there is an edge between the nodes ui and vi. Return the
# center of the given star graph.
# 
# 
# Example 1:
# 
# 
# Input: edges = [[1,2],[2,3],[4,2]]
# Output: 2
# Explanation: As shown in the figure above, node 2 is connected to every other
# node, so 2 is the center.
# 
# 
# Example 2:
# 
# 
# Input: edges = [[1,2],[5,1],[1,3],[1,4]]
# Output: 1
# 
# 
# 
# Constraints:
# 
# 
# 3 <= n <= 10^5
# edges.length == n - 1
# edges[i].length == 2
# 1 <= ui, vi <= n
# ui != vi
# The given edges represent a valid star graph.
# 
# 
#

# @lc code=start
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        counter = defaultdict(int)
        for edge in edges:
            counter[edge[0]] += 1
            counter[edge[1]] += 1

        n = len(counter)
        for node in counter:
            if counter[node] == n - 1:
                return node

        return -1
# @lc code=end

