# [293] Flip Game

# Description

# You are playing the following Flip Game with your friend:
# Given a string that contains only two characters: `+` and `-`,
# you can flip two consecutive `"++"` into `"--"`, you can only flip one time.

# Please find all strings that can be obtained after one flip.

# Write a program to find all possible states of the string after one valid move.

# Example

# Example 1

# Input:  s = "++++"
# Output: 
# [
#   "--++",
#   "+--+",
#   "++--"
# ]


# Example 2

# Input: s = "---+++-+++-+"
# Output: 
# [
# 	"---+++-+---+",
# 	"---+++---+-+",
# 	"---+---+++-+",
# 	"-----+-+++-+"
# ]

class Solution:
    """
    @param s: the given string
    @return: all the possible states of the string after one valid move
    """
    def generatePossibleNextMoves(self, s):
        # write your code here
        if not s or len(s) < 2:
            return []

        res = []
        n = len(s)
        for i in range(n - 1):
            if s[i:i + 2] == "++":
                res.append(s[:i] + "--" + s[i + 2:])

        return res

