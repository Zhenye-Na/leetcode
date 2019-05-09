96. Unique Binary Search Trees
Description
Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

Example:

Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:

```
   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
```


## Solution

```python
class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return 1

        # Table to store results of subproblems
        catalan = [0 for i in range(n + 1)]

        # Initialize first two values in table
        catalan[0] = 1
        catalan[1] = 1

        # Fill entries in catalan[] using recursive formula
        for i in range(2, n + 1):
            catalan[i] = 0
            for j in range(i):
                catalan[i] += catalan[j] * catalan[i - j - 1]

        # Return last entry
        return catalan[n]


```
