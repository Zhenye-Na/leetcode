/*
 * @lc app=leetcode id=378 lang=java
 *
 * [378] Kth Smallest Element in a Sorted Matrix
 *
 * https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/description/
 *
 * algorithms
 * Medium (57.13%)
 * Likes:    4231
 * Dislikes: 201
 * Total Accepted:    299K
 * Total Submissions: 517.6K
 * Testcase Example:  '[[1,5,9],[10,11,13],[12,13,15]]\n8'
 *
 * Given an n x n matrix where each of the rows and columns are sorted in
 * ascending order, return the k^th smallest element in the matrix.
 * 
 * Note that it is the k^th smallest element in the sorted order, not the k^th
 * distinct element.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
 * Output: 13
 * Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and
 * the 8^th smallest number is 13
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: matrix = [[-5]], k = 1
 * Output: -5
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * n == matrix.length
 * n == matrix[i].length
 * 1 <= n <= 300
 * -10^9 <= matrix[i][j] <= 10^9
 * All the rows and columns of matrix are guaranteed to be sorted in
 * non-decreasing order.
 * 1 <= k <= n^2
 * 
 * 
 */

// @lc code=start
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
// @lc code=end

