/*
 * @lc app=leetcode id=791 lang=java
 *
 * [791] Custom Sort String
 *
 * https://leetcode.com/problems/custom-sort-string/description/
 *
 * algorithms
 * Medium (66.00%)
 * Likes:    1362
 * Dislikes: 243
 * Total Accepted:    118.7K
 * Total Submissions: 177.2K
 * Testcase Example:  '"cba"\n"abcd"'
 *
 * order and str are strings composed of lowercase letters. In order, no letter
 * occurs more than once.
 * 
 * order was sorted in some custom order previously. We want to permute the
 * characters of str so that they match the order that order was sorted. More
 * specifically, if x occurs before y in order, then x should occur before y in
 * the returned string.
 * 
 * Return any permutation of str (as a string) that satisfies this property.
 * 
 * 
 * Example:
 * Input: 
 * order = "cba"
 * str = "abcd"
 * Output: "cbad"
 * Explanation: 
 * "a", "b", "c" appear in order, so the order of "a", "b", "c" should be "c",
 * "b", and "a". 
 * Since "d" does not appear in order, it can be at any position in the
 * returned string. "dcba", "cdba", "cbda" are also valid outputs.
 * 
 * 
 * 
 * 
 * Note:
 * 
 * 
 * order has length at most 26, and no character is repeated in order.
 * str has length at most 200.
 * order and str consist of lowercase letters only.
 * 
 * 
 */

// @lc code=start
class Solution {
    public String customSortString(String order, String str) {
       HashMap<Character, Integer> map = new HashMap<Character, Integer>();
        String ans = "";
        for (int i = 0 ; i< str.length(); i++) {
            map.put(str.charAt(i), map.getOrDefault( str.charAt(i), 0 ) + 1);
        }

        for (int i = 0; i < order.length(); i++) {
            char oo = order.charAt(i);
            if ( !map.containsKey(oo) )       
                continue;
            
            for (int j = 0; j < map.get(oo); j++)
                ans += oo;    
            map.remove(oo);         
        }

        for (Character key : map.keySet()) {
            int freq = map.get(key);
            for (int j = 0; j < freq; j++)
                ans += key;
        }

        return ans;
    }
}
// @lc code=end

