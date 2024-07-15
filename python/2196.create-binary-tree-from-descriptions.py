#
# @lc app=leetcode id=2196 lang=python3
#
# [2196] Create Binary Tree From Descriptions
#
# https://leetcode.com/problems/create-binary-tree-from-descriptions/description/
#
# algorithms
# Medium (72.21%)
# Likes:    944
# Dislikes: 20
# Total Accepted:    35K
# Total Submissions: 48K
# Testcase Example:  '[[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]]'
#
# You are given a 2D integer array descriptions where descriptions[i] =
# [parenti, childi, isLefti] indicates that parenti is the parent of childi in
# a binary tree of unique values. Furthermore,
#
#
# If isLefti == 1, then childi is the left child of parenti.
# If isLefti == 0, then childi is the right child of parenti.
#
#
# Construct the binary tree described by descriptions and return its root.
#
# The test cases will be generated such that the binary tree is valid.
#
#
# Example 1:
#
#
# Input: descriptions = [[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]]
# Output: [50,20,80,15,17,19]
# Explanation: The root node is the node with value 50 since it has no parent.
# The resulting binary tree is shown in the diagram.
#
#
# Example 2:
#
#
# Input: descriptions = [[1,2,1],[2,3,0],[3,4,1]]
# Output: [1,2,null,null,3,4]
# Explanation: The root node is the node with value 1 since it has no parent.
# The resulting binary tree is shown in the diagram.
#
#
#
# Constraints:
#
#
# 1 <= descriptions.length <= 10^4
# descriptions[i].length == 3
# 1 <= parenti, childi <= 10^5
# 0 <= isLefti <= 1
# The binary tree described by descriptions is valid.
#
#
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes = {}
        for description in descriptions:
            curr_root, curr_child, idx = description
            curr_root_node = (
                TreeNode(curr_root) if curr_root not in nodes else nodes[curr_root][0]
            )
            curr_child_node = (
                TreeNode(curr_child)
                if curr_child not in nodes
                else nodes[curr_child][0]
            )

            if idx == 0:
                curr_root_node.right = curr_child_node
            else:
                curr_root_node.left = curr_child_node

            if curr_root not in nodes:
                nodes[curr_root] = [curr_root_node, None]
            else:
                nodes[curr_root][0] = curr_root_node

            if curr_child not in nodes:
                nodes[curr_child] = [curr_child_node, curr_root_node]
            else:
                nodes[curr_child][0] = curr_child_node
                nodes[curr_child][1] = curr_root_node

        for val in nodes:
            if nodes[val][1] is None:
                return nodes[val][0]


# @lc code=end
