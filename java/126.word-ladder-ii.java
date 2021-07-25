/*
 * @lc app=leetcode id=126 lang=java
 *
 * [126] Word Ladder II
 *
 * https://leetcode.com/problems/word-ladder-ii/description/
 *
 * algorithms
 * Hard (24.27%)
 * Likes:    2861
 * Dislikes: 310
 * Total Accepted:    247.3K
 * Total Submissions: 988.6K
 * Testcase Example:  '"hit"\n"cog"\n["hot","dot","dog","lot","log","cog"]'
 *
 * A transformation sequence from word beginWord to word endWord using a
 * dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... ->
 * sk such that:
 * 
 * 
 * Every adjacent pair of words differs by a single letter.
 * Every si for 1 <= i <= k is in wordList. Note that beginWord does not need
 * to be in wordList.
 * sk == endWord
 * 
 * 
 * Given two words, beginWord and endWord, and a dictionary wordList, return
 * all the shortest transformation sequences from beginWord to endWord, or an
 * empty list if no such sequence exists. Each sequence should be returned as a
 * list of the words [beginWord, s1, s2, ..., sk].
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: beginWord = "hit", endWord = "cog", wordList =
 * ["hot","dot","dog","lot","log","cog"]
 * Output: [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]
 * Explanation: There are 2 shortest transformation sequences:
 * "hit" -> "hot" -> "dot" -> "dog" -> "cog"
 * "hit" -> "hot" -> "lot" -> "log" -> "cog"
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: beginWord = "hit", endWord = "cog", wordList =
 * ["hot","dot","dog","lot","log"]
 * Output: []
 * Explanation: The endWord "cog" is not in wordList, therefore there is no
 * valid transformation sequence.
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= beginWord.length <= 5
 * endWord.length == beginWord.length
 * 1 <= wordList.length <= 1000
 * wordList[i].length == beginWord.length
 * beginWord, endWord, and wordList[i] consist of lowercase English
 * letters.
 * beginWord != endWord
 * All the words in wordList are unique.
 * 
 * 
 */

// @lc code=start
class Solution {
    private Map<String, Set<String>> graph;
    private List<List<String>> result;
    private Map<String, Integer> distance;
    
    public List<List<String>> findLadders(String beginWord, String endWord, List<String> wordList) {
        distance = new HashMap<>();
        graph = buildGraph(beginWord, wordList);
        result = new ArrayList<>();
        dfs(beginWord, endWord,  new ArrayList<>());
        return result;
    }
    
    private void dfs(String word, String target, List<String> solution) {
        solution.add(word);
        if (target.equals(word)) {
            result.add(solution);
        } else {
            for (String child : graph.get(word)) {
                if (distance.get(word) + 1 == distance.getOrDefault(child, Integer.MAX_VALUE)) { 
                    dfs(child, target, new ArrayList<>(solution));
                }
            }
        }
    }
    
    private Map<String, Set<String>> buildGraph(String beginWord, List<String> wordList) {
        Map<String, Set<String>> map = new HashMap<>();
        Queue<String> queue = new LinkedList<>();
        queue.add(beginWord);
        distance.put(beginWord, 0);
        while (!queue.isEmpty()) {
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                String word = queue.poll();
                Set<String> set = map.getOrDefault(word, new HashSet<>());
                map.put(word, set);
                for (String s : wordList) {
                    int cnt = 0;
                    for (int j = 0; j < word.length(); j++) {
                        if (s.charAt(j) != word.charAt(j)) {
                            cnt++;
                        }
                    }
                    if (cnt == 1) {
                        if (!distance.containsKey(s)) {
                            queue.add(s);
                            distance.put(s, distance.get(word) + 1);
                        }
                        set.add(s);
                    }
                }
            }
        }
        return map;
    }
    
}
// @lc code=end

