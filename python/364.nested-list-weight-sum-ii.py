# [364] Nested List Weight Sum II

# Description

# Given a nested list of integers, return the sum of all integers in the list weighted by their depth.

# Each element is either an integer, or a list -- whose elements may also be integers or other lists.

# Different from the previous question ([339] Nested List Weight Sum) where weight is increasing from
# root to leaf, now the weight is defined from bottom up. i.e., the leaf level integers have weight 1,
# and the root level integers have the largest weight.

# Example

# Example 1:

# Input: nestedList = [[1,1],2,[1,1]]
# Output: 8
# Explanation:
# four 1's at depth 1, one 2 at depth 2

# Example 2:

# Input: nestedList = [1,[4,[6]]]
# Output: 17
# Explanation:
# one 1 at depth 3, one 4 at depth 2, and one 6 at depth 1; 1*3 + 4*2 + 6*1 = 17



class Solution:
    """
    @param nestedList: a list of NestedInteger
    @return: the sum
    """
    def depthSumInverse(self, nestedList):
        # Write your code here.
        if not nestedList or len(nestedList) == 0:
            return 0

        self.node_depth = []
        self.dfs(nestedList, 1)

        sorted_node_path = sorted(self.node_depth, key=lambda x : x[1])
        
        max_depth = sorted_node_path[-1][1] + 1

        res = 0
        for node_val, depth in sorted_node_path:
            res += (node_val * (max_depth - depth))

        return res


    def dfs(self, lst, depth):
        if not lst or len(lst) == 0:
            self.node_depth.append([0, depth])

        for nestedInteger in lst:
            if nestedInteger.isInteger():
                self.node_depth.append([nestedInteger.getInteger(), depth])
                continue
            self.dfs(nestedInteger.getList(), depth + 1)
