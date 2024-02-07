/*
 * @lc app=leetcode id=451 lang=rust
 *
 * [451] Sort Characters By Frequency
 *
 * https://leetcode.com/problems/sort-characters-by-frequency/description/
 *
 * algorithms
 * Medium (70.38%)
 * Likes:    7557
 * Dislikes: 250
 * Total Accepted:    584.4K
 * Total Submissions: 825.3K
 * Testcase Example:  '"tree"'
 *
 * Given a string s, sort it in decreasing order based on the frequency of the
 * characters. The frequency of a character is the number of times it appears
 * in the string.
 * 
 * Return the sorted string. If there are multiple answers, return any of
 * them.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: s = "tree"
 * Output: "eert"
 * Explanation: 'e' appears twice while 'r' and 't' both appear once.
 * So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid
 * answer.
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: s = "cccaaa"
 * Output: "aaaccc"
 * Explanation: Both 'c' and 'a' appear three times, so both "cccaaa" and
 * "aaaccc" are valid answers.
 * Note that "cacaca" is incorrect, as the same characters must be together.
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: s = "Aabb"
 * Output: "bbAa"
 * Explanation: "bbaA" is also a valid answer, but "Aabb" is incorrect.
 * Note that 'A' and 'a' are treated as two different characters.
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= s.length <= 5 * 10^5
 * s consists of uppercase and lowercase English letters and digits.
 * 
 * 
 */

// @lc code=start
use std::collections::HashMap;
use std::collections::BinaryHeap;
use std::cmp::Ordering;

use std::iter::repeat;

#[derive(Debug, Eq)]
struct Entry(i32, char);

impl PartialEq for Entry {
    fn eq(&self, other: &Self) -> bool {
        self.0 == other.0 && self.1 == other.1
    }
}

impl PartialOrd for Entry {
    fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
        Some(self.cmp(other))
    }
}

impl Ord for Entry {
    fn cmp(&self, other: &Self) -> Ordering {
        // Compare based on the first element
        let cmp_first = self.0.cmp(&other.0);
        if cmp_first != Ordering::Equal {
            return cmp_first;
        }
        // If the first elements are equal, compare based on the second element
        self.1.cmp(&other.1)
    }
}

impl Solution {
    pub fn frequency_sort(s: String) -> String {
        let mut heap = BinaryHeap::new();
        let mut counter = HashMap::new();

        for c in s.chars() {
            if let Some(v) = counter.get_mut(&c) {
                *v += 1;
                continue;
            }
            counter.insert(c, 1);
        }

        for (entry, count) in &counter {
            heap.push(Entry(*count, *entry))
        }

        let mut res = String::new();
        while let Some(elem) = heap.pop() {
            res.extend(repeat(elem.1).take(elem.0 as usize));
        }

        return res;
    }
}
// @lc code=end

