# Minimum Window Subsequence

# Description
# Given strings S and T, find the minimum (contiguous) substring W of S,
# so that T is a subsequence of W.

# If there is no such window in S that covers all characters in T, return
# the empty string "". If there are multiple such minimum-length windows,
# return the one with the smallest starting index.

# All the strings in the input will only contain lowercase letters.
# The length of S will be in the range [1, 20000].
# The length of T will be in the range [1, 100].

# Example

# Example 1:
# Input：S="jmeqksfrsdcmsiwvaovztaqenprpvnbstl"，T="u"
# Output：""
# Explanation： unable to match

# Example 2:
# Input：S = "abcdebdde"， T = "bde"
# Output："bcde"
# Explanation："bcde" is the answer and "deb" is not a smaller window because
# the elements of T in the window must occur in order.


# Dynamic Programming
#   Time O(n^2)
#   Space O(n^2)
class Solution:
    """
    @param S: a string
    @param T: a string
    @return: the minimum substring of S
    """
    def minWindow(self, S, T):
        # Write your code here
        if not S or not T or len(S) == 0 or len(T) == 0:
            return ""

        l1, l2 = len(S), len(T)
        S = "#" + S
        T = "#" + T

        # dp initialization
        # f[i][j] represents the MWString (W) of s[:i] ending with S[i], T[:j] is the subsequence of W
        f = [[0 for _ in range(l2 + 1)] for _ in range(l1 + 1)]

        for j in range(1, l2 + 1):
            f[0][j] = l1 + 1

        for i in range(1, l1 + 1):
            for j in range(1, l2 + 1):
                if S[i] == T[j]:
                    f[i][j] = f[i - 1][j - 1] + 1 # 1 means s[i] or t[j]
                else:
                    f[i][j] = f[i - 1][j] + 1 # we hope MWS of s[:i - 1] may contains t[j], +1 means include s[i]

        min_len, end_idx = l1 + 1, -1
        for i in range(1, l1 + 1):
            if f[i][l2] < min_len:
                min_len = f[i][l2]
                end_idx = i

        if end_idx == -1:
            return ""
        else:
            return S[end_idx - min_len + 1:end_idx + 1]


# Rolling Array Optimization
#   Time O(n^2)
#   Space O(n)

class Solution:
    """
    @param S: a string
    @param T: a string
    @return: the minimum substring of S
    """
    def minWindow(self, S, T):
        # Write your code here
        if not S or not T or len(S) == 0 or len(T) == 0:
            return ""

        l1, l2 = len(S), len(T)
        S = "#" + S
        T = "#" + T

        # dp initialization
        # f[i][j] represents the MWString (W) of s[:i] ending with S[i], T[:j] is the subsequence of W
        f = [[0 for _ in range(l2 + 1)] for _ in range(2)]

        for j in range(1, l2 + 1):
            f[0][j] = l1 + 1

        min_len, end_idx = l1, -1
        for i in range(1, l1 + 1):
            # print(min_len)
            for j in range(1, l2 + 1):

                if S[i] == T[j]:
                    f[i % 2][j] = f[(i - 1) % 2][j - 1] + 1 # 1 means s[i] or t[j]
                else:
                    f[i % 2][j] = f[(i - 1) % 2][j] + 1 # we hope MWS of s[:i - 1] may contains t[j], +1 means include s[i]

            if f[i % 2][l2] < min_len:
                min_len = f[i % 2][l2]
                end_idx = i

        if end_idx == -1:
            return ""
        else:
            return S[end_idx - min_len + 1:end_idx + 1]

