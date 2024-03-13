#
# @lc app=leetcode id=1311 lang=python3
#
# [1311] Get Watched Videos by Your Friends
#
# https://leetcode.com/problems/get-watched-videos-by-your-friends/description/
#
# algorithms
# Medium (46.45%)
# Likes:    372
# Dislikes: 412
# Total Accepted:    22.4K
# Total Submissions: 47.8K
# Testcase Example:  '[["A","B"],["C"],["B","C"],["D"]]\n[[1,2],[0,3],[0,3],[1,2]]\n0\n1'
#
# There are n people, each person has a unique id between 0 and n-1. Given the
# arrays watchedVideos and friends, where watchedVideos[i] and friends[i]
# contain the list of watched videos and the list of friends respectively for
# the person with id = i.
# 
# Level 1 of videos are all watched videos by your friends, level 2 of videos
# are all watched videos by the friends of your friends and so on. In general,
# the level k of videos are all watched videos by people with the shortest path
# exactly equal to k with you. Given your id and the level of videos, return
# the list of videos ordered by their frequencies (increasing). For videos with
# the same frequency order them alphabetically from least to greatest. 
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: watchedVideos = [["A","B"],["C"],["B","C"],["D"]], friends =
# [[1,2],[0,3],[0,3],[1,2]], id = 0, level = 1
# Output: ["B","C"] 
# Explanation: 
# You have id = 0 (green color in the figure) and your friends are (yellow
# color in the figure):
# Person with id = 1 -> watchedVideos = ["C"] 
# Person with id = 2 -> watchedVideos = ["B","C"] 
# The frequencies of watchedVideos by your friends are: 
# B -> 1 
# C -> 2
# 
# 
# Example 2:
# 
# 
# 
# 
# Input: watchedVideos = [["A","B"],["C"],["B","C"],["D"]], friends =
# [[1,2],[0,3],[0,3],[1,2]], id = 0, level = 2
# Output: ["D"]
# Explanation: 
# You have id = 0 (green color in the figure) and the only friend of your
# friends is the person with id = 3 (yellow color in the figure).
# 
# 
# 
# Constraints:
# 
# 
# n == watchedVideos.length == friends.length
# 2 <= n <= 100
# 1 <= watchedVideos[i].length <= 100
# 1 <= watchedVideos[i][j].length <= 8
# 0 <= friends[i].length < n
# 0 <= friends[i][j] < n
# 0 <= id < n
# 1 <= level < n
# if friends[i] contains j, then friends[j] contains i
# 
# 
#

# @lc code=start
from collections import deque, defaultdict
from heapq import heappush, heappop

class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], startIndex: int, level: int) -> List[str]:
        queue = deque([startIndex])
        visited = set([startIndex])
        curr_level = 0
        while queue:
            size = len(queue)
            if curr_level == level:
                break

            curr_level += 1
            for _ in range(size):
                person = queue.popleft()
                friend = friends[person]
                for f in friend:
                    if f not in visited:
                        queue.append(f)
                        visited.add(f)

        videos = []
        counts = defaultdict(int)
        for p in queue:
            watched_videos = watchedVideos[p]
            for video in watched_videos:
                counts[video] += 1

        for video in counts:
            heappush(videos, (counts[video], video))

        res = []
        while videos:
            count, video = heappop(videos)
            res.append(video)

        return res
# @lc code=end

