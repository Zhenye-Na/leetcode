---
layout: post
title: "658. Find K Closest Elements"
category: heap
---


## Problem Description

Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.

An integer a is closer to x than an integer b if:

```
|a - x| < |b - x|, or
|a - x| == |b - x| and a < b
```

Example 1:

```
Input: arr = [1,2,3,4,5], k = 4, x = 3
Output: [1,2,3,4]
```


Example 2:

```
Input: arr = [1,2,3,4,5], k = 4, x = -1
Output: [1,2,3,4]
```

Constraints:

```
1 <= k <= arr.length
1 <= arr.length <= 104
arr is sorted in ascending order.
-104 <= arr[i], x <= 104
```

## Solution

I have summarized this problem with two different approaches, select the one that you like and are comfortable to write during the interview

- Binary Search
- Heap / Priority Queue

### Binary Search

There is a condition in the problem

> Given a sorted integer array arr

Given this conditionm, we can perform a Binary Search on the array, and trying to find the rightmost index which is smaller than `x` and leftmost index which is larger than or equal to `x`

> It has the same sort of requirement in the problem "search insert position"

With python we have `bisect.bisect_left()` function so that we dont need to write binary search from scratch, but for Java, you can write your own (I am not sure if Java has this kind of lib to use)

Here is the codes for Binary Search solution to this problem in Python

```python
import bisect
class Solution_BinarySearch:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if not arr or len(arr) < k:
            return arr
        
        right = bisect.bisect_left(arr, x)

        if right == 0:
            return arr[:k]
        if right == len(arr):
            return arr[len(arr) - k:]

        left = right - 1
        res = []

        while len(res) < k:
            if left >= 0 and right < len(arr):
                # this if else block could be optimized
                # to remove redundancy
                # but I dont wanna

                # Ideally, just to make sure "right - left + 1 == k"
                if abs(arr[left] - x) < abs(arr[right] - x):
                    res.append(arr[left])
                    left -= 1
                elif abs(arr[left] - x) > abs(arr[right] - x):
                    res.append(arr[right])
                    right += 1
                else:
                    if arr[right] < arr[left]:
                        res.append(arr[right])
                        right += 1
                    else:
                        res.append(arr[left])
                        left -= 1
            elif left >= 0:
                res.append(arr[left])
                left -= 1
            else:
                res.append(arr[right])
                right += 1

        return sorted(res)
```

**Complexity Analysis**

- Time Complexity
  - O(logn) on Binary Search
  - O(klogk) on sorting results
    - But if you did the optimization, do not add the number to res array and just move two pointers, we will not have this factor
- Space Complexity
  - O(1)


### Heap / Priority Queue

Heap / Priority Queue (I will use heap for short continued in this post) is the best data structure to solve "k closest/nearest/largest/smallest"-type question

Since Python and Java both have the Heap data structure already (in Java, it is called PriorityQueue), and they are both min-heap. So, we can store two value in the heap - the diff and the value of the number itself.

The algorithm to manipulate the heap is as follows:

- if the size of heap is smaller than k
  - push items into the heap
- otherwise
  - check if the new element is better than the top element in the heap
    - if the diff is smaller than the top element (min-heap), which means the top element has a larger distance and can be removed from the heap
  - if so pop the heap and add new element in the heap

when checking if the new element is better, below is the logic we used to compare

```java
class CoordinateComparator implements Comparator<Coordinate> {
    public int compare(Coordinate point1, Coordinate point2) {
        if (point1.diff < point2.diff) {
            return 1;
        } else if (point1.diff > point2.diff) {
            return -1;
        } else {
            if (point1.value < point2.value) {
                return 1;
            } else {
                return -1;
            }
        }
    }
}
```

#### Python

```python
from heapq import heappush, heappop, heappushpop

class Solution_Heap:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if not arr or len(arr) < k:
            return arr
        
        heap = []
        for num in arr:

            if len(heap) < k:
                heappush(heap, (-abs(num - x), num))
            else:
                # there are k numbers in the heap
                # pop and push if meet requirements
                if -abs(num - x) > heap[0][0]:
                    heappushpop(heap, (-abs(num - x), num))

        return sorted([ele[1] for ele in heap])
```


#### Java

> Check out how fewer lines of code needed in Python!

```java
class Solution {
    public List<Integer> findClosestElements(int[] arr, int k, int x) {
        if (arr == null || arr.length < k)
            return null;

        List<Integer> res = new ArrayList<>();
        PriorityQueue<Coordinate> pq = new PriorityQueue<Coordinate>(k, new CoordinateComparator());

        int n = arr.length;
        for (int i = 0; i < n; i++) {
            if (pq.size() < k) {
                pq.add(new Coordinate(Math.abs(arr[i] - x), arr[i]));
            } else {
                // check if we need to replace
                if (Math.abs(arr[i] - x) < pq.peek().diff) {
                    pq.poll();
                    pq.add(new Coordinate(Math.abs(arr[i] - x), arr[i]));
                }
            }
            // printPq(pq);
        }

        for (Coordinate c : pq) {
            res.add(c.value);
        }

        Collections.sort(res);
        return res;
    }
    
    
    private void printPq(PriorityQueue<Coordinate> pq) {
        for (Coordinate c : pq) {
            System.out.println(c.diff +" "+ c.value);
        }
    }
    
}


class CoordinateComparator implements Comparator<Coordinate> {
    public int compare(Coordinate point1, Coordinate point2) {
        if (point1.diff < point2.diff) {
            return 1;
        } else if (point1.diff > point2.diff) {
            return -1;
        } else {
            if (point1.value < point2.value) {
                return 1;
            } else {
                return -1;
            }
        }
    }
}


class Coordinate {
    public int diff;
    public int value;

    public Coordinate(int diff, int value) {
        this.diff = diff;
        this.value = value;
    }

}
```


**Complexity Analysis**

- Time Complexity
  - O(klogk) sorting, push/pop at most k times in a heap
- Space Complexity
  - O(1)

