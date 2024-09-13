#
# @lc app=leetcode id=1310 lang=python3
#
# [1310] XOR Queries of a Subarray
#
# https://leetcode.com/problems/xor-queries-of-a-subarray/description/
#
# algorithms
# Medium (72.28%)
# Likes:    1620
# Dislikes: 42
# Total Accepted:    86.2K
# Total Submissions: 114K
# Testcase Example:  '[1,3,4,8]\n[[0,1],[1,2],[0,3],[3,3]]'
#
# You are given an array arr of positive integers. You are also given the array
# queries where queries[i] = [lefti, righti].
#
# For each query i compute the XOR of elements from lefti to righti (that is,
# arr[lefti] XOR arr[lefti + 1] XOR ... XOR arr[righti] ).
#
# Return an array answer where answer[i] is the answer to the i^th query.
#
#
# Example 1:
#
#
# Input: arr = [1,3,4,8], queries = [[0,1],[1,2],[0,3],[3,3]]
# Output: [2,7,14,8]
# Explanation:
# The binary representation of the elements in the array are:
# 1 = 0001
# 3 = 0011
# 4 = 0100
# 8 = 1000
# The XOR values for queries are:
# [0,1] = 1 xor 3 = 2
# [1,2] = 3 xor 4 = 7
# [0,3] = 1 xor 3 xor 4 xor 8 = 14
# [3,3] = 8
#
#
# Example 2:
#
#
# Input: arr = [4,8,2,10], queries = [[2,3],[1,3],[0,0],[0,3]]
# Output: [8,0,4,4]
#
#
#
# Constraints:
#
#
# 1 <= arr.length, queries.length <= 3 * 10^4
# 1 <= arr[i] <= 10^9
# queries[i].length == 2
# 0 <= lefti <= righti < arr.length
#
#
#


# @lc code=start
class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        if not arr or len(arr) == 0:
            return []

        prefix_xor = [arr[0]]
        for i in range(1, len(arr)):
            prefix_xor.append(prefix_xor[-1] ^ arr[i])

        res = []
        for query in queries:
            start, end = query
            if start == 0:
                res.append(prefix_xor[end])
            else:
                res.append(prefix_xor[end] ^ prefix_xor[start - 1])

        return res


# @lc code=end
