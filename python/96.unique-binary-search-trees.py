#
# @lc app=leetcode id=96 lang=python3
#
# [96] Unique Binary Search Trees
#
# https://leetcode.com/problems/unique-binary-search-trees/description/
#
# algorithms
# Medium (54.22%)
# Likes:    4416
# Dislikes: 162
# Total Accepted:    353K
# Total Submissions: 647.4K
# Testcase Example:  '3'
#
# Given an integer n, return the number of structurally unique BST's (binary
# search trees) which has exactly n nodes of unique values from 1 to n.
# 
# 
# Example 1:
# 
#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3
# 
# Input: n = 3
# Output: 5
# 
# 
# Example 2:
# 
# 
# Input: n = 1
# Output: 1
# 
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 19
# 
# 
#

# @lc code=start
class Solution_DynamicProgramming:
    def numTrees(self, n: int) -> int:
        # initialization
        num_tree = [1 for _ in range(n + 1)]

        # example
        # num_tree[4] = num_tree[0] * num_tree[3] + \
        #               num_tree[1] * num_tree[2] + \
        #               num_tree[2] * num_tree[1] + \
        #               num_tree[3] * num_tree[0] + \

        for node in range(2, n + 1):
            curr_total = 0
            for root in range(1, node + 1):
                left_nodes = root - 1
                right_nodes = node - root
                curr_total += num_tree[left_nodes] * num_tree[right_nodes]

            num_tree[i] = curr_total

        return num_tree[n]


class Solution_Catalan:
    def numTrees(self, n: int) -> int:
        
        if n <= 1:
            return 1

        # Table to store results of subproblems
        catalan = [0 for i in range(n + 1)]

        # Initialize first two values in table
        catalan[0] = 1
        catalan[1] = 1

        # Fill entries in catalan[] using recursive formula
        for i in range(2, n + 1):
            catalan[i] = 0
            for j in range(i):
                catalan[i] += catalan[j] * catalan[i - j - 1]

        # Return last entry
        return catalan[n]
# @lc code=end

