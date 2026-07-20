class Twitter:

    def __init__(self):
        self.time = 0
        self.tweetMap = defaultdict(list)
        self.followMap = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time -= 1
        self.tweetMap[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        result = []
        users = self.followMap[userId] | {userId}

        heap = []
        for user in users:
            tweets = self.tweetMap[user]
            if tweets:
                index = len(tweets) - 1
                time, tweetId = tweets[index]
                heapq.heappush(heap, (time, tweetId, user, index))

        while len(result) < 10 and heap:
            time, tweetId, user, index = heapq.heappop(heap)
            result.append(tweetId)
            if index > 0:
                time, tweetId = self.tweetMap[user][index - 1]
                heapq.heappush(heap, (time, tweetId, user, index - 1))

        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].discard(followeeId)
