---
layout: post
title: "378. Kth Smallest Element in a Sorted Matrix"
category: heap
---


## Problem Description

Given an n x n matrix where each of the rows and columns are sorted in ascending order, return the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

 

Example 1:

```
Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
Output: 13
Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the 8th smallest number is 13
```

Example 2:

```
Input: matrix = [[-5]], k = 1
Output: -5
```

Constraints:

```
n == matrix.length
n == matrix[i].length
1 <= n <= 300
-109 <= matrix[i][j] <= 109
All the rows and columns of matrix are guaranteed to be sorted in non-decreasing order.
1 <= k <= n2
```

## Solution

We can use a minheap and do k-times push and pop, then the answer will be on the top of heap.

One thing to notice that for the next larger element, it will be either on the right of the current element or the element next row, same column


### Python

```python
from heapq import heappush, heappop

class Solution:
    dx = [0, 1]
    dy = [1, 0]

    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        if not matrix or len(matrix) == 0 or len(matrix[0]) == 0:
            return 0

        m, n = len(matrix), len(matrix[0])
        heap = [(matrix[0][0], 0, 0)]
        seen = set([(0, 0)])

        for _ in range(k - 1):
            _, x, y = heappop(heap)
            for i in range(2):
                newx, newy = x + self.dx[i], y + self.dy[i]
                if 0 <= newx < m and 0 <= newy < n and (newx, newy) not in seen:
                    heappush(heap, (matrix[newx][newy], newx, newy))
                    seen.add((newx, newy))

        return heap[0][0]
```

### Java

```java
class Solution {
    private int[] dx = new int[] {0, 1};
    private int[] dy = new int[] {1, 0};

    public int kthSmallest(int[][] matrix, int k) {
        if (matrix == null || matrix.length == 0 || matrix[0].length == 0 || k <= 0) {
            return 0;
        }

        int n = matrix.length, m = matrix[0].length;
        
        PriorityQueue<Point> pq = new PriorityQueue<Point>(new PointComparator());
        boolean[][] visited = new boolean[n][m];

        Point start = new Point(matrix[0][0], 0, 0);
        pq.add(start);
        visited[0][0] = true;

        for (int count = 1; count < k; count++) {
            Point prev_point = pq.poll();
            for (int d = 0; d < 2; d++) {
                int next_x = dx[d] + prev_point.x;
                int next_y = dy[d] + prev_point.y;
                if (next_x < n && next_y < m && !visited[next_x][next_y]) {
                    Point next_point = new Point(matrix[next_x][next_y], next_x, next_y);
                    pq.add(next_point);
                    visited[next_x][next_y] = true;
                }
            }
        }

        return pq.peek().value;
    }
}


class Point {
    public int value;
    public int x;
    public int y;

    public Point(int value, int x, int y) {
        this.value = value;
        this.x = x;
        this.y = y;
    }

}


class PointComparator implements Comparator<Point> {
    public int compare(Point point1, Point point2) {
        return point1.value - point2.value;
    }
}
```

**Complexity Analysis**

- Time Complexity
  - O(klogn)
- Space Complexity
  - O(n)

