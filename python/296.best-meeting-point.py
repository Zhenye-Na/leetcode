# [296] Best Meeting Point

# A group of two or more people wants to meet and minimize the total travel distance.

# You are given a 2D grid of values 0 or 1, where each 1 marks the home of someone in the group.

# The distance is calculated using Manhattan Distance, where distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|.

# Example:

# Input: 

# 1 - 0 - 0 - 0 - 1
# |   |   |   |   |
# 0 - 0 - 0 - 0 - 0
# |   |   |   |   |
# 0 - 0 - 1 - 0 - 0

# Output: 6 

# Explanation: Given three people living at (0,0), (0,4), and (2,2):
#              The point (0,2) is an ideal meeting point, as the total travel distance 
#              of 2+2+2=6 is minimal. So return 6.


# Math
class Solution:
    """
    @param grid: a 2D grid
    @return: the minimize travel distance
    """
    def minTotalDistance(self, grid):
        x, y = [], []

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    x.append(i)
                    y.append(j)

        x.sort()
        y.sort()

        px, py = x[len(x) // 2], y[len(y) // 2]
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    res += (abs(i - px) + abs(j - py))

        return res



# BFS O(n^3)
from collections import deque

class Solution:
    """
    @param grid: a 2D grid
    @return: the minimize travel distance
    """
    def __init__(self):
        self.dx = [0, 0, 1, -1]
        self.dy = [1, -1, 0, 0]

    def minTotalDistance(self, grid):
        # Write your code here
        # BFS on people
        self.PEOPLE = 1
        self.EMPTY = 0
        self.m, self.n = len(grid), len(grid[0])
        self.distance = [[0 for _ in range(self.n)] for _ in range(self.m)]

        ppl = []

        for i in range(self.m):
            for j in range(self.n):
                if board[i][j] == self.PEOPLE:
                    ppl.append((i, j))

        for x, y in ppl:
            self.bfs(x, y, board)

        min_distance = self.m + self.n + 2
        for i in range(self.m):
            for j in range(self.n):
                if board[i][j] == self.EMPTY:
                    min_distance = min(min_distance, self.distance[i][j])

        return min_distance


    def bfs(self, x, y, board)
        queue = deque([(x, y)])
        seen = set([(x, y)])

        d = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                x, y = queue.popleft()

                # update distance
                self.distance[x][y] += d

                for i in range(4):
                    next_x, next_y = x + self.dx[i], y + self.dy[i]
                    if self.is_valid(next_x, next_y, board, seen):
                        queue.append((next_x, next_y))
                        seen.add((next_x, next_y))

            d += 1

    
    def is_valid(self, x, y, board, seen):
        return 0 <= x < self.m and 0 <= y < self.n and board[x][y] == self.EMPTY and (x, y) not in seen


