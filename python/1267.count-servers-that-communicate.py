#
# @lc app=leetcode id=1267 lang=python3
#
# [1267] Count Servers that Communicate
#
# https://leetcode.com/problems/count-servers-that-communicate/description/
#
# algorithms
# Medium (57.78%)
# Likes:    565
# Dislikes: 55
# Total Accepted:    30.2K
# Total Submissions: 52.4K
# Testcase Example:  '[[1,0],[0,1]]'
#
# You are given a map of a server center, represented as a m * n integer matrix
# grid, where 1 means that on that cell there is a server and 0 means that it
# is no server. Two servers are said to communicate if they are on the same row
# or on the same column.
# 
# Return the number of servers that communicate with any other server.
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: grid = [[1,0],[0,1]]
# Output: 0
# Explanation: No servers can communicate with others.
# 
# Example 2:
# 
# 
# 
# 
# Input: grid = [[1,0],[1,1]]
# Output: 3
# Explanation: All three servers can communicate with at least one other
# server.
# 
# 
# Example 3:
# 
# 
# 
# 
# Input: grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]
# Output: 4
# Explanation: The two servers in the first row can communicate with each
# other. The two servers in the third column can communicate with each other.
# The server at right bottom corner can't communicate with any other
# server.
# 
# 
# 
# Constraints:
# 
# 
# m == grid.length
# n == grid[i].length
# 1 <= m <= 250
# 1 <= n <= 250
# grid[i][j] == 0 or 1
# 
# 
#

# @lc code=start
class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        row = [0] * m
        col = [0] * n
        
        computers = []
        
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    computers.append((i,j))
                    row[i] += grid[i][j]
                    col[j] += grid[i][j]
                
        count = 0
        
        for i,j in computers:
            if row[i] > 1 or col[j] > 1:
                count +=1

        return count



from collections import deque

class Solution_BFS:
    def __init__(self):
        self.SERVER = 1
    
    def countServers(self, grid: List[List[int]]) -> int:
        if not grid or len(grid) == 0 or len(grid[0]) == 0:
            return 0
        
        m, n = len(grid), len(grid[0])
        seen = set([])
        queue = deque([])
        total_count = 0

        def bfs(x, y, seen):       
            queue.append((x, y))
            seen.add((x, y))
            group = []

            while queue:
                x, y = queue.popleft()
                group.append((x, y))

                # same row or same column
                for i in range(m):
                    if i != x and grid[i][y] == self.SERVER and (i, y) not in seen:
                        queue.append((i, y))
                        seen.add((i, y))

                for j in range(n):
                    if j != y and grid[x][j] == self.SERVER and (x, j) not in seen:
                        queue.append((x, j))
                        seen.add((x, j))

            return len(group)


        for i in range(m):
            for j in range(n):
                if grid[i][j] == self.SERVER and (i, j) not in seen:
                    curr_count = bfs(i, j, seen)
                    total_count += curr_count if curr_count > 1 else 0


        return total_count
# @lc code=end

