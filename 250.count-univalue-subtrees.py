# [250] Count Univalue Subtrees

# Description

# Given a binary tree, count the number of uni-value subtrees.

# A Uni-value subtree means all nodes of the subtree have the same value.

# Example

# Example 1

# Input:  root = {5,1,5,5,5,#,5}
# Output: 4
# Explanation:
#               5
#              / \
#             1   5
#            / \   \
#           5   5   5
# Example 2

# Input:  root = {1,3,2,4,5,#,6}
# Output: 3
# Explanation:
#               1
#              / \
#             3   2
#            / \   \
#           4   5   6


"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the given tree
    @return: the number of uni-value subtrees.
    """
    def countUnivalSubtrees(self, root):
        # write your code here
        self.count = 0
        self.dfs(root)
        return self.count


    def dfs(self, root):
        """
        return how many subtrees with uni-values
        """
        if not root:
            return None, True

        left_node, left_uni = self.dfs(root.left)
        right_node, right_uni = self.dfs(root.right)

        if left_uni and right_uni:
            if left_node is None and right_node is None:
                self.count += 1
                return root, True
            elif left_node and left_node.val == root.val:
                self.count += 1
                return root, True
            elif right_node and right_node.val == root.val:
                self.count += 1
                return root, True
            elif right_node and left_node and left_node.val == root.val and right_node.val == root.val:
                self.count += 1
                return root, True

        return root, False

