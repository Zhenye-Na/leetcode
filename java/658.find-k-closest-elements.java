/*
 * @lc app=leetcode id=658 lang=java
 *
 * [658] Find K Closest Elements
 *
 * https://leetcode.com/problems/find-k-closest-elements/description/
 *
 * algorithms
 * Medium (42.80%)
 * Likes:    2657
 * Dislikes: 347
 * Total Accepted:    182.8K
 * Total Submissions: 422.8K
 * Testcase Example:  '[1,2,3,4,5]\n4\n3'
 *
 * Given a sorted integer array arr, two integers k and x, return the k closest
 * integers to x in the array. The result should also be sorted in ascending
 * order.
 * 
 * An integer a is closer to x than an integer b if:
 * 
 * 
 * |a - x| < |b - x|, or
 * |a - x| == |b - x| and a < b
 * 
 * 
 * 
 * Example 1:
 * Input: arr = [1,2,3,4,5], k = 4, x = 3
 * Output: [1,2,3,4]
 * Example 2:
 * Input: arr = [1,2,3,4,5], k = 4, x = -1
 * Output: [1,2,3,4]
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= k <= arr.length
 * 1 <= arr.length <= 10^4
 * arr is sorted in ascending order.
 * -10^4 <= arr[i], x <= 10^4
 * 
 * 
 */

// @lc code=start
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
// @lc code=end

