# Shopping Patterns

#   https://aonecode.com/amazon-online-assessment-shopping-patterns

from collections import defaultdict

class ShoppingPatterns:

    def __init__(self):
        self.neighbors = defaultdict(list)


    def getMinScore(self, products_nodes, products_edges, products_from, products_to):
            if products_edges <= products_nodes - 1:
                # graph without cycle, no trios
                return -1

            if len(products_from) != len(products_to):
                return -1

            self._build_graph(products_from, products_to)

            min_score = 3 * products_nodes
            for node in range(1, products_nodes):
                # extract node 1
                neighbors = self.neighbors[node]
                for i in range(len(neighbors)):
                    second_node = neighbors[i]
                    second_node_neighbors = self.neighbors[second_node]

                    for j in range(i + 1, len(neighbors)):
                        if neighbors[j] in second_node_neighbors:
                            # we find a trios, compute score
                            min_score = min( min_score, len(self.neighbors[node]) + len(self.neighbors[second_node]) + len(self.neighbors[neighbors[j]]) - 6 )
            print(min_score)
            return min_score


    def _build_graph(self, products_from, products_to):
        length = len(products_from)
        for i in range(length):
            self.neighbors[products_from[i]].append(products_to[i])
            self.neighbors[products_to[i]].append(products_from[i])


# test
solver = ShoppingPatterns()
solver.getMinScore(
    6,
    6,
    [1,2,2,3,4,5],
    [2,4,5,5,5,6]
)

solver2 = ShoppingPatterns()
solver2.getMinScore(
    5,
    6,
    [1,1,2,2,3,4],
    [2,3,3,4,4,5]
)

