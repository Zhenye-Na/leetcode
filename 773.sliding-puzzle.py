#
# @lc app=leetcode id=773 lang=python3
#
# [773] Sliding Puzzle
#
# https://leetcode.com/problems/sliding-puzzle/description/
#
# algorithms
# Hard (60.61%)
# Likes:    898
# Dislikes: 30
# Total Accepted:    50K
# Total Submissions: 82.1K
# Testcase Example:  '[[1,2,3],[4,0,5]]'
#
# On a 2x3 board, there are 5 tiles represented by the integers 1 through 5,
# and an empty square represented by 0.
# 
# A move consists of choosing 0 and a 4-directionally adjacent number and
# swapping it.
# 
# The state of the board is solved if and only if the board is
# [[1,2,3],[4,5,0]].
# 
# Given a puzzle board, return the least number of moves required so that the
# state of the board is solved. If it is impossible for the state of the board
# to be solved, return -1.
# 
# Examples:
# 
# 
# Input: board = [[1,2,3],[4,0,5]]
# Output: 1
# Explanation: Swap the 0 and the 5 in one move.
# 
# 
# 
# Input: board = [[1,2,3],[5,4,0]]
# Output: -1
# Explanation: No number of moves will make the board solved.
# 
# 
# 
# Input: board = [[4,1,2],[5,0,3]]
# Output: 5
# Explanation: 5 is the smallest number of moves that solves the board.
# An example path:
# After move 0: [[4,1,2],[5,0,3]]
# After move 1: [[4,1,2],[0,5,3]]
# After move 2: [[0,1,2],[4,5,3]]
# After move 3: [[1,0,2],[4,5,3]]
# After move 4: [[1,2,0],[4,5,3]]
# After move 5: [[1,2,3],[4,5,0]]
# 
# 
# 
# Input: board = [[3,2,4],[1,5,0]]
# Output: 14
# 
# 
# Note:
# 
# 
# board will be a 2 x 3 array as described above.
# board[i][j] will be a permutation of [0, 1, 2, 3, 4, 5].
# 
# 
#

# @lc code=start
from collections import deque

class Solution:
    def __init__(self):
        self.directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]


    def slidingPuzzle(self, board: List[List[int]]) -> int:
        if not board or len(board) != 2 or len(board[0]) != 3:
            return -1

        m, n = len(board), len(board[0])
        state = "".join([str(e) for row in board for e in row])
        queue = deque([state])
        history = set([state])
        steps = 0
        final_state = "123450"

        while queue:
            size = len(queue)

            for _ in range(size):
                curr_state = queue.popleft()
                if curr_state == final_state:
                    return steps
                zero_idx = curr_state.index("0")
                x, y = zero_idx // n, zero_idx % n

                for d in self.directions:
                    pos_x, pos_y = x + d[0], y + d[1]
                    if 0 <= pos_x < m and 0 <= pos_y < n:
                        new_position = pos_x * n + pos_y
                        curr_state_lst = [i for i in curr_state]
                        curr_state_lst[zero_idx] = curr_state_lst[new_position]
                        curr_state_lst[new_position] = "0"
                        next_state = "".join(curr_state_lst[:])
                        if next_state not in history:
                            history.add(next_state)
                            queue.append(next_state)

            steps += 1

        return -1


# @lc code=end

# resources
#   https://www.lintcode.com/discuss/2760/ : this blog covers several methods and optimizations, very amazing

