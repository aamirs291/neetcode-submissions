class Twitter:

    def __init__(self):
        self.count = 0
        # self.followMap = {}
        # self.tweetMap = {}
        self.followMap = defaultdict(set)
        self.tweetMap = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        
        # self.tweetMap[userId] = self.tweetMap.get(userId, [])
        # self.tweetMap[userId].append([self.count, tweetId])
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -=1 #important

    def getNewsFeed(self, userId: int) -> List[int]:
        
        res = []
        min_heap = []

        # self.followMap[userId] = self.followMap.get(userId, set())
        # self.followMap[userId].add(userId) #this is important
        self.followMap[userId].add(userId)
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId]) - 1
                count, tweetId = self.tweetMap[followeeId][index] # this is the latest tweet for this followeeid

                heapq.heappush(min_heap, [count, tweetId, followeeId, index])
            
        while min_heap and len(res)<10:
            count, tweetId, followeeId, index = heapq.heappop(min_heap)
            res.append(tweetId)
                
            if index >=1:#why 0 ?
                count, tweetId = self.tweetMap[followeeId][index-1]
                heapq.heappush(min_heap, [count, tweetId, followeeId, index-1])

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        # self.followMap[followerId] = self.followMap.get(followerId, set())
        # self.followMap[followerId].add(followeeId)
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        
        if followeeId in self.followMap[followerId]:
            #self.followMap[followerId].remove(followeeId)
            self.followMap[followerId].remove(followeeId)
