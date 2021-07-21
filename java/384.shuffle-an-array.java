/*
 * @lc app=leetcode id=384 lang=java
 *
 * [384] Shuffle an Array
 *
 * https://leetcode.com/problems/shuffle-an-array/description/
 *
 * algorithms
 * Medium (54.43%)
 * Likes:    337
 * Dislikes: 379
 * Total Accepted:    202.1K
 * Total Submissions: 366.3K
 * Testcase Example:  '["Solution","shuffle","reset","shuffle"]\n[[[1,2,3]],[],[],[]]'
 *
 * Given an integer array nums, design an algorithm to randomly shuffle the
 * array. All permutations of the array should be equally likely as a result of
 * the shuffling.
 * 
 * Implement the Solution class:
 * 
 * 
 * Solution(int[] nums) Initializes the object with the integer array nums.
 * int[] reset() Resets the array to its original configuration and returns
 * it.
 * int[] shuffle() Returns a random shuffling of the array.
 * 
 * 
 * 
 * Example 1:
 * 
 * 
 * Input
 * ["Solution", "shuffle", "reset", "shuffle"]
 * [[[1, 2, 3]], [], [], []]
 * Output
 * [null, [3, 1, 2], [1, 2, 3], [1, 3, 2]]
 * 
 * Explanation
 * Solution solution = new Solution([1, 2, 3]);
 * solution.shuffle();    // Shuffle the array [1,2,3] and return its result.
 * ⁠                      // Any permutation of [1,2,3] must be equally likely
 * to be returned.
 * ⁠                      // Example: return [3, 1, 2]
 * solution.reset();      // Resets the array back to its original
 * configuration [1,2,3]. Return [1, 2, 3]
 * solution.shuffle();    // Returns the random shuffling of array [1,2,3].
 * Example: return [1, 3, 2]
 * 
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= nums.length <= 200
 * -10^6 <= nums[i] <= 10^6
 * All the elements of nums are unique.
 * At most 5 * 10^4 calls in total will be made to reset and shuffle.
 * 
 * 
 */

// @lc code=start
class Solution {

    private int [] nums;
    private Random random;

    public Solution(int[] nums) {
        this.nums = nums;
        this.random = new Random();
    }

    /** Resets the array to its original configuration and return it. */
    public int[] reset() {
        return nums;
    }

    /** Returns a random shuffling of the array. */
    public int[] shuffle() {
        // keep generating random index, and keep swapping,
        // since random idx->[0,i] so iterate arr from end so that randomindex lies where the index decision has not been taken
        int [] copyarr = nums.clone();
        
        for (int i = nums.length - 1; i > 0; i--) {
            int ridx = random.nextInt(i + 1); // i+1 bcoz indexing is from 1-n and not 0-n-1
            // swap elements at ridx and i
            int temp = copyarr[i];
            copyarr[i] = copyarr[ridx];
            copyarr[ridx] = temp;
        }
        return copyarr;
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(nums);
 * int[] param_1 = obj.reset();
 * int[] param_2 = obj.shuffle();
 */
// @lc code=end

