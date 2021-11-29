#
# @lc app=leetcode id=721 lang=python3
#
# [721] Accounts Merge
#
# https://leetcode.com/problems/accounts-merge/description/
#
# algorithms
# Medium (53.29%)
# Likes:    3388
# Dislikes: 612
# Total Accepted:    198.3K
# Total Submissions: 363.1K
# Testcase Example:  '[["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]'
#
# Given a list of accounts where each element accounts[i] is a list of strings,
# where the first element accounts[i][0] is a name, and the rest of the
# elements are emails representing emails of the account.
# 
# Now, we would like to merge these accounts. Two accounts definitely belong to
# the same person if there is some common email to both accounts. Note that
# even if two accounts have the same name, they may belong to different people
# as people could have the same name. A person can have any number of accounts
# initially, but all of their accounts definitely have the same name.
# 
# After merging the accounts, return the accounts in the following format: the
# first element of each account is the name, and the rest of the elements are
# emails in sorted order. The accounts themselves can be returned in any
# order.
# 
# 
# Example 1:
# 
# 
# Input: accounts =
# [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
# Output:
# [["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
# Explanation:
# The first and second John's are the same person as they have the common email
# "johnsmith@mail.com".
# The third John and Mary are different people as none of their email addresses
# are used by other accounts.
# We could return these lists in any order, for example the answer [['Mary',
# 'mary@mail.com'], ['John', 'johnnybravo@mail.com'], 
# ['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']]
# would still be accepted.
# 
# 
# Example 2:
# 
# 
# Input: accounts =
# [["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]]
# Output:
# [["Ethan","Ethan0@m.co","Ethan4@m.co","Ethan5@m.co"],["Gabe","Gabe0@m.co","Gabe1@m.co","Gabe3@m.co"],["Hanzo","Hanzo0@m.co","Hanzo1@m.co","Hanzo3@m.co"],["Kevin","Kevin0@m.co","Kevin3@m.co","Kevin5@m.co"],["Fern","Fern0@m.co","Fern1@m.co","Fern5@m.co"]]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= accounts.length <= 1000
# 2 <= accounts[i].length <= 10
# 1 <= accounts[i][j] <= 30
# accounts[i][0] consists of English letters.
# accounts[i][j] (for j > 0) is a valid email.
# 
# 
#

# @lc code=start
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        merged = []

        if not accounts or len(accounts) == 0:
            return merged


        self.forward_index = self.create_forward_index(accounts)
        self.inverted_index = self.create_inverted_index(accounts)

        self.parents = {i : i for i in range(len(accounts)) if len(accounts[i]) >= 1}

        for email, people in self.inverted_index.items():
            if len(people) > 1:
                p1 = people[0]
                for i in range(1, len(people)):
                    self.connect(p1, people[i])

        curr = None
        for people, email in self.forward_index.items():
            if len(email) > 0:
                curr = []
                curr.append(accounts[people][0])
                curr.extend(sorted(list(set(email))))
                merged.append(curr)

        return merged


    def create_forward_index(self, accounts):
        forward_index = defaultdict(list)

        for idx, account in enumerate(accounts):
            forward_index[idx].extend(account[1:])

        return forward_index

    def create_inverted_index(self, accounts):
        inverted_index = defaultdict(list)
        for idx, account in enumerate(accounts):
            name = account[0]
            for email in account[1:]:
                inverted_index[email].append(idx)

        return inverted_index


    def connect(self, p1, p2):
        parent1 = self.find(p1)
        parent2 = self.find(p2)
        if parent2 != parent1:
            self.parents[parent1] = parent2
            self.forward_index[parent2].extend(self.forward_index[parent1])
            self.forward_index[parent1] = []


    def find(self, p):
        path = []
        while p != self.parents[p]:
            path.append(p)
            p = self.parents[p]

        for ppl in path:
            self.parents[ppl] = p

        return p
# @lc code=end

