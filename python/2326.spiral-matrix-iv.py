#
# @lc app=leetcode id=2326 lang=python3
#
# [2326] Spiral Matrix IV
#
# https://leetcode.com/problems/spiral-matrix-iv/description/
#
# algorithms
# Medium (75.18%)
# Likes:    1180
# Dislikes: 49
# Total Accepted:    150.8K
# Total Submissions: 182.8K
# Testcase Example:  '3\n5\n[3,0,2,6,8,1,7,9,4,2,5,5,0]'
#
# You are given two integers m and n, which represent the dimensions of a
# matrix.
#
# You are also given the head of a linked list of integers.
#
# Generate an m x n matrix that contains the integers in the linked list
# presented in spiral order (clockwise), starting from the top-left of the
# matrix. If there are remaining empty spaces, fill them with -1.
#
# Return the generated matrix.
#
#
# Example 1:
#
#
# Input: m = 3, n = 5, head = [3,0,2,6,8,1,7,9,4,2,5,5,0]
# Output: [[3,0,2,6,8],[5,0,-1,-1,1],[5,2,4,9,7]]
# Explanation: The diagram above shows how the values are printed in the
# matrix.
# Note that the remaining spaces in the matrix are filled with -1.
#
#
# Example 2:
#
#
# Input: m = 1, n = 4, head = [0,1,2]
# Output: [[0,1,2,-1]]
# Explanation: The diagram above shows how the values are printed from left to
# right in the matrix.
# The last space in the matrix is set to -1.
#
#
# Constraints:
#
#
# 1 <= m, n <= 10^5
# 1 <= m * n <= 10^5
# The number of nodes in the list is in the range [1, m * n].
# 0 <= Node.val <= 1000
#
#
#


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self):
        #                  Right,   Down,     Left,    Up
        self.directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        res = [[-1 for _ in range(n)] for _ in range(m)]
        visited = [[False for _ in range(n)] for _ in range(m)]

        current_direction = 0
        row, col = 0, 0

        while head:
            res[row][col] = head.val
            visited[row][col] = True
            head = head.next

            next_row = row + self.directions[current_direction][0]
            next_col = col + self.directions[current_direction][1]

            if (
                0 <= next_row < m
                and 0 <= next_col < n
                and not visited[next_row][next_col]
            ):
                row, col = next_row, next_col
            else:
                current_direction = (current_direction + 1) % 4
                row += self.directions[current_direction][0]
                col += self.directions[current_direction][1]

        return res


# @lc code=end
