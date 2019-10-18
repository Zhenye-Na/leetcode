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
        nodeList = self.getNodes(head)
        clone = {}
        for node in nodeList:
            clone[node] = Node(node.val, None, None)

        # copy `next` pointer
        for node in nodeList:
            clone[node].next = clone[node.next] if node.next else None

        # copy `random` pointer
        for node in nodeList:
            clone[node].random = clone[node.random] if node.random else None

        return clone[head]

    def getNodes(self, head):
        nodes = []
        while head is not None:
            nodes.append(head)
            head = head.next

        return nodes
# @lc code=end
