/*
 * @lc app=leetcode id=677 lang=java
 *
 * [677] Map Sum Pairs
 *
 * https://leetcode.com/problems/map-sum-pairs/description/
 *
 * algorithms
 * Medium (54.31%)
 * Likes:    952
 * Dislikes: 110
 * Total Accepted:    73K
 * Total Submissions: 128K
 * Testcase Example:  '["MapSum", "insert", "sum", "insert", "sum"]\n' +
  '[[], ["apple",3], ["ap"], ["app",2], ["ap"]]'
 *
 * Implement the MapSum class:
 * 
 * 
 * MapSum() Initializes the MapSum object.
 * void insert(String key, int val) Inserts the key-val pair into the map. If
 * the key already existed, the original key-value pair will be overridden to
 * the new one.
 * int sum(string prefix) Returns the sum of all the pairs' value whose key
 * starts with the prefix.
 * 
 * 
 * 
 * Example 1:
 * 
 * 
 * Input
 * ["MapSum", "insert", "sum", "insert", "sum"]
 * [[], ["apple", 3], ["ap"], ["app", 2], ["ap"]]
 * Output
 * [null, null, 3, null, 5]
 * 
 * Explanation
 * MapSum mapSum = new MapSum();
 * mapSum.insert("apple", 3);  
 * mapSum.sum("ap");           // return 3 (apple = 3)
 * mapSum.insert("app", 2);    
 * mapSum.sum("ap");           // return 5 (apple + app = 3 + 2 = 5)
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= key.length, prefix.length <= 50
 * key and prefix consist of only lowercase English letters.
 * 1 <= val <= 1000
 * At most 50 calls will be made to insert and sum.
 * 
 * 
 */

// @lc code=start
class TrieNode {
    public HashMap<Character, TrieNode> children;
    public int value;

    public TrieNode() {
        this.value = 0;
        this.children = new HashMap<>();
    }
}

class Trie {
    public TrieNode root;

    public Trie() {
        this.root = new TrieNode();
    }

    public void add(String key, int val) {
        TrieNode node = this.root;
        int length = key.length();
        for (int i = 0; i < length; i++) {
            if (!node.children.containsKey(key.charAt(i))) {
                node.children.put(key.charAt(i), new TrieNode());
            }
            node = node.children.get(key.charAt(i));
            node.value += val;
        }

    }


    public int search(String prefix) {
        TrieNode node = this.root;
        int length = prefix.length();
        for (int i = 0; i < length; i++) {
            if (!node.children.containsKey(prefix.charAt(i))) {
                return 0;
            }
            node = node.children.get(prefix.charAt(i));
        }

        return node.value;

    }

}



class MapSum {

    private Trie trie;
    private HashMap<String, Integer> record;

    /** Initialize your data structure here. */
    public MapSum() {
        this.trie = new Trie();
        this.record = new HashMap<>();
    }
    
    public void insert(String key, int val) {
        if (!this.record.containsKey(key)) {
            this.trie.add(key, val);
        } else {
            this.trie.add(key, val - this.record.get(key));
        }

        this.record.put(key, val);
    }
    
    public int sum(String prefix) {
        return this.trie.search(prefix);
    }
}

/**
 * Your MapSum object will be instantiated and called as such:
 * MapSum obj = new MapSum();
 * obj.insert(key,val);
 * int param_2 = obj.sum(prefix);
 */
// @lc code=end

