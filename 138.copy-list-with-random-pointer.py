#
# @lc app=leetcode id=138 lang=python3
#
# [138] Copy List with Random Pointer
#
# https://leetcode.com/problems/copy-list-with-random-pointer/description/
#
# algorithms
# Medium (29.56%)
# Likes:    1985
# Dislikes: 503
# Total Accepted:    291.6K
# Total Submissions: 985.5K
# Testcase Example:  '{"$id":"1","next":{"$id":"2","next":null,"random":{"$ref":"2"},"val":2},"random":{"$ref":"2"},"val":1}'
#
# A linked list is given such that each node contains an additional random
# pointer which could point to any node in the list or null.
# 
# Return a deep copy of the list.
# 
# 
# 
# Example 1:
# 
# 
# 
# 
# Input:
# 
# {"$id":"1","next":{"$id":"2","next":null,"random":{"$ref":"2"},"val":2},"random":{"$ref":"2"},"val":1}
# 
# Explanation:
# Node 1's value is 1, both of its next and random pointer points to Node 2.
# Node 2's value is 2, its next pointer points to null and its random pointer
# points to itself.
# 
# 
# 
# 
# Note:
# 
# 
# You must return the copy of the given head as a reference to the cloned
# list.
# 
# 
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head is None:
            return None

        # get all the nodes
        nodes = []
        curr = head
        while curr is not None:
            nodes.append(curr)
            curr = curr.next

        # clone all the nodes
        node_map = {}
        for node in nodes:
            node_map[node] = Node(node.val)

        # clone all the next/random pointers
        tmp = head
        while tmp is not None:
            if tmp.next is not None:
                node_map[tmp].next = node_map[tmp.next]
            if tmp.random is not None:
                node_map[tmp].random = node_map[tmp.random]
            tmp = tmp.next

        return node_map[head]


# @lc code=end
