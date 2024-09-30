"""
Description
A Trie is a tree-like data structure used to efficiently store and retrieve prefixes of a collection of strings.

In this problem, you are required to create a Trie class and implement the following functionalities:

Trie(): Initializes a Trie object
void insert(String word): Inserts the string word into the Trie
int countWordsEqualTo(String word): Returns the number of instances of the string word in the Trie
int countWordsStartingWith(String prefix): Returns the number of strings in the Trie that start with the prefix prefix
void erase(String word): Removes the string word from the Trie

1 <= word.length, prefix.length <= 2000
word and prefix only contain lowercase English letters.
The functions insert(), countWordsEqualTo(), countWordsStartingWith(), and erase() are called a maximum of 3x10^4 times in total.

It is guaranteed that the string word always exists in the trie when the erase() function is called.


Example

Example 1

Input

[
    "insert("apple")",
    "insert("apple")",
    "countWordsEqualTo("apple")",
    "countWordsStartingWith("app")",
    "erase("apple")",
    "countWordsEqualTo("apple")",
    "countWordsStartingWith("app")",
    "erase("apple")",
    "countWordsStartingWith("app")"
]

Output

[void, void, 2, 2, void, 1, 1, void, 0]

Explanation

trie.insert("apple");               // Insert "apple".
trie.insert("apple");               // Insert anothor "apple".
trie.countWordsEqualTo("apple");    // There is two instance of "apple", return 2.
trie.countWordsStartingWith("app"); // "app" is the prefix of "apple", return 2.
trie.erase("apple");                // Remove one "apple".
trie.countWordsEqualTo("apple");    // There is only one instance of "apple", return 1.
trie.countWordsStartingWith("app"); // Return 1.
trie.erase("apple");                // Remove "apple", and Trie is empty now.
trie.countWordsStartingWith("app"); // Return 0.
"""


class TrieNode:

    def __init__(self):
        self.words = []
        self.word_with_prefix_count = 0
        self.children = {}


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str):
        """
        @param word: The string to be inserted into the Trie.
        @return: nothing
        """
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()

            node = node.children[char]
            node.word_with_prefix_count += 1

        node.words.append(word)

    def count_words_equal_to(self, word: str) -> int:
        """
        @param word: The word to be searched for.
        @return: The number of words in the Trie that are equal to the given word.
        """
        node = self.root
        for char in word:
            if char not in node.children:
                return -1
            node = node.children[char]

        return len(node.words)

    def count_words_starting_with(self, prefix: str) -> int:
        """
        @param prefix: The prefix to be searched for.
        @return: The words in the Trie that have the same prefix as the given word.
        """
        node = self.root
        for char in prefix:
            if char not in node.children:
                return -1
            node = node.children[char]

        return node.word_with_prefix_count

    def erase(self, word: str):
        """
        @param word: The word to be removed.
        @return: nothing
        """
        node = self.root
        for char in word:
            node = node.children[char]
            node.word_with_prefix_count -= 1

        node.words.remove(word)
