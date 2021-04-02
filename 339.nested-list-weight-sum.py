# [339] Nested List Weight Sum

# Description

# Given a nested list of integers, return the sum of all integers in the 
# list weighted by their depth. Each element is either an integer, or a list

# -- whose elements may also be integers or other lists.

# Example

# Example 1:

# Input: the list [[1,1],2,[1,1]], 
# Output: 10. 
# Explanation:
# four 1's at depth 2, one 2 at depth 1, 4 * 1 * 2 + 1 * 2 * 1 = 10


# Example 2:

# Input: the list [1,[4,[6]]], 
# Output: 27. 
# Explanation:
# one 1 at depth 1, one 4 at depth 2, and one 6 at depth 3; 1 + 4 * 2 + 6 * 3 = 27

"""
This is the interface that allows for creating nested lists.
You should not implement it, or speculate about its implementation

class NestedInteger(object):
    def isInteger(self):
        # @return {boolean} True if this NestedInteger holds a single integer,
        # rather than a nested list.

    def getInteger(self):
        # @return {int} the single integer that this NestedInteger holds,
        # if it holds a single integer
        # Return None if this NestedInteger holds a nested list

    def getList(self):
        # @return {NestedInteger[]} the nested list that this NestedInteger holds,
        # if it holds a nested list
        # Return None if this NestedInteger holds a single integer
"""

class Solution(object):
    # @param {NestedInteger[]} nestedList a list of NestedInteger Object
    # @return {int} an integer
    def depthSum(self, nestedList):
        # Write your code here
        return self.dfs(nestedList, 1)


    def dfs(self, nestedList, curr_depth):
        curr_sum = 0
        for item in nestedList:
            if item.isInteger():
                curr_sum += (item.getInteger() * curr_depth)
                continue
            curr_sum += self.dfs(item.getList(), curr_depth + 1)

        return curr_sum

