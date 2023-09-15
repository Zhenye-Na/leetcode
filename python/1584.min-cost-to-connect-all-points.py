#
# @lc app=leetcode id=1584 lang=python3
#
# [1584] Min Cost to Connect All Points
#
# https://leetcode.com/problems/min-cost-to-connect-all-points/description/
#
# algorithms
# Medium (56.49%)
# Likes:    1548
# Dislikes: 51
# Total Accepted:    64.2K
# Total Submissions: 103.5K
# Testcase Example:  '[[0,0],[2,2],[3,10],[5,2],[7,0]]'
#
# You are given an array points representing integer coordinates of some points
# on a 2D-plane, where points[i] = [xi, yi].
# 
# The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan
# distance between them: |xi - xj| + |yi - yj|, where |val| denotes the
# absolute value of val.
# 
# Return the minimum cost to make all points connected. All points are
# connected if there is exactly one simple path between any two points.
# 
# 
# Example 1:
# 
# 
# Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
# Output: 20
# Explanation: 
# 
# We can connect the points as shown above to get the minimum cost of 20.
# Notice that there is a unique path between every pair of points.
# 
# 
# Example 2:
# 
# 
# Input: points = [[3,12],[-2,5],[-4,1]]
# Output: 18
# 
# 
# 
# Constraints:
# 
# 
# 1 <= points.length <= 1000
# -10^6 <= xi, yi <= 10^6
# All pairs (xi, yi) are distinct.
# 
# 
#

# @lc code=start
from heapq import heappush, heappop
from collections import defaultdict

class Solution:

    def __init__(self):
        self.visited = set()
        self.neighbors = defaultdict(list)

    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        self.constructNeighbors(points)

        heap = []
        heap.append((0, points[0]))

        min_cost = 0
        while heap:

            if len(self.visited) == len(points):
                return min_cost

            curr_cost, curr_point = heappop(heap)
            if tuple(curr_point) in self.visited:
                continue

            min_cost += curr_cost
            self.visited.add(tuple(curr_point))

            neighbors = self.neighbors[tuple(curr_point)]
            for n in neighbors:
                heappush(heap, n)

        return 0

    def constructNeighbors(self, points):
        for i in range(len(points)):
            for j in range(len(points)):
                if i != j:
                    cost = self.manhattan(points[i], points[j])
                    self.neighbors[tuple(points[i])].append((cost, points[j]))

    def manhattan(self, pointA, pointB):
        return abs(pointA[0] - pointB[0]) + abs(pointA[1] - pointB[1])


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        manhattan = lambda p1, p2: abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        n, c = len(points), collections.defaultdict(list)
        for i in range(n):
            for j in range(i + 1, n):
                d = manhattan(points[i], points[j])
                c[i].append((d, j))
                c[j].append((d, i))

        cnt, ans, visited, heap = 1, 0, [0] * n, c[0]
        visited[0] = 1
        heapq.heapify(heap)

        while heap:
            d, j = heapq.heappop(heap)
            if not visited[j]:
                visited[j], cnt, ans = 1, cnt + 1, ans + d
                for record in c[j]: heapq.heappush(heap, record)
            if cnt >= n: break        
        return ans
# @lc code=end

