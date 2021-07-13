/*
 * @lc app=leetcode id=205 lang=java
 *
 * [205] Isomorphic Strings
 *
 * https://leetcode.com/problems/isomorphic-strings/description/
 *
 * algorithms
 * Easy (40.89%)
 * Likes:    2445
 * Dislikes: 520
 * Total Accepted:    402.9K
 * Total Submissions: 974.8K
 * Testcase Example:  '"egg"\n"add"'
 *
 * Given two strings s and t, determine if they are isomorphic.
 * 
 * Two strings s and t are isomorphic if the characters in s can be replaced to
 * get t.
 * 
 * All occurrences of a character must be replaced with another character while
 * preserving the order of characters. No two characters may map to the same
 * character, but a character may map to itself.
 * 
 * 
 * Example 1:
 * Input: s = "egg", t = "add"
 * Output: true
 * Example 2:
 * Input: s = "foo", t = "bar"
 * Output: false
 * Example 3:
 * Input: s = "paper", t = "title"
 * Output: true
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= s.length <= 5 * 10^4
 * t.length == s.length
 * s and t consist of any valid ascii character.
 * 
 * 
 */

// @lc code=start
class Solution {
    public boolean isIsomorphic(String s, String t) {
        HashMap<Character, Character> s2t = new HashMap<>();
        HashMap<Character, Character> t2s = new HashMap<>();

        int n = s.length();
        for (int i = 0; i < n; i++) {
            if (!s2t.containsKey(s.charAt(i))) {
                if (t2s.containsKey(t.charAt(i)) && t2s.get(t.charAt(i)) != s.charAt(i)) {
                    return false;
                }
                s2t.put(s.charAt(i), t.charAt(i));
                t2s.put(t.charAt(i), s.charAt(i));
            } else {
                if (t.charAt(i) != s2t.get(s.charAt(i))) {
                    return false;
                }
            }
        }

        return true;
    }
}
// @lc code=end

