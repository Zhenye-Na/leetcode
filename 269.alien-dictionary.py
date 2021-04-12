# [269] Alien Dictionary

# Description

# There is a new alien language which uses the latin alphabet. However,
# the order among letters are unknown to you. You receive a list of
# non-empty words from the dictionary, where words are sorted
# lexicographically by the rules of this new language.

# Derive the order of letters in this language.

# You may assume all letters are in lowercase.
# The dictionary is invalid, if a is prefix of b and b is appear before a.
# If the order is invalid, return an empty string.

# There may be multiple valid order of letters, return the smallest in normal lexicographical order

# Example

# Example 1:

# Input：["wrt","wrf","er","ett","rftt"]
# Output："wertf"
# Explanation：
# from "wrt"and"wrf" ,we can get 't'<'f'
# from "wrt"and"er" ,we can get 'w'<'e'
# from "er"and"ett" ,we can get 'r'<'t'
# from "ett"and"rftt" ,we can get 'e'<'r'
# So return "wertf"

# Example 2:

# Input：["z","x"]
# Output："zx"
# Explanation：
# from "z" and "x"，we can get 'z' < 'x'
# So return "zx"

from heapq import heappush, heappop, heapify

class Solution:
    """
    @param words: a list of words
    @return: a string which is correct order
    """
    def alienOrder(self, words):
        # Write your code here
        graph = self.build_graph(words)
        if not graph:
            return ""
        return self.topological_sort(graph)


    def build_graph(self, words):
        # key is node, value is neighbors
        graph = {}

        # initialize graph
        for word in words:
            for c in word:
                if c not in graph:
                    graph[c] = set() 

        # add edges        
        n = len(words)
        for i in range(n - 1):
            for j in range(min(len(words[i]), len(words[i + 1]))):
                if words[i][j] != words[i + 1][j]:
                    graph[words[i][j]].add(words[i + 1][j])
                    break
                if j == min(len(words[i]), len(words[i + 1])) - 1:
                    if len(words[i]) > len(words[i + 1]):
                        return None
                
        return graph


    def topological_sort(self, graph):        
        # initialize indegree 
        indegree = {
            node: 0
            for node in graph
        }
        
        # calculate indegree
        for node in graph:
            for neighbor in graph[node]:
                indegree[neighbor] = indegree[neighbor] + 1
        
        # use heapq instead of regular queue so that we can get the 
        # smallest lexicographical order
        queue = [node for node in graph if indegree[node] == 0]
        heapify(queue)
        
        # regular bfs algorithm to do topological sorting
        topo_order = ""
        while queue:
            node = heappop(queue)
            topo_order += node
            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    heappush(queue, neighbor)
            
        # if all nodes popped
        if len(topo_order) == len(graph):
            return topo_order
        
        return ""

