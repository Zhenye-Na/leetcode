# [161] One Edit Distance

# Given two strings s and t, determine if they are both one edit distance apart.

# Note: 

# There are 3 possiblities to satisify one edit distance apart:

# Insert a character into s to get t
# Delete a character from s to get t
# Replace a character of s to get t

# Example 1:

# Input: s = "ab", t = "acb"
# Output: true
# Explanation: We can insert 'c' into s to get t.


# Example 2:

# Input: s = "cab", t = "ad"
# Output: false
# Explanation: We cannot get t from s by only one step.


# Example 3:

# Input: s = "1203", t = "1213"
# Output: true
# Explanation: We can replace '0' with '1' to get t.


# Time O(n)
# Space O(1)
class Solution:
    """
    @param s: a string
    @param t: a string
    @return: true if they are both one edit distance apart or false
    """
    def isOneEditDistance(self, s, t):
        # write your code here
        if not s or len(s) == 0:
            return len(t) == 1

        if not t or len(t) == 0:
            return len(s) == 1

        if abs(len(s) - len(t)) > 1:
            return False

        l1, l2 = len(s), len(t)
        if l1 == l2:
            return self.is_replace_one_edit(s, t)
        elif l1 > l2:
            return self.is_remove_one_edit(s, t)
        else:
            return self.is_remove_one_edit(t, s)


    def is_remove_one_edit(self, s, t):
        # len(s) > len(t)
        l1, l2 = len(s), len(t)
        edits = 1
        i, j = 0, 0
        while i < l1 and j < l2:

            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                i += 1
                edits -= 1

            if edits < 0:
                return False

        while i < l1:
            edits -= 1
            i += 1

        return edits == 0


    def is_replace_one_edit(self, s, t):
        l = len(s)
        edits = 1
        for i in range(l):
            if s[i] == t[i]:
                continue
            else:
                edits -= 1

            if edits < 0:
                return False

        return edits == 0


# Time O(n^2)
# Space O(n)
class Solution_DP:
    """
    @param s: a string
    @param t: a string
    @return: true if they are both one edit distance apart or false
    """
    def isOneEditDistance(self, s, t):
        # write your code here
        if not s or len(s) == 0:
            return len(t) == 1

        if not t or len(t) == 0:
            return len(s) == 1

        if abs(len(s) - len(t)) > 1:
            return False


        l1, l2 = len(s), len(t)
        s = "#" + s
        t = "#" + t

        # dp initialization
        # f[i][j] represents the edit distance from s[:j] to t[:j]
        f = [[0 for _ in range(l2 + 1)] for _ in range(2)]

        for j in range(l2 + 1):
            f[0][j] = j

        f[0][0] = 0

        for i in range(1, l1 + 1):
            f[i % 2][0] = i

            for j in range(1, l2 + 1):
                if s[i] == t[j]:
                    f[i % 2][j] = f[(i - 1) % 2][j - 1]
                else:
                    f[i % 2][j] = min(
                        f[(i - 1) % 2][j - 1] + 1,
                        f[(i - 1) % 2][j] + 1,
                        f[i % 2][j - 1] + 1
                    )

        return f[l1 % 2][l2] == 1
