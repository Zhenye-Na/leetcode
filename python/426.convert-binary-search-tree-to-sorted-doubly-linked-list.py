# [426] Convert Binary Search Tree to Sorted Doubly Linked List

# Description

# Convert a BST to a sorted circular doubly-linked list in-place.
# Think of the left and right pointers as synonymous to the previous
# and next pointers in a doubly-linked list.

# Let's take the following BST as an example, it may help you understand the problem better:

# ![](https://assets.leetcode.com/uploads/2018/10/12/bstdlloriginalbst.png)

# We want to transform this BST into a circular doubly linked list.
# Each node in a doubly linked list has a predecessor and successor.
# For a circular doubly linked list, the predecessor of the first element
# is the last element, and the successor of the last element is the first
# element.

# The figure below shows the circular doubly linked list for the BST above.
# The "head" symbol means the node it points to is the smallest element of
# the linked list.

# ![](https://assets.leetcode.com/uploads/2018/10/12/bstdllreturndll.png)
 
# Specifically, we want to do the transformation in place. After the transformation,
# the left pointer of the tree node should point to its predecessor, and the right
# pointer should point to its successor. We should return the pointer to the first
# element of the linked list.

# The figure below shows the transformed BST. The solid line indicates the successor
# relationship, while the dashed line means the predecessor relationship.

# ![](https://assets.leetcode.com/uploads/2018/10/12/bstdllreturnbst.png)

# Example

# Example 1:

# Input: {4,2,5,1,3}
#          4
#        /  \
#       2   5
#      / \
#     1   3
# Output: "left:1->5->4->3->2  right:1->2->3->4->5"
# Explanation:
# Left: reverse output
# Right: positive sequence output


# Example 2:

# Input: {2,1,3}
#          2
#        /  \
#       1   3
# Output: "left:1->3->2  right:1->2->3"



"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: root of a tree
    @return: head node of a doubly linked list
    """
    def treeToDoublyList(self, root):
        # Write your code here.
        dummy = TreeNode(0)
        stack = []
        node = root

        orders = []

        while node:
            stack.append(node)
            node = node.left


        while stack:
            node = stack.pop()
            orders.append(node)
            if node.right:
                node = node.right
                while node:
                    stack.append(node)
                    node = node.left

        # orders contains inorder traversal of root

        first = prev = orders[0]
        last = orders[-1]

        dummy.right = first

        for i in range(1, len(orders)):
            prev.right = orders[i]
            orders[i].left = prev

            prev = orders[i]

        last.right = first
        first.left = last

        return dummy.right

