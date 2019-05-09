# 162. Find Peak Element

- **Description**
    - There is an integer array which has the following features:
    - The numbers in adjacent positions are different.

      ```
      A[0] < A[1] && A[A.length - 2] > A[A.length - 1].
      ```
      
    - We define a position P is a peak if:

      ```
      A[P] > A[P-1] && A[P] > A[P+1]
      ```

    - Find a peak element in this array. Return the index of the peak.
    - It's guaranteed the array has at least one peak.
    - The array may contain multiple peeks, **find any of them**.
    - **The array has at least 3 numbers in it**.
- **Example**
    - Given `[1, 2, 1, 3, 4, 5, 7, 6]`
    - Return index `1` (which is number `2`) or `6` (which is number `7`)
- **Challenge**
    - Time complexity O(log N)


## Solution

![](https://codebysteven.files.wordpress.com/2016/09/img_41601-e1473197754737.jpg)


We can divide into 4 situations:

1. `A[mid - 1] < A[mid] && A[mid] > A[mid + 1]`
    - Peak. directly return `mid`
2. `A[mid - 1] < A[mid] && A[mid] < A[mid + 1]`
    - Currently in ascending section, so we can make sure there exists a peak in the RHS section. So `start = mid`.
3. `A[mid - 1] > A[mid] && A[mid] < A[mid + 1]`
    - Valley. RHS or LHS, either is OK.
4. `A[mid - 1] > A[mid] && A[mid] > A[mid + 1]`
    - Currently in descending section, `end = mid`


### Python

```python
class Solution:
    """
    @param: A: An integers array.
    @return: return any of peek positions.
    """
    def findPeak(self, A):
        # write your code here
        start, end = 0, len(A) - 1
        while (start + 1 < end):
            P = (start + end) // 2

            # A[mid] is one of peaks
            if A[P] > A[P - 1] and A[P] > A[P + 1]:
                return P
            # Ascending area
            elif A[P] > A[P - 1] and A[P] < A[P + 1]:
                start = P
            # Descending area
            else:
                end = P

        return start if A[start] >= A[end] else end

```



### Java


```java
public class Solution {
    /*
     * @param A: An integers array.
     * @return: return any of peek positions.
     */
    public int findPeak(int[] A) {
        // write your code here
        int start = 0, end = A.length - 1;
        
        while (start + 1 < end) {
            
            int mid = (end - start) / 2 + start;
            
            if (A[mid - 1] < A[mid] && A[mid] < A[mid + 1]) {         // Ascending section
                start = mid;
            } else if (A[mid - 1] > A[mid] && A[mid] > A[mid + 1]) {  // Descending section
                end = mid;
            } else if (A[mid - 1] > A[mid] && A[mid] < A[mid + 1]) {  // Valley
                end = mid;
            } else {                                                  // Peak
                return mid;
            }
            
            
        }
        
        if (A[start] < A[end]) {
            return end;
        } else {
            return start;
        }

        
    }
}
```
