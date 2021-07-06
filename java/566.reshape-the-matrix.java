/*
 * @lc app=leetcode id=566 lang=java
 *
 * [566] Reshape the Matrix
 *
 * https://leetcode.com/problems/reshape-the-matrix/description/
 *
 * algorithms
 * Easy (61.09%)
 * Likes:    1198
 * Dislikes: 133
 * Total Accepted:    137.7K
 * Total Submissions: 222.5K
 * Testcase Example:  '[[1,2],[3,4]]\n1\n4'
 *
 * In MATLAB, there is a handy function called reshape which can reshape an m x
 * n matrix into a new one with a different size r x c keeping its original
 * data.
 * 
 * You are given an m x n matrix mat and two integers r and c representing the
 * row number and column number of the wanted reshaped matrix.
 * 
 * The reshaped matrix should be filled with all the elements of the original
 * matrix in the same row-traversing order as they were.
 * 
 * If the reshape operation with given parameters is possible and legal, output
 * the new reshaped matrix; Otherwise, output the original matrix.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: mat = [[1,2],[3,4]], r = 1, c = 4
 * Output: [[1,2,3,4]]
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: mat = [[1,2],[3,4]], r = 2, c = 4
 * Output: [[1,2],[3,4]]
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * m == mat.length
 * n == mat[i].length
 * 1 <= m, n <= 100
 * -1000 <= mat[i][j] <= 1000
 * 1 <= r, c <= 300
 * 
 * 
 */

// @lc code=start
class Solution {
    public int[][] matrixReshape(int[][] mat, int r, int c) {
        if (mat == null || mat.length == 0 || mat[0].length == 0)
            return mat;

        int n = mat.length, m = mat[0].length;
        if (n * m != r * c)
            return mat;

        int[][] ret = new int[r][c];

        for (int i = 0; i < n; i++) {
            for ( int j = 0; j < m; j++) {
                int xy = i * m + j;
                int x = xy / c;
                int y = xy % c;
                ret[x][y] = mat[i][j];
            }
        }

        return ret;
    }
}
// @lc code=end

// 57/57 cases passed (0 ms)
// Your runtime beats 100 % of java submissions
// Your memory usage beats 69.25 % of java submissions (39.9 MB)
