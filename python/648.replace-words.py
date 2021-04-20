#
# @lc app=leetcode id=648 lang=python3
#
# [648] Replace Words
#


class TrieNode:

    def __init__(self):
        self.children = {}
        self.is_word = False
        self.word = None


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]

        node.is_word = True
        node.word = word

    def _find(self, word):
        node = self.root
        for ch in word:
            node = node.children.get(ch)
            if node is None:
                return None
            elif node.is_word == True:
                return node

    def searchRoot(self, word):
        node = self._find(word)
        if node is not None:
            return node.word
        else:
            return word


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        replaced_sentence = []
        if dictionary is None or sentence is None or len(dictionary) == 0 or len(sentence) == 0:
            return replaced_sentence

        trie = Trie()
        for root_word in dictionary:
            trie.insert(root_word)

        sentence_list = sentence.split()

        for word in sentence_list:
            new_word = trie.searchRoot(word)
            replaced_sentence.append(new_word)

        return " ".join(replaced_sentence)
