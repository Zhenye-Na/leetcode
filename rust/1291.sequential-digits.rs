/*
 * @lc app=leetcode id=1291 lang=rust
 *
 * [1291] Sequential Digits
 *
 * https://leetcode.com/problems/sequential-digits/description/
 *
 * algorithms
 * Medium (61.32%)
 * Likes:    2010
 * Dislikes: 118
 * Total Accepted:    99.1K
 * Total Submissions: 160.2K
 * Testcase Example:  '100\n300'
 *
 * An integer has sequential digits if and only if each digit in the number is
 * one more than the previous digit.
 * 
 * Return a sorted list of all the integers in the range [low, high] inclusive
 * that have sequential digits.
 * 
 * 
 * Example 1:
 * Input: low = 100, high = 300
 * Output: [123,234]
 * Example 2:
 * Input: low = 1000, high = 13000
 * Output: [1234,2345,3456,4567,5678,6789,12345]
 * 
 * 
 * Constraints:
 * 
 * 
 * 10 <= low <= high <= 10^9
 * 
 * 
 */

// @lc code=start
use std::cmp;

impl Solution {
    pub fn sequential_digits(low: i32, high: i32) -> Vec<i32> {
        let digits = "123456789";

        let min_length = low.to_string().chars().count();
        let max_length = high.to_string().chars().count();

        let mut res: Vec<i32> = Vec::new();
        for len in min_length..=cmp::min(max_length, 9) {
            for i in 0..=9 - len {
                let num: i32 = digits[i..i + len].parse().unwrap();
                if low <= num && num <= high {
                    res.push(num);
                }
            }
        }

        return res;
    }
}
// @lc code=end

