# Factor Combinations
# Description
# Numbers can be regarded as product of its factors. For example,

# 8 = 2 x 2 x 2;
#   = 2 x 4.
# Write a function that takes an integer n and return all possible combinations of its factors.

# You may assume that n is always positive.
# Factors should be greater than 1 and less than n.

# Example
# Example1

# Input: 12
# Output: 
# [
#   [2, 6],
#   [2, 2, 3],
#   [3, 4]
# ]
# Explanation:
# 2*6 = 12
# 2*2*3 = 12
# 3*4 = 12
# Example2

# Input: 32
# Output: 
# [
#   [2, 16],
#   [2, 2, 8],
#   [2, 2, 2, 4],
#   [2, 2, 2, 2, 2],
#   [2, 4, 4],
#   [4, 8]
# ]
# Explanation:
# 2*16=32
# 2*2*8=32
# 2*2*2*4=32
# 2*2*2*2*2=32
# 2*4*4=32
# 4*8=32

class Solution:
    """
    @param n: a integer
    @return: return a 2D array
    """
    def getFactors(self, n):
        # write your code here
        self.res = []
        self._dfs(n, 2, [])
        return self.res

    def _dfs(self, n, start, curr):
        if n <= 1 and len(curr) > 1:
            self.res.append(curr[:])
            return
        
        if n < start:
            return

        # pruning
        factors = [*range(start, int(math.sqrt(n)) + 1)] + [n]
        for i in factors:
            if n % i == 0:
                curr.append(i)
                self._dfs(n // i, i, curr)
                curr.pop()

