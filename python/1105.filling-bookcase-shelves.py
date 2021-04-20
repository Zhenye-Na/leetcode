#
# @lc app=leetcode id=1105 lang=python3
#
# [1105] Filling Bookcase Shelves
#
# https://leetcode.com/problems/filling-bookcase-shelves/description/
#
# algorithms
# Medium (57.63%)
# Likes:    831
# Dislikes: 53
# Total Accepted:    22.7K
# Total Submissions: 39.5K
# Testcase Example:  '[[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]]\n4'
#
# We have a sequence of books: the i-th book has thickness books[i][0] and
# height books[i][1].
# 
# We want to place these books in order onto bookcase shelves that have total
# width shelf_width.
# 
# We choose some of the books to place on this shelf (such that the sum of
# their thickness is <= shelf_width), then build another level of shelf of the
# bookcase so that the total height of the bookcase has increased by the
# maximum height of the books we just put down. We repeat this process until
# there are no more books to place.
# 
# Note again that at each step of the above process, the order of the books we
# place is the same order as the given sequence of books.  For example, if we
# have an ordered list of 5 books, we might place the first and second book
# onto the first shelf, the third book on the second shelf, and the fourth and
# fifth book on the last shelf.
# 
# Return the minimum possible height that the total bookshelf can be after
# placing shelves in this manner.
# 
# 
# Example 1:
# 
# 
# Input: books = [[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]], shelf_width = 4
# Output: 6
# Explanation:
# The sum of the heights of the 3 shelves are 1 + 3 + 2 = 6.
# Notice that book number 2 does not have to be on the first shelf.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= books.length <= 1000
# 1 <= books[i][0] <= shelf_width <= 1000
# 1 <= books[i][1] <= 1000
# 
# 
#

# @lc code=start
class Solution:

    def minHeightShelves(self, books: List[List[int]], shelf_width: int) -> int:
        if not books or len(books) == 0 or len(books[0]) == 0:
            return 0

        n = len(books)
        books.insert(0, [0, 0])

        # dp initialization
        states = [sys.maxsize for _ in range(n + 1)]
        states[0] = 0

        for i in range(1, n + 1):

            max_height, curr_width = 0, 0
            for j in range(i, 0, -1):
                max_height = max(max_height, books[j][1])
                curr_width += books[j][0]
                if curr_width > shelf_width:
                    break

                # j-1 is the last book in the previous level
                states[i] = min(states[i], states[j - 1] + max_height)

        return states[-1]
# @lc code=end

