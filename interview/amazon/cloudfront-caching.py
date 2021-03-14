# Cloudfront Caching

# https://aonecode.com/amazon-online-assessment-cloudfront-caching

import math

class UnionFind:

    def __init__(self, n):
        self.leader = {}
        self.size = {}
        for i in range(1, n + 1):
            self.leader[i] = i
            self.size[i] = 1


    def _find(self, node):
        path = []
        while node != self.leader[node]:
            path.append(node)
            node = self.leader[node]

        for p in path:
            self.leader[p] = node
            self.size[p] = self.size[node]

        return node


    def union(self, node_1, node_2):
        leader_1, leader_2 = self._find(node_1), self._find(node_2)
        if leader_1 != leader_2:
            self.leader[leader_1] = leader_2
            self.size[leader_2] += self.size[leader_1]


class CloudFrontCaching:


    def connectedSum(self, n, edges):
        # create UnionFind class
        uf = UnionFind(n)

        for edge in edges:
            start, end = edge.split(" ")
            uf.union(int(start), int(end))

        # compute score
        score = 0
        for i in range(1, n + 1):
            if uf.leader[i] == i:
                # this is the leader of its group
                score += math.ceil(math.sqrt(uf.size[i]))

        print(score)
        return score


# test
solver = CloudFrontCaching()
solver.connectedSum(
    n=4,
    edges=["1 2", "1 4"]    
)


solver2 = CloudFrontCaching()
solver2.connectedSum(
    n=8,
    edges=["8 1",  "5 8", "7 3", "8 6"] 
)

