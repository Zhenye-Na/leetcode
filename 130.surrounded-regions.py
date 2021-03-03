#
# @lc app=leetcode id=130 lang=python3
#
# [130] Surrounded Regions
#
# https://leetcode.com/problems/surrounded-regions/description/
#
# algorithms
# Medium (29.21%)
# Likes:    2538
# Dislikes: 750
# Total Accepted:    285.6K
# Total Submissions: 969.9K
# Testcase Example:  '[["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]'
#
# Given an m x n matrix board containing 'X' and 'O', capture all regions
# surrounded by 'X'.
# 
# A region is captured by flipping all 'O's into 'X's in that surrounded
# region.
# 
# 
# Example 1:
# 
# 
# Input: board =
# [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
# Output:
# [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
# Explanation: Surrounded regions should not be on the border, which means that
# any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is
# not on the border and it is not connected to an 'O' on the border will be
# flipped to 'X'. Two cells are connected if they are adjacent cells connected
# horizontally or vertically.
# 
# 
# Example 2:
# 
# 
# Input: board = [["X"]]
# Output: [["X"]]
# 
# 
# 
# Constraints:
# 
# 
# m == board.length
# n == board[i].length
# 1 <= m, n <= 200
# board[i][j] is 'X' or 'O'.
# 
# 
#

# @lc code=start
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        queue = collections.deque([])
        for r in range(len(board)):
            for c in range(len(board[0])):
                if (r in [0, len(board) - 1] or c in [0, len(board[0]) - 1]) and board[r][c] == "O":
                    queue.append((r, c))

        while queue:
            r, c = queue.popleft()
            if 0 <= r < len(board) and 0 <= c < len(board[0]) and board[r][c] == "O":
                board[r][c] = "D"
                queue.append((r - 1, c)); queue.append((r + 1, c))
                queue.append((r, c - 1)); queue.append((r, c + 1))
            
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "D":
                    board[r][c] = "O"
# @lc code=end

