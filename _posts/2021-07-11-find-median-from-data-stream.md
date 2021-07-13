---
layout: post
title: "295. Find Median from Data Stream"
category: heap
---


## Problem Description

The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value and the median is the mean of the two middle values.

```
For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
```

Implement the MedianFinder class:

- `MedianFinder()` initializes the MedianFinder object.
- `void addNum(int num)` adds the integer num from the data stream to the data structure.
- `double findMedian()` returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.
 

Example 1:

```
Input
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
Output
[null, null, null, 1.5, null, 2.0]

Explanation
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0
```

Constraints:

```
-10^5 <= num <= 10^5
There will be at least one element in the data structure before calling `findMedian`.
At most 5 * 10^4 calls will be made to `addNum` and `findMedian`.
```

Follow up:

- If all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
- If 99% of all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?


## Solution

Use two PriorityQueues to implement the algorithm, where

```
1. equal length
    1. length of (lower, greater) = (k, k) => then the median is the average value of the top from both queues
2. un-equal length
    1. length of (lower, greater) = (k, k + 1) => then the median is the top value of greater queue
    2. length of (lower, greater) = (k + 1, k) => then the median is the top value of lower queue

// this is because the solution I gave below, the python and java used different approach
```

Here is a leetcode post explaining the follow up question, which is perfect. [here.](https://leetcode.com/problems/find-median-from-data-stream/discuss/354195/C%2B%2B-112-ms-99-solution-w-follow-up)


### Python

```python
from heapq import heappush, heappop

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.greater = []
        self.lower = []

    def addNum(self, num: int) -> None:
        if len(self.lower) == 0 or num <= - self.lower[0]:
            heappush(self.lower, - num)
        else:
            heappush(self.greater, num)

        self._balance()


    def findMedian(self) -> float:
        if abs(len(self.greater) - len(self.lower)) == 1:
            return - self.lower[0]
        else:
            return (self.greater[0] - self.lower[0]) / 2

    def _balance(self):
        if len(self.lower) < len(self.greater):
            heappush(self.lower, - heappop(self.greater))
        if len(self.lower) > len(self.greater) + 1:
            heappush(self.greater, - heappop(self.lower))
```


### Java

```java
class MedianFinder {

    private PriorityQueue<Integer> lower;
    private PriorityQueue<Integer> greater;

    /** initialize your data structure here. */
    public MedianFinder() {
        lower = new PriorityQueue<>();
        greater = new PriorityQueue<>();
    }
    
    public void addNum(int num) {
        if (this.greater.size() == 0 || num >= this.greater.peek()) {
            this.greater.add(num);
        } else {
            this.lower.add(- num);
        }

        balance();
    }
    
    public double findMedian() {
        if (this.lower.size() == this.greater.size()) {
            return (double) (this.greater.peek() - this.lower.peek()) / 2;
        } else {
            return (double) this.greater.peek();
        }
    }

    private void balance() {
        if (this.lower.size() > this.greater.size()) {
            this.greater.add(-1 * this.lower.poll());
        }
        if (this.lower.size() + 1 < this.greater.size()) {
            this.lower.add(-1 * this.greater.poll());
        }
    }

}
```

**Complexity Analysis**

- Time Complexity
  - O(nlogn)
- Space Complexity
  - O(n)

