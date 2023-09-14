#
# @lc app=leetcode id=332 lang=python3
#
# [332] Reconstruct Itinerary
#
# https://leetcode.com/problems/reconstruct-itinerary/description/
#
# algorithms
# Medium (38.84%)
# Likes:    5073
# Dislikes: 1723
# Total Accepted:    356.3K
# Total Submissions: 845.9K
# Testcase Example:  '[["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]'
#
# You are given a list of airline tickets where tickets[i] = [fromi, toi]
# represent the departure and the arrival airports of one flight. Reconstruct
# the itinerary in order and return it.
# 
# All of the tickets belong to a man who departs from "JFK", thus, the
# itinerary must begin with "JFK". If there are multiple valid itineraries, you
# should return the itinerary that has the smallest lexical order when read as
# a single string.
# 
# 
# For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than
# ["JFK", "LGB"].
# 
# 
# You may assume all tickets form at least one valid itinerary. You must use
# all the tickets once and only once.
# 
# 
# Example 1:
# 
# 
# Input: tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
# Output: ["JFK","MUC","LHR","SFO","SJC"]
# 
# 
# Example 2:
# 
# 
# Input: tickets =
# [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
# Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
# Explanation: Another possible reconstruction is
# ["JFK","SFO","ATL","JFK","ATL","SFO"] but it is larger in lexical order.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= tickets.length <= 300
# tickets[i].length == 2
# fromi.length == 3
# toi.length == 3
# fromi and toi consist of uppercase English letters.
# fromi != toi
# 
# 
#

# @lc code=start
class Solution:
    def __init__(self):
        self.itineraries = []

    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        self.n = len(tickets)
        flights = self.constructFlights(tickets)

        self.dfs(flights, ["JFK"])

        self.itineraries.sort()
        return self.itineraries[0] if len(self.itineraries) > 0 else []

    def dfs(self, flights, itinerary ):
        if len(itinerary) == self.n + 1:
            self.itineraries.append(itinerary[:])
            return

        departure = itinerary[-1]
        if len(flights[departure]) == 0:
            # no more flight from this place
            return
        
        for dst in flights[departure]:

            itinerary.append(dst)
            flights[departure].remove(dst)
            if len(flights[departure]) == 0:
                del flights[departure]

            self.dfs(flights, itinerary)

            flights[departure].append(dst)
            flights[departure].sort()
            itinerary.pop()

    def constructFlights(self, tickets):
        flights = defaultdict(list)
        for src, dst in tickets:
            flights[src].append(dst)

        for src in flights:
            flights[src].sort()

        return flights
# @lc code=end

