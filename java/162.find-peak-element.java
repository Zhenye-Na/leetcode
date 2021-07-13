/*
 * @lc app=leetcode id=162 lang=java
 *
 * [162] Find Peak Element
 *
 * https://leetcode.com/problems/find-peak-element/description/
 *
 * algorithms
 * Medium (44.29%)
 * Likes:    3393
 * Dislikes: 2849
 * Total Accepted:    537.6K
 * Total Submissions: 1.2M
 * Testcase Example:  '[1,2,3,1]'
 *
 * A peak element is an element that is strictly greater than its neighbors.
 * 
 * Given an integer array nums, find a peak element, and return its index. If
 * the array contains multiple peaks, return the index to any of the peaks.
 * 
 * You may imagine that nums[-1] = nums[n] = -∞.
 * 
 * You must write an algorithm that runs in O(log n) time.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: nums = [1,2,3,1]
 * Output: 2
 * Explanation: 3 is a peak element and your function should return the index
 * number 2.
 * 
 * Example 2:
 * 
 * 
 * Input: nums = [1,2,1,3,5,6,4]
 * Output: 5
 * Explanation: Your function can return either index number 1 where the peak
 * element is 2, or index number 5 where the peak element is 6.
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= nums.length <= 1000
 * -2^31 <= nums[i] <= 2^31 - 1
 * nums[i] != nums[i + 1] for all valid i.
 * 
 * 
 */

// @lc code=start
class Solution {
    public int findPeakElement(int[] nums) {
        int start = 0, end = nums.length - 1;
        int mid;
        while (start + 1 < end) {
            mid = (start + end) / 2;
            if (nums[mid] > nums[mid + 1] && nums[mid] > nums[mid - 1]) {
                return mid;
            } else if (nums[mid - 1] < nums[mid] && nums[mid] < nums[mid + 1]) {
                start = mid;
            } else {
                end = mid;
            }
        }
        if (nums[start] >= nums[end]) {
            return start;
        } else {
            return end;
        }
    }
}
// @lc code=end

