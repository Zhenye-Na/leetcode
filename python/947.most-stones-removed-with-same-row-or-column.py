#
# @lc app=leetcode id=947 lang=python3
#
# [947] Most Stones Removed with Same Row or Column
#
# https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/description/
#
# algorithms
# Medium (58.88%)
# Likes:    5429
# Dislikes: 649
# Total Accepted:    225.3K
# Total Submissions: 381.6K
# Testcase Example:  '[[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]'
#
# On a 2D plane, we place n stones at some integer coordinate points. Each
# coordinate point may have at most one stone.
#
# A stone can be removed if it shares either the same row or the same column as
# another stone that has not been removed.
#
# Given an array stones of length n where stones[i] = [xi, yi] represents the
# location of the i^th stone, return the largest possible number of stones that
# can be removed.
#
#
# Example 1:
#
#
# Input: stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
# Output: 5
# Explanation: One way to remove 5 stones is as follows:
# 1. Remove stone [2,2] because it shares the same row as [2,1].
# 2. Remove stone [2,1] because it shares the same column as [0,1].
# 3. Remove stone [1,2] because it shares the same row as [1,0].
# 4. Remove stone [1,0] because it shares the same column as [0,0].
# 5. Remove stone [0,1] because it shares the same row as [0,0].
# Stone [0,0] cannot be removed since it does not share a row/column with
# another stone still on the plane.
#
#
# Example 2:
#
#
# Input: stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
# Output: 3
# Explanation: One way to make 3 moves is as follows:
# 1. Remove stone [2,2] because it shares the same row as [2,0].
# 2. Remove stone [2,0] because it shares the same column as [0,0].
# 3. Remove stone [0,2] because it shares the same row as [0,0].
# Stones [0,0] and [1,1] cannot be removed since they do not share a row/column
# with another stone still on the plane.
#
#
# Example 3:
#
#
# Input: stones = [[0,0]]
# Output: 0
# Explanation: [0,0] is the only stone on the plane, so you cannot remove
# it.
#
#
#
# Constraints:
#
#
# 1 <= stones.length <= 1000
# 0 <= xi, yi <= 10^4
# No two stones are at the same coordinate point.
#
#
#

# @lc code=start

from typing import List


class UnionFind:
    def __init__(self, stones):
        self.parent = {tuple(stone): tuple(stone) for stone in stones}
        self.rank = {tuple(stone): 0 for stone in stones}

    def find(self, stone):
        stone_t = tuple(stone)
        if self.parent[stone_t] != stone_t:
            self.parent[stone_t] = self.find(self.parent[stone_t])
        return self.parent[stone_t]

    def union(self, stone1, stone2):
        root1 = self.find(stone1)
        root2 = self.find(stone2)

        if root1 != root2:
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            elif self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            else:
                self.parent[root2] = root1
                self.rank[root1] += 1


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        if not stones:
            return 0

        union_find = UnionFind(stones)

        for i in range(len(stones)):
            for j in range(i + 1, len(stones)):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    union_find.union(stones[i], stones[j])

        roots = set(union_find.find(stone) for stone in stones)
        return len(stones) - len(roots)


# @lc code=end
