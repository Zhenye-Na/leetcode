#
# @lc app=leetcode id=667 lang=python3
#
# [667] Beautiful Arrangement II
#
# https://leetcode.com/problems/beautiful-arrangement-ii/description/
#
# algorithms
# Medium (55.04%)
# Likes:    506
# Dislikes: 831
# Total Accepted:    38K
# Total Submissions: 65.3K
# Testcase Example:  '3\n2'
#
# 
# Given two integers n and k, you need to construct a list which contains n
# different positive integers ranging from 1 to n and obeys the following
# requirement: 
# 
# Suppose this list is [a1, a2, a3, ... , an], then the list [|a1 - a2|, |a2 -
# a3|, |a3 - a4|, ... , |an-1 - an|] has exactly k distinct integers.
# 
# 
# 
# If there are multiple answers, print any of them.
# 
# 
# Example 1:
# 
# Input: n = 3, k = 1
# Output: [1, 2, 3]
# Explanation: The [1, 2, 3] has three different positive integers ranging from
# 1 to 3, and the [1, 1] has exactly 1 distinct integer: 1.
# 
# 
# 
# Example 2:
# 
# Input: n = 3, k = 2
# Output: [1, 3, 2]
# Explanation: The [1, 3, 2] has three different positive integers ranging from
# 1 to 3, and the [2, 1] has exactly 2 distinct integers: 1 and 2.
# 
# 
# 
# Note:
# 
# The n and k are in the range 1 
# 
# 
#

# @lc code=start
class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        ans = list(range(1, n - k))
        for i in range(k+1):
            if i % 2 == 0:
                ans.append(n-k + i // 2)
            else:
                ans.append(n - i // 2)

        return ans


class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        self.res = []
        unique_diff = set([])
        self.dfs(n, k, [], unique_diff)
        return self.res[0]


    def dfs(self, n, k, curr, unique_diff):
        
        
        if len(curr) == n and len(unique_diff) == k:
            self.res.append(curr[:])
            return

        length = len(unique_diff)
        if length > k or len(self.res) >= 1:
            return

        for num in range(1, n + 1):
            if not curr or len(curr) == 0:
                curr.append(num)
                self.dfs(n, k, curr, unique_diff)
                curr.pop()

            elif num not in curr:
                # print(num , curr)
                next_diff = abs(num - curr[-1])
                if next_diff not in unique_diff:
                    if length + 1 > k:
                        continue
                    else:
                        unique_diff.add(next_diff)
                        curr.append(num)
                        self.dfs(n, k, curr, unique_diff)
                        curr.pop()
                        unique_diff.remove(next_diff)

                else:
                    curr.append(num)
                    self.dfs(n, k, curr, unique_diff)
                    curr.pop()

# @lc code=end

