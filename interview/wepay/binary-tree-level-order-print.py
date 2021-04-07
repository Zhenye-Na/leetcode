"""
    1
2        3
       4     5

print out should be

1
2 3
. 4 . 5
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        queue = deque([root])
        res = []
        depth = self.get_depth(root)
        curr_depth = 0
        
        while queue and curr_depth < depth:
            size = len(queue)
            level = []
            for _ in range(size):
                node = queue.popleft()
                if node is not None:
                    level.append(str(node.val))
                    queue.append(node.left)
                    queue.append(node.right)
                else:
                    level.append(".")
            
            curr_depth += 1
            res.append(level)
            
        # for level in res:
        #     print(level)

        return res
            
            
            
    def get_depth(self, root):
        if not root:
            return 0
        
        left = self.get_depth(root.left)
        right = self.get_depth(root.right)
            
        return max(left, right) + 1

