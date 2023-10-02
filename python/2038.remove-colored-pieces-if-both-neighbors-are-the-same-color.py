#
# @lc app=leetcode id=2038 lang=python3
#
# [2038] Remove Colored Pieces if Both Neighbors are the Same Color
#
# https://leetcode.com/problems/remove-colored-pieces-if-both-neighbors-are-the-same-color/description/
#
# algorithms
# Medium (61.18%)
# Likes:    739
# Dislikes: 67
# Total Accepted:    49K
# Total Submissions: 80.1K
# Testcase Example:  '"AAABABB"'
#
# There are n pieces arranged in a line, and each piece is colored either by
# 'A' or by 'B'. You are given a string colors of length n where colors[i] is
# the color of the i^th piece.
# 
# Alice and Bob are playing a game where they take alternating turns removing
# pieces from the line. In this game, Alice moves first.
# 
# 
# Alice is only allowed to remove a piece colored 'A' if both its neighbors are
# also colored 'A'. She is not allowed to remove pieces that are colored
# 'B'.
# Bob is only allowed to remove a piece colored 'B' if both its neighbors are
# also colored 'B'. He is not allowed to remove pieces that are colored
# 'A'.
# Alice and Bob cannot remove pieces from the edge of the line.
# If a player cannot make a move on their turn, that player loses and the other
# player wins.
# 
# 
# Assuming Alice and Bob play optimally, return true if Alice wins, or return
# false if Bob wins.
# 
# 
# Example 1:
# 
# 
# Input: colors = "AAABABB"
# Output: true
# Explanation:
# AAABABB -> AABABB
# Alice moves first.
# She removes the second 'A' from the left since that is the only 'A' whose
# neighbors are both 'A'.
# 
# Now it's Bob's turn.
# Bob cannot make a move on his turn since there are no 'B's whose neighbors
# are both 'B'.
# Thus, Alice wins, so return true.
# 
# 
# Example 2:
# 
# 
# Input: colors = "AA"
# Output: false
# Explanation:
# Alice has her turn first.
# There are only two 'A's and both are on the edge of the line, so she cannot
# move on her turn.
# Thus, Bob wins, so return false.
# 
# 
# Example 3:
# 
# 
# Input: colors = "ABBBBBBBAAA"
# Output: false
# Explanation:
# ABBBBBBBAAA -> ABBBBBBBAA
# Alice moves first.
# Her only option is to remove the second to last 'A' from the right.
# 
# ABBBBBBBAA -> ABBBBBBAA
# Next is Bob's turn.
# He has many options for which 'B' piece to remove. He can pick any.
# 
# On Alice's second turn, she has no more pieces that she can remove.
# Thus, Bob wins, so return false.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= colors.length <= 10^5
# colors consists of only the letters 'A' and 'B'
# 
# 
#

# @lc code=start
class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        if not colors or len(colors) < 3:
            return False

        counts = {}
        counts["A"] = 0
        counts["B"] = 0

        i, j  = 0, 0
        ptr = colors[0]
        while j < len(colors):
            while j < len(colors) and colors[j] == ptr:
                j += 1

            counts[ptr] += max(j - i - 2, 0)
            
            if j >= len(colors):
                break

            i = j
            ptr = colors[j]

        return counts["A"] - counts["B"] >= 1

# Greedy
#     3     4        3
# " AAAAA BBBBBB   AAAAA"
#  |0     5|       11 | 16


class Solution_TLE:
    def winnerOfGame(self, colors: str) -> bool:

        pattern = {}
        pattern[0] = "AAA"
        pattern[1] = "BBB"

        rounds = 0
        while True:
            if self.findPattern(colors, pattern[rounds % 2]):
                colors = colors.replace(pattern[rounds % 2], pattern[rounds % 2][:2], 1)
                rounds += 1
            else:
                break

        return rounds % 2 != 0

    def findPattern(self, colors, pattern):
        return pattern in colors

# minimize input string so that, there is no more AAA or BBB
# based on the number of moves -> determine who wins

# Brute Force
# Find AAA then turn to ABBBBBBBAA
# Find BBB then turn to ABBBBBBAA
# Find AAA then turn to ABBBBBBAA
# @lc code=end

