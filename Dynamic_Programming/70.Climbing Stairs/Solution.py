import sys

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1

        dp = [sys.maxint] * (n + 1)
        dp[1], dp[2] = 1, 2

        for i in xrange(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]
