# Paint Fence

# Description

# There is a fence with n posts, each post can be painted with one of the k colors.
# You have to paint all the posts such that no more than two adjacent fence posts have the same color.
# Return the total number of ways you can paint the fence.

# n and k are non-negative integers.

# Example

# Example 1:
# Input: n=3, k=2  
# Output: 6
# Explanation:
#           post 1,   post 2, post 3
#     way1    0         0       1 
#     way2    0         1       0
#     way3    0         1       1
#     way4    1         0       0
#     way5    1         0       1
#     way6    1         1       0

# Example 2:
# Input: n=2, k=2  
# Output: 4
# Explanation:
#           post 1,   post 2
#     way1    0         0       
#     way2    0         1            
#     way3    1         0          
#     way4    1         1     


class Solution:
    """
    @param n: non-negative integer, n posts
    @param k: non-negative integer, k colors
    @return: an integer, the total number of ways
    """
    def numWays(self, n, k):
        # write your code here
        # initialization
        ways = [0 for _ in range(n)]
        ways[0], ways[1] = k, k * k
        for i in range(2, n):
            #         different from i-1 th + (same as i-1, which means different from i - 2)
            ways[i] = ways[i - 1] * (k - 1) + ways[i - 2] * (k - 1)

        return ways[-1]

