#
# @lc app=leetcode id=646 lang=python3
#
# [646] Maximum Length of Pair Chain
#
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        if not pairs:
            return 0

        pairs.sort(key=lambda x: x[1])
        prev = - sys.maxsize - 1
        count = 0

        for idx in range(len(pairs)):
            if pairs[idx][0] > prev:
                prev = pairs[idx][1]
                count += 1

        return count


