#
# @lc app=leetcode id=1275 lang=python3
#
# [1275] Find Winner on a Tic Tac Toe Game
#
# https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/description/
#
# algorithms
# Easy (54.12%)
# Likes:    1498
# Dislikes: 348
# Total Accepted:    131.3K
# Total Submissions: 243.4K
# Testcase Example:  '[[0,0],[2,0],[1,1],[2,1],[2,2]]'
#
# Tic-tac-toe is played by two players A and B on a 3 x 3 grid. The rules of
# Tic-Tac-Toe are:
#
#
# Players take turns placing characters into empty squares ' '.
# The first player A always places 'X' characters, while the second player B
# always places 'O' characters.
# 'X' and 'O' characters are always placed into empty squares, never on filled
# ones.
# The game ends when there are three of the same (non-empty) character filling
# any row, column, or diagonal.
# The game also ends if all squares are non-empty.
# No more moves can be played if the game is over.
#
#
# Given a 2D integer array moves where moves[i] = [rowi, coli] indicates that
# the i^th move will be played on grid[rowi][coli]. return the winner of the
# game if it exists (A or B). In case the game ends in a draw return "Draw". If
# there are still movements to play return "Pending".
#
# You can assume that moves is valid (i.e., it follows the rules of
# Tic-Tac-Toe), the grid is initially empty, and A will play first.
#
#
# Example 1:
#
#
# Input: moves = [[0,0],[2,0],[1,1],[2,1],[2,2]]
# Output: "A"
# Explanation: A wins, they always play first.
#
#
# Example 2:
#
#
# Input: moves = [[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]
# Output: "B"
# Explanation: B wins.
#
#
# Example 3:
#
#
# Input: moves = [[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]
# Output: "Draw"
# Explanation: The game ends in a draw since there are no moves to make.
#
#
#
# Constraints:
#
#
# 1 <= moves.length <= 9
# moves[i].length == 2
# 0 <= rowi, coli <= 2
# There are no repeated elements on moves.
# moves follow the rules of tic tac toe.
#
#
#


# @lc code=start
from typing import List


class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        board = self._draw_board(moves)
        A_wins = self._is_winner(board, "X")
        B_wins = self._is_winner(board, "O")

        if not A_wins and not B_wins:
            if len(moves) == 9:
                return "Draw"
            else:
                return "Pending"

        return "A" if A_wins else "B"

    def _draw_board(self, moves):
        board = [[" " for _ in range(3)] for _ in range(3)]
        for i, move in enumerate(moves):
            if i % 2 == 0:
                board[move[0]][move[1]] = "X"
            else:
                board[move[0]][move[1]] = "O"
        return board

    def _is_winner(self, board: List[str], player: str) -> bool:

        for i in range(3):
            if board[i][0] == board[i][1] == board[i][2] == player:
                return True
            if board[0][i] == board[1][i] == board[2][i] == player:
                return True

        if board[0][0] == board[1][1] == board[2][2] == player:
            return True

        if board[0][2] == board[1][1] == board[2][0] == player:
            return True

        return False


# @lc code=end
