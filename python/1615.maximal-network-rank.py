#
# @lc app=leetcode id=1615 lang=python3
#
# [1615] Maximal Network Rank
#
# https://leetcode.com/problems/maximal-network-rank/description/
#
# algorithms
# Medium (54.33%)
# Likes:    2133
# Dislikes: 323
# Total Accepted:    121K
# Total Submissions: 185.7K
# Testcase Example:  '4\n[[0,1],[0,3],[1,2],[1,3]]'
#
# There is an infrastructure of n cities with some number of roads connecting
# these cities. Each roads[i] = [ai, bi] indicates that there is a
# bidirectional road between cities ai and bi.
# 
# The network rank of two different cities is defined as the total number of
# directly connected roads to either city. If a road is directly connected to
# both cities, it is only counted once.
# 
# The maximal network rank of the infrastructure is the maximum network rank of
# all pairs of different cities.
# 
# Given the integer n and the array roads, return the maximal network rank of
# the entire infrastructure.
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: n = 4, roads = [[0,1],[0,3],[1,2],[1,3]]
# Output: 4
# Explanation: The network rank of cities 0 and 1 is 4 as there are 4 roads
# that are connected to either 0 or 1. The road between 0 and 1 is only counted
# once.
# 
# 
# Example 2:
# 
# 
# 
# 
# Input: n = 5, roads = [[0,1],[0,3],[1,2],[1,3],[2,3],[2,4]]
# Output: 5
# Explanation: There are 5 roads that are connected to cities 1 or 2.
# 
# 
# Example 3:
# 
# 
# Input: n = 8, roads = [[0,1],[1,2],[2,3],[2,4],[5,6],[5,7]]
# Output: 5
# Explanation: The network rank of 2 and 5 is 5. Notice that all the cities do
# not have to be connected.
# 
# 
# 
# Constraints:
# 
# 
# 2 <= n <= 100
# 0 <= roads.length <= n * (n - 1) / 2
# roads[i].length == 2
# 0 <= ai, bi <= n-1
# ai != bi
# Each pair of cities has at most one road connecting them.
# 
# 
#

# @lc code=start
class Solution:

    def __init__(self):
        self.in_degrees = defaultdict(int)

    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        self.is_connected = [[0 for _ in range(n)] for _ in range(n)]
        self.constructInDegrees(n, roads)
        max_rank = 0

        for i in range(1, n):
            for j in range(0, i):
                current_rank = self.in_degrees[i] + self.in_degrees[j]
                if self.is_connected[i][j] == 1:
                    current_rank -= 1

                max_rank = max(max_rank, current_rank)

        return max_rank

    def constructInDegrees(self, n, roads):
        for i in range(n):
            in_degree = 0
            for road in roads:
                if i in road:
                    in_degree += 1
                    self.is_connected[road[0]][road[1]] = 1
                    self.is_connected[road[1]][road[0]] = 1
            self.in_degrees[i] = in_degree


class SolutionTLE:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        max_rank = 0

        for i in range(1, n):
            for j in range(0, i):
                max_rank = max(max_rank, self.findNumsOfRoad(i, j, roads))

        return max_rank

    def findNumsOfRoad(self, point_a, point_b, roads):
        num_of_roads = 0

        for road in roads:
            if (road[0] == point_a and road[1] == point_b) or (road[1] == point_a and road[0] == point_b):
                num_of_roads += 1
                continue

            if road[0] == point_a or road[1] == point_a:
                num_of_roads += 1

            if road[0] == point_b or road[1] == point_b:
                num_of_roads += 1

        return num_of_roads
# @lc code=end

