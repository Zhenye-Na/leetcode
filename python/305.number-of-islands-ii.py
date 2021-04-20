# [305] Number of Islands II
#
# A 2d grid map of m rows and n columns is initially filled with water.
# We may perform an addLand operation which turns the water at position
# (row, col) into a land. Given a list of positions to operate, count
# the number of islands after each addLand operation. 
#
# An island is surrounded by water and is formed by connecting adjacent
# lands horizontally or vertically.
#
# You may assume all four edges of the grid are all surrounded by water.
#
# Example:
#
# Given m = 3, n = 3, positions = [[0,0], [0,1], [1,2], [2,1]].
# Initially, the 2d grid grid is filled with water.
#
# (Assume 0 represents water and 1 represents land).

# ```
# 0 0 0 
# 0 0 0
# 0 0 0
# ```

# Operation #1: addLand(0, 0) turns the water at grid[0][0] into a land.

# ```
# 1 0 0
# 0 0 0   Number of islands = 1
# 0 0 0
# ```

# Operation #2: addLand(0, 1) turns the water at grid[0][1] into a land.

# ```
# 1 1 0
# 0 0 0   Number of islands = 1
# 0 0 0
# ```

# Operation #3: addLand(1, 2) turns the water at grid[1][2] into a land.

# ```
# 1 1 0
# 0 0 1   Number of islands = 2
# 0 0 0
# ```

# Operation #4: addLand(2, 1) turns the water at grid[2][1] into a land.

# ```
# 1 1 0
# 0 0 1   Number of islands = 3
# 0 1 0
# ```

# We return the result as an array: [1, 1, 2, 3]

"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""
class UnionFind:
    def __init__(self):
        self.parent = {}
        self.count = 0


    def _find(self, cordinate):
        path = []
        while cordinate != self.parent[cordinate]:
            path.append(cordinate)
            cordinate = self.parent[cordinate]

        for node in path:
            self.parent[node] = cordinate

        return cordinate


    def union(self, pointA, pointB):
        pA = self._find(pointA)
        pB = self._find(pointB)
        if pA != pB:
            self.parent[pA] = pB
            self.count -= 1

    @property
    def count(self):
        return self._count


    @count.setter
    def count(self, value):
        self._count = value

class Solution:
    """
    @param n: An integer
    @param m: An integer
    @param operators: an array of point
    @return: an integer array
    """
    def __init__(self):
        self.DIRECTIONS = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    def numIslands2(self, n, m, operators):
        # write your code here
        solver = UnionFind()

        results = []
        islands = set([])

        for point in operators:
            x, y = point.x, point.y

            if (x, y) in islands:
                results.append(solver.count)
                continue

            islands.add((x, y))
            solver.parent[(x, y)] = (x, y)
            solver.count += 1

            for dx, dy in self.DIRECTIONS:
                neighbor_x, neighbor_y = x + dx, y + dy 
                if (neighbor_x, neighbor_y) in islands:
                    solver.union((x, y), (neighbor_x, neighbor_y))

            results.append(solver.count)

        return results




# reference, @property in python
#   https://www.programiz.com/python-programming/property
#   https://stackoverflow.com/questions/57066724/increment-class-property-attribute-in-setter
