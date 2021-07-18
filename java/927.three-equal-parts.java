/*
 * @lc app=leetcode id=927 lang=java
 *
 * [927] Three Equal Parts
 *
 * https://leetcode.com/problems/three-equal-parts/description/
 *
 * algorithms
 * Hard (34.82%)
 * Likes:    547
 * Dislikes: 92
 * Total Accepted:    20.4K
 * Total Submissions: 53K
 * Testcase Example:  '[1,0,1,0,1]'
 *
 * You are given an array arr which consists of only zeros and ones, divide the
 * array into three non-empty parts such that all of these parts represent the
 * same binary value.
 * 
 * If it is possible, return any [i, j] with i + 1 < j, such that:
 * 
 * 
 * arr[0], arr[1], ..., arr[i] is the first part,
 * arr[i + 1], arr[i + 2], ..., arr[j - 1] is the second part, and
 * arr[j], arr[j + 1], ..., arr[arr.length - 1] is the third part.
 * All three parts have equal binary values.
 * 
 * 
 * If it is not possible, return [-1, -1].
 * 
 * Note that the entire part is used when considering what binary value it
 * represents. For example, [1,1,0] represents 6 in decimal, not 3. Also,
 * leading zeros are allowed, so [0,1,1] and [1,1] represent the same value.
 * 
 * 
 * Example 1:
 * Input: arr = [1,0,1,0,1]
 * Output: [0,3]
 * Example 2:
 * Input: arr = [1,1,0,1,1]
 * Output: [-1,-1]
 * Example 3:
 * Input: arr = [1,1,0,0,1]
 * Output: [0,2]
 * 
 * 
 * Constraints:
 * 
 * 
 * 3 <= arr.length <= 3 * 10^4
 * arr[i] is 0 or 1
 * 
 * 
 */

// @lc code=start
class Solution {
    public int[] threeEqualParts(int[] arr) {
        int sum = 0;
        for (int i = 0; i < arr.length; i++) {
            sum += arr[i];
        }

        if (sum % 3 != 0) {
            return new int[]{-1, -1};
        }

        if (sum == 0) {
            return new int[]{0, arr.length - 1};
        }

        int[] ret = new int[2];
        int count = (int) sum / 3;

        // count from end to start
        int j = arr.length - 1;
        while (j >= 0 && count > 0) {
            if (arr[j] == 1) {
                count--;
            }
            j--;
        }

        // j point to the first `1` in the third part
        j++;


        // check for the first part
        int i = 0;
        while (i < arr.length && arr[i] == 0) {
            i++;
        }

        // i points to the first `1`

        int pointer = j;
        while (pointer < arr.length) {
            if (arr[i] == arr[pointer]) {
                i++;
                pointer++;
            } else {
                break;
            }
        }

        if (pointer != arr.length) {
            return new int[]{-1, -1};
        }

        ret[0] = i - 1;

        // check for the second part
        while (i < arr.length && arr[i] == 0) {
            i++;
        }

        pointer = j;
        while (pointer < arr.length) {
            if (arr[i] == arr[pointer]) {
                i++;
                pointer++;
            } else {
                break;
            }
        }

        if (pointer != arr.length) {
            return new int[]{-1, -1};
        }

        ret[1] = i;

        return ret;
    }
}
// @lc code=end

