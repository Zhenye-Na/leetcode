#
# @lc app=leetcode id=1091 lang=python3
#
# [1091] Shortest Path in Binary Matrix
#
# https://leetcode.com/problems/shortest-path-in-binary-matrix/description/
#
# algorithms
# Medium (40.73%)
# Likes:    2707
# Dislikes: 131
# Total Accepted:    193.4K
# Total Submissions: 448.8K
# Testcase Example:  '[[0,1],[1,0]]'
#
# Given an n x n binary matrix grid, return the length of the shortest clear
# path in the matrix. If there is no clear path, return -1.
# 
# A clear path in a binary matrix is a path from the top-left cell (i.e., (0,
# 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:
# 
# 
# All the visited cells of the path are 0.
# All the adjacent cells of the path are 8-directionally connected (i.e., they
# are different and they share an edge or a corner).
# 
# 
# The length of a clear path is the number of visited cells of this path.
# 
# 
# Example 1:
# 
# 
# Input: grid = [[0,1],[1,0]]
# Output: 2
# 
# 
# Example 2:
# 
# 
# Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
# Output: 4
# 
# 
# Example 3:
# 
# 
# Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
# Output: -1
# 
# 
# 
# Constraints:
# 
# 
# n == grid.length
# n == grid[i].length
# 1 <= n <= 100
# grid[i][j] is 0 or 1
# 
# 
#

# @lc code=start
from collections import deque

# BFS

class Solution_BFS:
    
    def __init__(self):
        self.EMPTY = 0
        self.BLOCK = 1
        self.DIRECTIONS = [[-1, -1], [-1, 1], [1, -1], [1, 1], [0, 1], [0, -1], [1, 0], [-1, 0]]

    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if not grid or len(grid) == 0 or len(grid[0]) == 0 or grid[0][0] != self.EMPTY or grid[len(grid) - 1][len(grid[0]) - 1] != self.EMPTY:
            return -1

        if len(grid) == 1 and len(grid[0]) == 1:
            return 1

        m, n = len(grid), len(grid[0])
        step = 1
        queue = deque([(0, 0)])
        visited = set([(0, 0)])

        while queue:
            step += 1
            size = len(queue)
            for _ in range(size):
                x, y = queue.popleft()
                for d in self.DIRECTIONS:
                    x_, y_ = x + d[0], y + d[1]
                    if self._inBound(x_, y_, m, n, grid, visited):
                        if x_ == m - 1 and y_ == n - 1:
                            return step
                        queue.append((x_, y_))
                        visited.add((x_, y_))

        return -1

    def _inBound(self, x, y, m, n, grid, visited):
        return 0 <= x < m and  0 <= y < n and grid[x][y] == self.EMPTY and (x, y) not in visited


# A* Search
# Dont compute the solution path

# Reference
# https://leetcode.com/problems/shortest-path-in-binary-matrix/discuss/313347/A*-search-in-Python

class Solution:
    def shortestPathBinaryMatrix(self, grid):
        n = len(grid)
        if n == 0 or grid[0][0] == 1:
            return -1
        target = (n - 1, n - 1)
        f0 = 2 * n - 2  # score of the source node, it is not important at all
        scores = {(0, 0): f0}
        # heap contains (f, g, row-ind, col-in)
        heap = [(f0, 1, 0, 0)]
        while heap:
            f, g, i, j = heappop(heap)
            if (i, j) == target:
                return g
            if scores[(i, j)] < f:  # Lazy removal
                continue
            children = [
                (i + 1, j),
                (i - 1, j),
                (i, j + 1),
                (i, j - 1),
                (i + 1, j + 1),
                (i - 1, j - 1),
                (i + 1, j - 1),
                (i - 1, j + 1),
            ]
            for k, l in children:
                if not (0 <= k < n and 0 <= l < n and grid[k][l] == 0):
                    continue
                heuristic = max(abs(k - target[0]), abs(l - target[1]))
                new_score = heuristic + g + 1
                if new_score < scores.get((k, l), float("inf")):
                    scores[(k, l)] = new_score
                    heappush(heap, (new_score, g + 1, k, l))
        return -1



# A* Search
# Print out the path

from heapq import heappush, heappop

class PriorityQueue:

    def __init__(self, iterable=[]):
        self.heap = []
        for value in iterable:
            heappush(self.heap, (0, value))

    def add(self, value, priority=0):
        heappush(self.heap, (priority, value))

    def pop(self):
        priority, value = heappop(self.heap)
        return value

    def __len__(self):
        return len(self.heap)


class Solution:
    def shortestPathBinaryMatrix(self, grid):
        shortest_path = a_star_graph_search(
            start              = (0, 0), 
            goal_function      = get_goal_function(grid),
            successor_function = get_successor_function(grid),
            heuristic          = get_heuristic(grid)
        )
        if shortest_path is None or grid[0][0] == 1:
            return -1
        else:
            return len(shortest_path)

def a_star_graph_search(
            start,
            goal_function,
            successor_function,
            heuristic
	):
    visited = set()
    came_from = dict()
    distance = {start: 0}
    frontier = PriorityQueue()
    frontier.add(start)
    while frontier:
        node = frontier.pop()
        if node in visited:
            continue
        if goal_function(node):
            return reconstruct_path(came_from, start, node)
        visited.add(node)
        for successor in successor_function(node):
            frontier.add(
                successor,
                priority = distance[node] + 1 + heuristic(successor)
            )
            if (successor not in distance
                or distance[node] + 1 < distance[successor]):
                distance[successor] = distance[node] + 1
                came_from[successor] = node
    return None

def reconstruct_path(came_from, start, end):
    """
    >>> came_from = {'b': 'a', 'c': 'a', 'd': 'c', 'e': 'd', 'f': 'd'}
    >>> reconstruct_path(came_from, 'a', 'e')
    ['a', 'c', 'd', 'e']
    """
    reverse_path = [end]
    while end != start:
        end = came_from[end]
        reverse_path.append(end)
    return list(reversed(reverse_path))


def get_goal_function(grid):
    """
    >>> f = get_goal_function([[0, 0], [0, 0]])
    >>> f((0, 0))
    False
    >>> f((0, 1))
    False
    >>> f((1, 1))
    True
    """
    M = len(grid)
    N = len(grid[0])
    def is_bottom_right(cell):
        return cell == (M-1, N-1)
    return is_bottom_right


def get_successor_function(grid):
    """
    >>> f = get_successor_function([[0, 0, 0], [0, 1, 0], [1, 0, 0]])
    >>> sorted(f((1, 2)))
    [(0, 1), (0, 2), (2, 1), (2, 2)]
    >>> sorted(f((2, 1)))
    [(1, 0), (1, 2), (2, 2)]
    """
    def get_clear_adjacent_cells(cell):
        i, j = cell
        return (
            (i + a, j + b)
            for a in (-1, 0, 1)
            for b in (-1, 0, 1)
            if a != 0 or b != 0
            if 0 <= i + a < len(grid)
            if 0 <= j + b < len(grid[0])
            if grid[i + a][j + b] == 0
        )
    return get_clear_adjacent_cells

def get_heuristic(grid):
    """
    >>> f = get_heuristic([[0, 0], [0, 0]])
    >>> f((0, 0))
    1
    >>> f((0, 1))
    1
    >>> f((1, 1))
    0
    """
    M, N = len(grid), len(grid[0])
    (a, b) = goal_cell = (M - 1, N - 1)
    def get_clear_path_distance_from_goal(cell):
        (i, j) = cell
        return max(abs(a - i), abs(b - j))
    return get_clear_path_distance_from_goal
# @lc code=end

