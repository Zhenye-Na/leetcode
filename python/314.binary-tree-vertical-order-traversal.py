# [314] Binary Tree Vertical Order Traversal

# Given a binary tree, return the vertical order traversal of its nodes' values.
# (ie, from top to bottom, column by column).

# If two nodes are in the same row and column, the order should be from left to right.

# Examples 1:

# Input: [3,9,20,null,null,15,7]

#    3
#   /\
#  /  \
#  9  20
#     /\
#    /  \
#   15   7 

# Output:

# [
#   [9],
#   [3,15],
#   [20],
#   [7]
# ]


# Examples 2:

# Input: [3,9,8,4,0,1,7]

#      3
#     /\
#    /  \
#    9   8
#   /\  /\
#  /  \/  \
#  4  01   7 

# Output:

# [
#   [4],
#   [9],
#   [3,0,1],
#   [8],
#   [7]
# ]


# Examples 3:

# Input: [3,9,8,4,0,1,7,null,null,null,2,5] (0's right child is 2 and 1's left child is 5)

#      3
#     /\
#    /  \
#    9   8
#   /\  /\
#  /  \/  \
#  4  01   7
#     /\
#    /  \
#    5   2

# Output:

# [
#   [4],
#   [9,5],
#   [3,0,1],
#   [8,2],
#   [7]
# ]




"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
from collections import defaultdict
class Solution:
    """
    @param root: the root of tree
    @return: the vertical order traversal
    """
    def verticalOrder(self, root):
        # write your code here
        if not root:
            return []

        self.hashmap = defaultdict(list)
        res = []

        self.hashmap[0].append((0, root.val))
        self.dfs(root, 0, 0)

        min_x, max_x = 0, -sys.maxsize
        for x in self.hashmap:
            max_x = max(max_x, x)
            min_x = min(min_x, x)
            self.hashmap[x] = sorted([(val[0], idx, val[1]) for idx, val in enumerate(self.hashmap[x])], key=lambda x : (x[0], x[1], x[2]))


        for x in range(min_x, max_x + 1):
            res.append([node_val for _, _, node_val in self.hashmap[x]])

        return res


    def dfs(self, root, x, depth):
        if not root:
            return

        if root.left:
            self.hashmap[x - 1].append((depth + 1, root.left.val))
            self.dfs(root.left, x - 1, depth + 1)

        if root.right:
            self.hashmap[x + 1].append((depth + 1, root.right.val))
            self.dfs(root.right, x + 1, depth + 1)


