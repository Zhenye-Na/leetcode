# [302] Smallest Rectangle Enclosing Black Pixels

# Description

# An image is represented by a binary matrix with 0 as a white pixel and 1 as a black pixel.
# The black pixels are connected, i.e., there is only one black region.

# Pixels are connected horizontally and vertically.

# Given the location (x, y) of one of the black pixels, return the area of the smallest
# (axis-aligned) rectangle that encloses all black pixels.

# Example

# Example 1:

# Input：
# [
#   "0010",
#   "0110",
#   "0100"
# ],
# x=0，y=2
# Output：6
# Explanation：
# The upper left coordinate of the matrix is (0,1), and the lower right coordinate is (2,2).

# Example 2:
# Input：["1110","1100","0000","0000"], x = 0, y = 1
# Output：6
# Explanation：
# The upper left coordinate of the matrix is (0, 0), and the lower right coordinate is (1,2).

# Tag Google


class Solution:
    """
    @param image: a binary matrix with '0' and '1'
    @param x: the location of one of the black pixels
    @param y: the location of one of the black pixels
    @return: an integer
    """
    def __init__(self):
        self.WHITE = '0'
        self.BLACK = '1'

    def minArea(self, image, x, y):
        # write your code here
        # O(n^2)
        if not image or len(image) == 0 or len(image[0]) == 0:
            return 0

        m, n = len(image), len(image[0])
        x_min, x_max = n - 1, 0
        y_min, y_max = m - 1, 0

        for i in range(m):
            for j in range(n):
                if image[i][j] == self.BLACK:
                    x_min = min(x_min, j)
                    x_max = max(x_max, j)
                    y_min = min(y_min, i)
                    y_max = max(y_max, i)

        return (x_max - x_min + 1) * (y_max - y_min + 1)

