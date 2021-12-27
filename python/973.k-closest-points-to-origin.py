#
# @lc app=leetcode id=973 lang=python3
#
# [973] K Closest Points to Origin
#
# https://leetcode.com/problems/k-closest-points-to-origin/description/
#
# algorithms
# Medium (61.19%)
# Likes:    772
# Dislikes: 72
# Total Accepted:    124.4K
# Total Submissions: 203.2K
# Testcase Example:  '[[1,3],[-2,2]]\n1'
#
# We have a list of points on the plane.  Find the K closest points to the
# origin (0, 0).
# 
# (Here, the distance between two points on a plane is the Euclidean
# distance.)
# 
# You may return the answer in any order.  The answer is guaranteed to be
# unique (except for the order that it is in.)
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: points = [[1,3],[-2,2]], K = 1
# Output: [[-2,2]]
# Explanation: 
# The distance between (1, 3) and the origin is sqrt(10).
# The distance between (-2, 2) and the origin is sqrt(8).
# Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
# We only want the closest K = 1 points from the origin, so the answer is just
# [[-2,2]].
# 
# 
# 
# Example 2:
# 
# 
# Input: points = [[3,3],[5,-1],[-2,4]], K = 2
# Output: [[3,3],[-2,4]]
# (The answer [[-2,4],[3,3]] would also be accepted.)
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= K <= points.length <= 10000
# -10000 < points[i][0] < 10000
# -10000 < points[i][1] < 10000
# 
# 
# 
#

# @lc code=start
from heapq import heappush, heappop, heapreplace

class Solution:
    def _compute_dist(self, point):
        return point[0] ** 2 + point[1] ** 2


    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if not points or len(points) == 0 or k <= 0:
            return []

        heap = []
        for point in points:

            dist = self._compute_dist(point)
            if len(heap) < k:
                heappush(heap, (-dist, point))
            else:
                if dist < -heap[0][0]:
                    heapreplace(heap, (-dist, point))

        return [p for _, p in heap]


    def kClosest2(self, points: List[List[int]], K: int) -> List[List[int]]:
        if not points or len(points) <= K:
            return points

        results, origin = [], [0, 0]
        for point in points:
            distance = self.computerDistance(origin, point)
            if len(results) < K:
                heappush(results, (- distance, point))
            else:
                if distance < - results[0][0]:
                    heappop(results)
                    heappush(results, (- distance, point))

        return [result[1] for result in results]

    def computerDistance(self, pointA, pointB):
        return (pointA[0] - pointB[0]) ** 2 + (pointA[1] - pointB[1]) ** 2
# @lc code=end

