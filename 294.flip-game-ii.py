# [294] Flip Game II

# Description

# You are playing the following Flip Game with your friend:
# Given a string that contains only these two characters: + and -,
# you and your friend take turns to flip two consecutive "++" into "--".

# The game ends when a person can no longer make a move and therefore the other person will be the winner.

# Write a function to determine if the starting player can guarantee a win.

# Example

# Example 1

# Input:  s = "++++"
# Output: true
# Explanation:
# The starting player can guarantee a win by flipping the middle "++" to become "+--+".

# Example 2

# Input: s = "+++++"
# Output: false 
# Explanation:
# The starting player can not win 
# "+++--" --> "+----"
# "++--+" --> "----+"

# Challenge

# Derive your algorithm's runtime complexity.

class Solution:
    """
    @param s: the given string
    @return: if the starting player can guarantee a win
    """
    def canWin(self, s):
        n = len(s)
        for i in range(n - 1):
            if s[i:(i + 1) + 1] == "++":
                if not self.canWin(s[:i] + "--" + s[i + 2:]):
                    return True

        return False
