#
# @lc app=leetcode id=932 lang=python3
#
# [932] Beautiful Array
#
# https://leetcode.com/problems/beautiful-array/description/
#
# algorithms
# Medium (61.61%)
# Likes:    650
# Dislikes: 933
# Total Accepted:    29K
# Total Submissions: 46K
# Testcase Example:  '4'
#
# An array nums of length n is beautiful if:
# 
# 
# nums is a permutation of the integers in the range [1, n].
# For every 0 <= i < j < n, there is no index k with i < k < j where 2 *
# nums[k] == nums[i] + nums[j].
# 
# 
# Given the integer n, return any beautiful array nums of length n. There will
# be at least one valid answer for the given n.
# 
# 
# Example 1:
# Input: n = 4
# Output: [2,1,4,3]
# Example 2:
# Input: n = 5
# Output: [3,1,2,5,4]
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 1000
# 
# 
#

# @lc code=start
class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        res = [1]
        while len(res) < n:
            res = [2 * i - 1 for i in res] + [i * 2 for i in res]

        return [i for i in res if i <= n]


    def beautifulArrayRecursion(self, n: int) -> List[int]:
        if n == 1:
            return [1]

        odd = [2 * i - 1 for i in self.beautifulArrayRecursion(n // 2 + n % 2)]
        even = [2 * i for i in self.beautifulArrayRecursion(n // 2)]

        res = odd + even
        return [i for i in res if i <= n]

    def beautifulArrayBinary(self, n: int) -> List[int]:
        return sorted(range(1, n + 1), key=lambda x: bin(x)[:1:-1])
# @lc code=end

