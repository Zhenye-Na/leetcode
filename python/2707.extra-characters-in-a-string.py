#
# @lc app=leetcode id=2707 lang=python3
#
# [2707] Extra Characters in a String
#
# @lc code=start
class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:

        dictionary = set(dictionary)
        s = "#" + s
        dp = [len(s) for _ in range(len(s))]
        dp[0] = 0

        for i in range(1, len(s)):
            for j in range(0, i):

                if s[j + 1: i + 1] in dictionary:
                    dp[i] = min(dp[i], dp[j])
                else:
                    dp[i] = min(dp[i], dp[j] + i - j)

        return dp[-1]
# @lc code=end
