---
layout: post
title: "1192. Critical Connections in a Network"
category: graph
---

## Problem Description

There are `n` servers numbered from `0` to `n-1` connected by undirected server-to-server connections forming a network where `connections[i] = [a, b]` represents a connection between servers `a` and `b`. Any server can reach any other server directly or indirectly through the network.

A critical connection is a connection that, if removed, will make some server unable to reach some other server.

Return all critical connections in the network in any order.

Example 1:

![](https://raw.githubusercontent.com/Zhenye-Na/img-hosting-picgo/master/img/1537_ex1_2.png)

```
Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
Output: [[1,3]]
Explanation: [[3,1]] is also accepted.
```

Constraints:

* `1 <= n <= 10^5`
* `n-1 <= connections.length <= 10^5`
* `connections[i][0] != connections[i][1]`
* There are no repeated connections.


## Naive Approach - Brute Force

```
for each edge in the list:
    try to remove the edge from the graph:
        check how many nodes you can visit / how many connected component in the graph
        if did not visit all the nodes or number of connected component is 2:
            add to the result
```

* You can use DFS or BFS to traverse in the graph
* You can use Union Find to contruct in every loop

Overall Time Complexity will be O(n^2)

## Tarjan's Algorithm

Before introducing what is Tarjan's Algorithm, let's explain some of the terms beforehand.

* SCC: Strongly Connected Component, a graph is said to be strongly connected if every vertex is reachable from every other vertex. For example, since Tarjan's Algorithm works for Directed Graph too, if `A -> B` and `B -> A`, then `AB` is a SCC

Tarjan's Algorithm uses DFS to traverse all the nodes in the graph, during traverse we need to do two things:

1. DFS to traverse all the nodes (trivial)
2. when traverse to a node, we need to update the distance/step/Id from its parent node
    1. for DFS, we return the smallest distance/step/Id of all the child node that current node can reach out to, except the parent node of current node

## Code Implementation

```python
from collections import defaultdict

class Solution:
    def __init__(self):
        self.graph = defaultdict(set)
        self.res = []


    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        # create graph
        self.build_graph(connections)

        # create steps array
        self.steps = [-1] * len(connections)

        # dfs
        self.dfs(0, -1, 0)
        return self.res


    def dfs(self, node, parent, step):

        self.steps[node] = step + 1

        for child in self.graph[node]:
            # if current node is parent node, we continue explore
            if child == parent:
                continue
            # if current step is -1 means we did not explore this node yet
            elif self.steps[child] == -1:
                self.steps[node] = min(
                    self.steps[node],
                    self.dfs(child, node, step + 1)
                )
            # otherwise, we just update the step of current node
            else:
                self.steps[node] = min(
                    self.steps[node],
                    self.steps[child]
                )

        # check
        # if step does not changed or it is the `0` node we start (since -1 is 0's dummy parent)
        if self.steps[node] == step + 1 and node != 0:
            self.res.append([parent, node])

        return self.steps[node]


    def build_graph(self, connections):
        for u, v in connections:
            self.graph[u].add(v)
            self.graph[v].add(u)
```

### Complexity Analysis

- Time Complexity
    - O(n)
- Space Complexity
    - O(1)

## Resources

- [【小小福讲Leetcode】LeetCode 1192. critical connections in a network 中文详解](https://www.youtube.com/watch?v=mKUsbABiwBI&ab_channel=%E5%B0%8F%E5%B0%8F%E7%A6%8FLeetCode)
- [Leetcode 1192: Critical Connections In a Network & Tarjan's Algorithm](https://www.youtube.com/watch?v=RYaakWv5m6o&ab_channel=TechRevisions)
