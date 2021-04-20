# Paint House

# Description

# There are a row of n houses, each house can be painted with one of the three colors:
# red, blue or green. The cost of painting each house with a certain color is different.
# You have to paint all the houses such that no two adjacent houses have the same color,
# and you need to cost the least. Return the minimum cost.

# The cost of painting each house with a certain color is represented by a n x 3 cost matrix.
# For example, costs[0][0] is the cost of painting house 0 with color red; costs[1][2] is the
# cost of painting house 1 with color green, and so on... Find the minimum cost to paint all
# houses.

# All costs are positive integers.

# Example

# Example 1:

# Input: [[14,2,11],[11,14,5],[14,3,10]]
# Output: 10
# Explanation: Paint house 0 into blue, paint house 1 into green, paint house 2 into blue.
# Minimum cost: 2 + 5 + 3 = 10.

# Example 2:

# Input: [[1,2,3],[1,4,6]]
# Output: 3

class Solution:
    """
    @param costs: n x 3 cost matrix
    @return: An integer, the minimum cost to paint all houses
    """
    def minCost(self, costs):
        # write your code here
        if not costs or len(costs) == 0 or len(costs[0]) == 0:
            return 0

        n = len(costs)
        f = [[0 for _ in range(3)] for _ in range(n)]
        f[0][0] = costs[0][0]
        f[0][1] = costs[0][1]
        f[0][2] = costs[0][2]

        for i in range(1, n):
            f[i][0] = min(f[i - 1][1], f[i - 1][2]) + costs[i][0]
            f[i][1] = min(f[i - 1][0], f[i - 1][2]) + costs[i][1]
            f[i][2] = min(f[i - 1][0], f[i - 1][1]) + costs[i][2]

        return min(f[-1])

