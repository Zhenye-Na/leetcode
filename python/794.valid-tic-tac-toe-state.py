#
# @lc app=leetcode id=794 lang=python3
#
# [794] Valid Tic-Tac-Toe State
#
# https://leetcode.com/problems/valid-tic-tac-toe-state/description/
#
# algorithms
# Medium (34.94%)
# Likes:    550
# Dislikes: 1151
# Total Accepted:    59.6K
# Total Submissions: 171.6K
# Testcase Example:  '["O  ","   ","   "]'
#
# Given a Tic-Tac-Toe board as a string array board, return true if and only if
# it is possible to reach this board position during the course of a valid
# tic-tac-toe game.
#
# The board is a 3 x 3 array that consists of characters ' ', 'X', and 'O'. The
# ' ' character represents an empty square.
#
# Here are the rules of Tic-Tac-Toe:
#
#
# Players take turns placing characters into empty squares ' '.
# The first player always places 'X' characters, while the second player always
# places 'O' characters.
# 'X' and 'O' characters are always placed into empty squares, never filled
# ones.
# The game ends when there are three of the same (non-empty) character filling
# any row, column, or diagonal.
# The game also ends if all squares are non-empty.
# No more moves can be played if the game is over.
#
#
#
# Example 1:
#
#
# Input: board = ["O  ","   ","   "]
# Output: false
# Explanation: The first player always plays "X".
#
#
# Example 2:
#
#
# Input: board = ["XOX"," X ","   "]
# Output: false
# Explanation: Players take turns making moves.
#
#
# Example 3:
#
#
# Input: board = ["XOX","O O","XOX"]
# Output: true
#
#
#
# Constraints:
#
#
# board.length == 3
# board[i].length == 3
# board[i][j] is either 'X', 'O', or ' '.
#
#
#

# @lc code=start
from typing import List


class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        count_X = sum(row.count("X") for row in board)
        count_O = sum(row.count("O") for row in board)

        if not (count_X == count_O or count_X == count_O + 1):
            return False

        X_wins = self._is_winner(board, "X")
        O_wins = self._is_winner(board, "O")

        if X_wins and O_wins:
            return False

        if X_wins and count_X != count_O + 1:
            return False

        if O_wins and count_X != count_O:
            return False

        return True

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
