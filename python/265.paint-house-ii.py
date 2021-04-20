# Paint House II
# Description
# There are a row of n houses, each house can be painted with one of the k colors.
# The cost of painting each house with a certain color is different.

# You have to paint all the houses such that no two adjacent houses have the same color.

# The cost of painting each house with a certain color is represented
# by a n x k cost matrix. For example, costs[0][0] is the cost of painting
# house 0 with color 0; costs[1][2] is the cost of painting house 1 with color 2,
# and so on... Find the minimum cost to paint all houses.

# All costs are positive integers.

# Example

# Example 1

# Input:
# costs = [[14,2,11],[11,14,5],[14,3,10]]
# Output: 10
# Explanation:
# The three house use color [1,2,1] for each house. The total cost is 10.

# Example 2

# Input:
# costs = [[5]]
# Output: 5
# Explanation:
# There is only one color and one house.

# Challenge
# Could you solve it in O(nk)


# same as [1289] Minimum Falling Path Sum II
class Solution:
    """
    @param costs: n x k cost matrix
    @return: an integer, the minimum cost to paint all houses
    """
    def minCostII(self, costs):
        # write your code here
        if not costs or len(costs) == 0 or len(costs[0]) == 0:
            return 0

        n, k = len(costs), len(costs[0])

        states = [[0 for _ in range(k)] for _ in range(n)]
        for i in range(k):
            states[0][i] = costs[0][i]

        for j in range(1, n):

            # sort the temp array is overkill
            # we can just store the min_value and second_min_value with
            # their corresponding colors
            temp = []
            for l in range(k):
                temp.append([states[j - 1][l], l])
            temp.sort(key=lambda x: (x[0],                                                                                  x[1]))

            for c in range(k):
                # check if c is the same as the color of min_value
                if c == temp[0][1]:
                    states[j][c] = temp[1][0] + costs[j][c]
                else:
                    states[j][c] = temp[0][0] + costs[j][c]

        return min(states[-1])

