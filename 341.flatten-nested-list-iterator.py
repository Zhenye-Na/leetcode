#
# @lc app=leetcode id=341 lang=python3
#
# [341] Flatten Nested List Iterator
#
# https://leetcode.com/problems/flatten-nested-list-iterator/description/
#
# algorithms
# Medium (54.30%)
# Likes:    2087
# Dislikes: 795
# Total Accepted:    206.5K
# Total Submissions: 377.1K
# Testcase Example:  '[[1,1],2,[1,1]]'
#
# You are given a nested list of integers nestedList. Each element is either an
# integer or a list whose elements may also be integers or other lists.
# Implement an iterator to flatten it.
# 
# Implement the NestedIterator class:
# 
# 
# NestedIterator(List<NestedInteger> nestedList) Initializes the iterator with
# the nested list nestedList.
# int next() Returns the next integer in the nested list.
# boolean hasNext() Returns true if there are still some integers in the nested
# list and false otherwise.
# 
# 
# 
# Example 1:
# 
# 
# Input: nestedList = [[1,1],2,[1,1]]
# Output: [1,1,2,1,1]
# Explanation: By calling next repeatedly until hasNext returns false, the
# order of elements returned by next should be: [1,1,2,1,1].
# 
# 
# Example 2:
# 
# 
# Input: nestedList = [1,[4,[6]]]
# Output: [1,4,6]
# Explanation: By calling next repeatedly until hasNext returns false, the
# order of elements returned by next should be: [1,4,6].
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nestedList.length <= 500
# The values of the integers in the nested list is in the range [-10^6, 10^6].
# 
# 
#

# @lc code=start
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """

#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """

#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """
class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = []
        for lst in reversed(nestedList):
            self.stack.append(lst)

        self.next_val = None


    def next(self) -> int:
        if self.next_val is None:
            self.hasNext()

        tmp, self.next_val = self.next_val, None
        return tmp


    def hasNext(self) -> bool:
        if self.next_val:
            return True

        while self.stack:
            top = self.stack.pop()
            if top.isInteger():
                self.next_val = top.getInteger()
                return True
            for elem in reversed(top.getList()):
                self.stack.append(elem)

        return False


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
# @lc code=end

