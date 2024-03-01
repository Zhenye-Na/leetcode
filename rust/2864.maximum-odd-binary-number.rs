/*
 * @lc app=leetcode id=2864 lang=rust
 *
 * [2864] Maximum Odd Binary Number
 *
 * https://leetcode.com/problems/maximum-odd-binary-number/description/
 *
 * algorithms
 * Easy (71.08%)
 * Likes:    295
 * Dislikes: 4
 * Total Accepted:    62.5K
 * Total Submissions: 79.3K
 * Testcase Example:  '"010"'
 *
 * You are given a binary string s that contains at least one '1'.
 * 
 * You have to rearrange the bits in such a way that the resulting binary
 * number is the maximum odd binary number that can be created from this
 * combination.
 * 
 * Return a string representing the maximum odd binary number that can be
 * created from the given combination.
 * 
 * Note that the resulting string can have leading zeros.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: s = "010"
 * Output: "001"
 * Explanation: Because there is just one '1', it must be in the last position.
 * So the answer is "001".
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: s = "0101"
 * Output: "1001"
 * Explanation: One of the '1's must be in the last position. The maximum
 * number that can be made with the remaining digits is "100". So the answer is
 * "1001".
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= s.length <= 100
 * s consists only of '0' and '1'.
 * s contains at least one '1'.
 * 
 * 
 */

// @lc code=start
use std::collections::HashMap;

impl Solution {
    pub fn maximum_odd_binary_number(s: String) -> String {
        let mut counter = HashMap::new();
        for c in s.chars() {
            counter.entry(c.to_string()).and_modify(|x| *x += 1).or_insert(1);
        }

        let ones = "1".repeat(counter.get("1").unwrap_or(&1) - 1);
        let zeros = "0".repeat(*counter.get("0").unwrap_or(&0));

        return format!("{}{}1", ones, zeros);
    }
}
// @lc code=end

