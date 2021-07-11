/*
 * @lc app=leetcode id=735 lang=java
 *
 * [735] Asteroid Collision
 *
 * https://leetcode.com/problems/asteroid-collision/description/
 *
 * algorithms
 * Medium (43.49%)
 * Likes:    2092
 * Dislikes: 176
 * Total Accepted:    121.9K
 * Total Submissions: 280.3K
 * Testcase Example:  '[5,10,-5]'
 *
 * We are given an array asteroids of integers representing asteroids in a
 * row.
 * 
 * For each asteroid, the absolute value represents its size, and the sign
 * represents its direction (positive meaning right, negative meaning left).
 * Each asteroid moves at the same speed.
 * 
 * Find out the state of the asteroids after all collisions. If two asteroids
 * meet, the smaller one will explode. If both are the same size, both will
 * explode. Two asteroids moving in the same direction will never meet.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: asteroids = [5,10,-5]
 * Output: [5,10]
 * Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never
 * collide.
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: asteroids = [8,-8]
 * Output: []
 * Explanation: The 8 and -8 collide exploding each other.
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: asteroids = [10,2,-5]
 * Output: [10]
 * Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide
 * resulting in 10.
 * 
 * 
 * Example 4:
 * 
 * 
 * Input: asteroids = [-2,-1,1,2]
 * Output: [-2,-1,1,2]
 * Explanation: The -2 and -1 are moving left, while the 1 and 2 are moving
 * right. Asteroids moving the same direction never meet, so no asteroids will
 * meet each other.
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 2 <= asteroids.length <= 10^4
 * -1000 <= asteroids[i] <= 1000
 * asteroids[i] != 0
 * 
 * 
 */

// @lc code=start
class Solution {
    public int[] asteroidCollision(int[] asteroids) {
        Stack<Integer> stack = new Stack<>();
        int n = asteroids.length;

        for (int i = 0; i < n; i++) {
            while (!stack.empty() && stack.peek() > 0 && stack.peek() + asteroids[i] < 0) {
                stack.pop();
            }

            if (!stack.empty() && stack.peek() > 0 && stack.peek() + asteroids[i] == 0) {
                stack.pop();
                continue;
            }

            if (!stack.empty() && stack.peek() > 0 && asteroids[i] < 0 && stack.peek() + asteroids[i] > 0) {
                continue;
            }

            stack.push(asteroids[i]);
        }

        int length = stack.size();
        int[] ret = new int[length];
        for (int i = length - 1; i >= 0; i--) {
            ret[i] = stack.pop();
        }

        return ret;
    }
}
// @lc code=end

