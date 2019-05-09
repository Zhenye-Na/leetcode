# 33. Search in Rotated Sorted Array

- **Description**
    - Suppose a sorted array is rotated at some pivot unknown to you beforehand.
    - i.e., `[0 1 2 4 5 6 7]` might become `[4 5 6 7 0 1 2]`.
    - You are given a target value to search. If found in the array return its `index`, otherwise return `-1`.
    - You may assume **no duplicate** exists in the array.
- **Example**
    - For `[4, 5, 1, 2, 3]` and `target = 1`, return `2`.
    - For `[4, 5, 1, 2, 3]` and `target = 0`, return `-1`.
- **Challenge**
    - $O( \log N)$ time



## Solution

**Binary Search**

![](http://1.bp.blogspot.com/-wc7OcV2Pf7s/VckcOaJP35I/AAAAAAAAAGE/RnbvHoKxVf4/s640/leet.png)

### Python

```python
class Solution:
    """
    @param A: an integer rotated sorted array
    @param target: an integer to be searched
    @return: an integer
    """
    def search(self, A, target):
        # write your code here
        if A is None or len(A) == 0:
            return -1

        start, end = 0, len(A) - 1
        while (start + 1 < end):
            mid = (end + start) / 2

            if (A[start] < A[mid]):
                if A[start] <= target and target <= A[mid]:
                    end = mid
                else:
                    start = mid
            else:
                if A[end] >= target and A[mid] <= target:
                    start = mid
                else:
                    end = mid


        if A[start] == target:
            return start
        if A[end] == target:
            return end
        return -1
```

### Java

```java
public class Solution {
    /**
     * @param A: an integer rotated sorted array
     * @param target: an integer to be searched
     * @return: an integer
     */
    public int search(int[] A, int target) {
        // write your code here

        if (A == null || A.length == 0) return -1;

        int start = 0, end = A.length - 1;

        while (start + 1 < end) {

            int mid = (end - start) / 2 + start;

            if (A[start] < A[mid]) {

                if (A[start] <= target && target <= A[mid]) {
                    end = mid;
                } else {
                    start = mid;
                }
            } else {

                if (A[mid] <= target && target <= A[end]) {
                    start = mid;
                } else {
                    end = mid;
                }

            }

        }

        if (A[start] == target) return start;
        if (A[end] == target) return end;
        return -1;

    }
}
```
