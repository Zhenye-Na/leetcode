/*
 * @lc app=leetcode id=1481 lang=rust
 *
 * [1481] Least Number of Unique Integers after K Removals
 *
 * https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals/description/
 *
 * algorithms
 * Medium (55.92%)
 * Likes:    1524
 * Dislikes: 151
 * Total Accepted:    121.3K
 * Total Submissions: 211.6K
 * Testcase Example:  '[5,5,4]\n1'
 *
 * Given an array of integers arr and an integer k. Find the least number of
 * unique integers after removing exactly k elements.
 * 
 * 
 * 
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: arr = [5,5,4], k = 1
 * Output: 1
 * Explanation: Remove the single 4, only 5 is left.
 * 
 * Example 2:
 * 
 * 
 * Input: arr = [4,3,1,1,3,3,2], k = 3
 * Output: 2
 * Explanation: Remove 4, 2 and either one of the two 1s or three 3s. 1 and 3
 * will be left.
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= arr.length <= 10^5
 * 1 <= arr[i] <= 10^9
 * 0 <= k <= arr.length
 * 
 */

// @lc code=start
use std::collections::{HashMap, VecDeque};

impl Solution {
    pub fn find_least_num_of_unique_ints(arr: Vec<i32>, k: i32) -> i32 {
        let mut counts = Solution::get_count_of_nums(arr);
        let mut sorted_counts = Solution::sort_by_value(&counts);

        let mut i = 0;
        let mut index = 0;
        while index < sorted_counts.len() {
            let (_, value) = sorted_counts[index];
            if i + value <= k as usize {
                sorted_counts.pop_front();
                i += value;
            } else {
                break;
            }
        }

        return sorted_counts.len() as i32;
    }

    pub fn get_count_of_nums(numbers: Vec<i32>) -> HashMap<i32, usize> {
        let mut counts: HashMap<i32, usize> = HashMap::new();

        for &num in &numbers {
            let count = counts.entry(num).or_insert(0);
            *count += 1;
        }

        return counts;
    }

    pub fn sort_by_value(counts: &HashMap<i32, usize>) -> VecDeque<(i32, usize)> {
        let mut count_vec: Vec<_> = counts.iter().collect();
        count_vec.sort_by(|a, b| a.1.cmp(&b.1));
        return count_vec.into_iter().map(|(&k, &v)| (k, v)).collect();
    }
}
// @lc code=end

