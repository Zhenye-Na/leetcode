# Storage Optimization

#   https://aonecode.com/amazon-online-assessment-storage-optimization


# Intuitive Solution
# O(mn) Time

def storage_opt(n, m, h, v):
    return get_max(n + 1, h) * get_max(m + 1, v)


def get_max(length, bars):
    separators = set([])
    for i in range(1, length):
        separators.add(i)

    for i in bars:
        separators.remove(i)

    if separators < 1:
        return length

    max_length = separators[0]
    for i in range(1, len(separators)):
        max_length = max(max_length, separators[i] - separators[i - 1])

    max_length = max(max_length, length - separators[-1])

    return max_length




# Union Find Solution -> Time Limit Exceeded

# Time Complexity:
#   - O(mn) to create UnionFind object
#   - O(hm) to union column cells
#   - O(vn) to union row cells
#   - O(mn) to find the max area
#   - Overall: O(mn)

# Space Complexity:  O(mn)

class UnionFind:

    def __init__(self, n, m):
        self.leader = {}
        self.area = {}
        for i in range(0, n + 1):
            for j in range(0, m + 1):
                self.leader[(i, j)] = (i, j)
                self.area[(i, j)] = 1
        

    def _find(self, point):
        path = []
        while point != self.leader[point]:
            path.append(point)
            point = self.leader[point]

        for node in path:
            self.leader[node] = point

        return point

    def union(self, point_a, point_b):
        leader_a, leader_b = self._find(point_a), self._find(point_b)
        if leader_a != leader_b:
            self.leader[leader_a] = leader_b
            self.area[leader_b] += self.area[leader_a]


class StorageOptimization:

    def solve(self, n, m, h, v):
        
        uf = UnionFind(n, m)

        for _h in h:
            for col in range(m + 1):
                uf.union((_h - 1, col), (_h, col))

        for _v in v:
            for row in range(n + 1):
                uf.union((row, _v - 1), (row, _v))

        max_area = 0
        for i in range(n + 1):
            for j in range(m + 1):
                max_area = max(max_area, uf.area[(i, j)])
        print(max_area)
        return max_area

# tests
so1 = StorageOptimization()
so1.solve(
    6,
    6,
    [4],
    [2]
)

so2 = StorageOptimization()
so2.solve(
    3,
    3,
    [2],
    [2]
)

so3 = StorageOptimization()
so3.solve(
    2,
    2,
    [1],
    [2]
)

so3 = StorageOptimization()
so3.solve(
    3,
    2,
    [1, 2, 3],
    [1, 2]
)
