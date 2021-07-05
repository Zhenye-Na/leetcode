/*
 * @lc app=leetcode id=1220 lang=java
 *
 * [1220] Count Vowels Permutation
 *
 * https://leetcode.com/problems/count-vowels-permutation/description/
 *
 * algorithms
 * Hard (54.24%)
 * Likes:    593
 * Dislikes: 76
 * Total Accepted:    30.2K
 * Total Submissions: 52.8K
 * Testcase Example:  '1'
 *
 * Given an integer n, your task is to count how many strings of length n can
 * be formed under the following rules:
 * 
 * 
 * Each character is a lower case vowel ('a', 'e', 'i', 'o', 'u')
 * Each vowel 'a' may only be followed by an 'e'.
 * Each vowel 'e' may only be followed by an 'a' or an 'i'.
 * Each vowel 'i' may not be followed by another 'i'.
 * Each vowel 'o' may only be followed by an 'i' or a 'u'.
 * Each vowel 'u' may only be followed by an 'a'.
 * 
 * 
 * Since the answer may be too large, return it modulo 10^9 + 7.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: n = 1
 * Output: 5
 * Explanation: All possible strings are: "a", "e", "i" , "o" and "u".
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: n = 2
 * Output: 10
 * Explanation: All possible strings are: "ae", "ea", "ei", "ia", "ie", "io",
 * "iu", "oi", "ou" and "ua".
 * 
 * 
 * Example 3: 
 * 
 * 
 * Input: n = 5
 * Output: 68
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= n <= 2 * 10^4
 * 
 * 
 */

// @lc code=start
class Solution {
    public int countVowelPermutation(int n) {
        if (n == 0)
            return 0;

        // dp initialization
        // f[i][j], string length == i, ending with vowel[j]
        long[][] f = new long[n][5];

        for (int j = 0; j < 5; j++)
            f[0][j] = 1;

        int a = 0, e = 1, i = 2, o = 3, u = 4;
        int mod = (int) Math.pow(10, 9) + 7;

        for (int r = 1; r < n; r++) {
            f[r][a] = (f[r - 1][e] + f[r - 1][i] + f[r - 1][u]) % mod;
            f[r][e] = (f[r - 1][a] + f[r - 1][i]) % mod;
            f[r][i] = (f[r - 1][e] + f[r - 1][o]) % mod;
            f[r][o] = (f[r - 1][i]) % mod;
            f[r][u] = (f[r - 1][i] + f[r - 1][o]) % mod;
        }

        long res = 0;
        for (int j = 0; j < 5; j++)
            res = (res + f[n - 1][j]) % mod;

        return (int) res;
    }
}
// @lc code=end

