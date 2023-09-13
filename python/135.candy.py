#
# @lc app=leetcode id=135 lang=python3
#
# [135] Candy
#
# https://leetcode.com/problems/candy/description/
#
# algorithms
# Hard (34.93%)
# Likes:    1872
# Dislikes: 211
# Total Accepted:    175.1K
# Total Submissions: 501.3K
# Testcase Example:  '[1,0,2]'
#
# There are n children standing in a line. Each child is assigned a rating
# value given in the integer array ratings.
# 
# You are giving candies to these children subjected to the following
# requirements:
# 
# 
# Each child must have at least one candy.
# Children with a higher rating get more candies than their neighbors.
# 
# 
# Return the minimum number of candies you need to have to distribute the
# candies to the children.
# 
# 
# Example 1:
# 
# 
# Input: ratings = [1,0,2]
# Output: 5
# Explanation: You can allocate to the first, second and third child with 2, 1,
# 2 candies respectively.
# 
# 
# Example 2:
# 
# 
# Input: ratings = [1,2,2]
# Output: 4
# Explanation: You can allocate to the first, second and third child with 1, 2,
# 1 candies respectively.
# The third child gets 1 candy because it satisfies the above two
# conditions.
# 
# 
# 
# Constraints:
# 
# 
# n == ratings.length
# 1 <= n <= 2 * 10^4
# 0 <= ratings[i] <= 2 * 10^4
# 
# 
#

# References:
#   https://www.youtube.com/watch?v=QzPWc0ilEek&ab_channel=HuifengGuan

# @lc code=start
class Solution:
    def candy(self, ratings: List[int]) -> int:
        if not ratings or len(ratings) == 0:
            return 0

        n = len(ratings)
        candies = [1 for _ in range(n)]

        # greedy algorithm
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = max(1, candies[i - 1] + 1)

        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)

        return sum(candies)

from heapq import heappush, heappop

class Solution_Heap:
    def candy(self, ratings: List[int]) -> int:
        
        n = len(ratings)
        candies = [0 for _ in range(n)]

        heap = []
        for i in range(n):
            heappush(heap, (ratings[i], i))

        while heap:
            rate, idx = heappop(heap)
            candies[idx] += 1

            if idx == 0:
                if idx + 1 < n and rate > ratings[idx + 1]:
                    candies[idx] = candies[idx + 1] + 1
            elif idx == n - 1:
                if idx - 1 >= 0 and rate > ratings[idx - 1]:
                    candies[idx] = candies[idx - 1] + 1
            else:
                if rate > ratings[idx + 1] and rate > ratings[idx - 1]:
                    candies[idx] = max(candies[idx - 1], candies[idx + 1]) + 1
                elif rate > ratings[idx - 1]:
                    candies[idx] = candies[idx - 1] + 1
                elif rate > ratings[idx + 1]:
                    candies[idx] = candies[idx + 1] + 1

        return sum(candies)
# @lc code=end

