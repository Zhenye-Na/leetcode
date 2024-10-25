#
# @lc app=leetcode id=1233 lang=python3
#
# [1233] Remove Sub-Folders from the Filesystem
#
# https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/description/
#
# algorithms
# Medium (65.70%)
# Likes:    794
# Dislikes: 111
# Total Accepted:    52.1K
# Total Submissions: 79.2K
# Testcase Example:  '["/a","/a/b","/c/d","/c/d/e","/c/f"]'
#
# Given a list of folders folder, return the folders after removing all
# sub-folders in those folders. You may return the answer in any order.
#
# If a folder[i] is located within another folder[j], it is called a sub-folder
# of it.
#
# The format of a path is one or more concatenated strings of the form: '/'
# followed by one or more lowercase English letters.
#
#
# For example, "/leetcode" and "/leetcode/problems" are valid paths while an
# empty string and "/" are not.
#
#
#
# Example 1:
#
#
# Input: folder = ["/a","/a/b","/c/d","/c/d/e","/c/f"]
# Output: ["/a","/c/d","/c/f"]
# Explanation: Folders "/a/b" is a subfolder of "/a" and "/c/d/e" is inside of
# folder "/c/d" in our filesystem.
#
#
# Example 2:
#
#
# Input: folder = ["/a","/a/b/c","/a/b/d"]
# Output: ["/a"]
# Explanation: Folders "/a/b/c" and "/a/b/d" will be removed because they are
# subfolders of "/a".
#
#
# Example 3:
#
#
# Input: folder = ["/a/b/c","/a/b/ca","/a/b/d"]
# Output: ["/a/b/c","/a/b/ca","/a/b/d"]
#
#
#
# Constraints:
#
#
# 1 <= folder.length <= 4 * 10^4
# 2 <= folder[i].length <= 100
# folder[i] contains only lowercase letters and '/'.
# folder[i] always starts with the character '/'.
# Each folder name is unique.
#
#
#

# @lc code=start
from collections import deque
from typing import List


class DirectoryTrieNode:

    def __init__(self):
        self.is_folder = False
        self.children = {}
        self.folder = []


class Solution:

    def __init__(self):
        self.root_dir = DirectoryTrieNode()

    def insert(self, trie_node, folder):
        root = trie_node
        dir_names = folder.split("/")
        for dir_name in dir_names:
            if dir_name not in root.children:
                root.children[dir_name] = DirectoryTrieNode()
            root = root.children[dir_name]

        root.folder.append(folder)
        root.is_folder = True

    def removeSubfolders(self, folder: List[str]) -> List[str]:
        dummy_dir = DirectoryTrieNode()
        for f in folder:
            self.insert(dummy_dir, f)

        res = []
        queue = deque([dummy_dir])
        while queue:
            curr_dir = queue.popleft()
            if curr_dir.is_folder:
                res.extend(curr_dir.folder)
                continue

            for child in curr_dir.children:
                queue.append(curr_dir.children[child])

        return res


# @lc code=end
