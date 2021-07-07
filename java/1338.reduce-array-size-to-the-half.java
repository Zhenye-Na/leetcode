/*
 * @lc app=leetcode id=1338 lang=java
 *
 * [1338] Reduce Array Size to The Half
 *
 * https://leetcode.com/problems/reduce-array-size-to-the-half/description/
 *
 * algorithms
 * Medium (67.63%)
 * Likes:    780
 * Dislikes: 65
 * Total Accepted:    60.6K
 * Total Submissions: 88.6K
 * Testcase Example:  '[3,3,3,3,5,5,5,2,2,7]'
 *
 * Given an array arr.  You can choose a set of integers and remove all the
 * occurrences of these integers in the array.
 * 
 * Return the minimum size of the set so that at least half of the integers of
 * the array are removed.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: arr = [3,3,3,3,5,5,5,2,2,7]
 * Output: 2
 * Explanation: Choosing {3,7} will make the new array [5,5,5,2,2] which has
 * size 5 (i.e equal to half of the size of the old array).
 * Possible sets of size 2 are {3,5},{3,2},{5,2}.
 * Choosing set {2,7} is not possible as it will make the new array
 * [3,3,3,3,5,5,5] which has size greater than half of the size of the old
 * array.
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: arr = [7,7,7,7,7,7]
 * Output: 1
 * Explanation: The only possible set you can choose is {7}. This will make the
 * new array empty.
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: arr = [1,9]
 * Output: 1
 * 
 * 
 * Example 4:
 * 
 * 
 * Input: arr = [1000,1000,3,7]
 * Output: 1
 * 
 * 
 * Example 5:
 * 
 * 
 * Input: arr = [1,2,3,4,5,6,7,8,9,10]
 * Output: 5
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= arr.length <= 10^5
 * arr.length is even.
 * 1 <= arr[i] <= 10^5
 * 
 */

// @lc code=start
class Solution {
    public int minSetSize(int[] arr) {
        if (arr == null || arr.length == 0)
            return 0;

        HashMap<Integer, Integer> counter = new HashMap<Integer, Integer>();
        int n = arr.length;

        for (int i = 0; i < n; i++) {
            if (counter.containsKey(arr[i])) {
                counter.put(arr[i], counter.get(arr[i]) + 1);
            } else {
                counter.put(arr[i], 1);
            }
        }

        List<Point> freq = new ArrayList<>();
        for (Map.Entry<Integer, Integer> entry : counter.entrySet())
            freq.add(
                new Point((int) entry.getValue(), (int) entry.getKey())
            );

        Collections.sort(freq, new CounterComparator());
        int curr = 0, res = 0;
        for (int i = 0; i < n; i++) {
            curr += freq.get(i).occurrence;
            res += 1;
            if (curr * 2 >= n) {
                return res;
            }
        }

        return res;
    }
}


class Point {

    int occurrence;
    int value;

    public Point(int occurrence, int value) {
        this.occurrence = occurrence;
        this.value = value;
    }

}

class CounterComparator implements Comparator<Point> {
    public int compare(Point point1, Point point2) {
        if (point1.occurrence < point2.occurrence) {
            return 1;
        } else if (point1.occurrence == point2.occurrence) {
            return 0;
        } else {
            return -1;
        }
    }
}
// @lc code=end

