class Solution:
    """
    @param: A: An integers array.
    @return: return any of peek positions.
    """
    def findPeak(self, A):
        # write your code here
        start, end = 0, len(A) - 1
        while (start + 1 < end):
            P = (start + end) // 2

            # A[mid] is one of peaks
            if A[P] > A[P - 1] and A[P] > A[P + 1]:
                return P
            # Ascending area
            elif A[P] > A[P - 1] and A[P] < A[P + 1]:
                start = P
            # Descending area
            else:
                end = P

        return start if A[start] >= A[end] else end
