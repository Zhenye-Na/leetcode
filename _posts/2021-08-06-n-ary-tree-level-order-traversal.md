---
layout: post
title: "429. N-ary Tree Level Order Traversal"
category: bfs
---


## Problem Description

Given an n-ary tree, return the level order traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).

Example 1:

![](https://raw.githubusercontent.com/Zhenye-Na/img-hosting-picgo/master/img/narytreeexample.png)

```
Input: root = [1,null,3,2,4,null,5,6]
Output: [[1],[3,2,4],[5,6]]
```


Example 2:

![](https://raw.githubusercontent.com/Zhenye-Na/img-hosting-picgo/master/img/sample_4_964.png)

```
Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: [[1],[2,3,4,5],[6,7,8,9,10],[11,12,13],[14]]
```

Constraints:

```
The height of the n-ary tree is less than or equal to 1000
The total number of nodes is between [0, 104]
```

## Solution

Level Order BFS


### Java

```java
/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> children;

    public Node() {}

    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, List<Node> _children) {
        val = _val;
        children = _children;
    }
};
*/

class Solution {
    public List<List<Integer>> levelOrder(Node root) {
        List<List<Integer>> ret = new ArrayList<List<Integer>>();
        if (root == null) {
            return ret;
        }
        
        Queue<Node> pq = new LinkedList<>();
        pq.add(root);
        while (!pq.isEmpty()) {
            List<Integer> level = new ArrayList<>();
            int size = pq.size();
            for (int i = 0; i < size; i++) {
                Node node = pq.poll();
                level.add(node.val);
                for (Node child : node.children) {
                    pq.add(child);
                }
            }

            ret.add(level);
        }
        
        return ret;
    }
}
```

**Complexity Analysis**

- Time Complexity
  - O(n)
- Space Complexity
  - O(n)
