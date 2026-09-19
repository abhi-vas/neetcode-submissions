class Twitter:

    def __init__(self):
        self.time=0
        self.my_tweet=defaultdict(list)
        self.my_follow=defaultdict(set)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time=self.time-1
        self.my_tweet[userId].append([self.time,tweetId])
        

    def getNewsFeed(self, userId: int) -> List[int]:
    
        res=[]
        minheap=[]
        self.my_follow[userId].add(userId)
        for follow in self.my_follow[userId]:
            index=len(self.my_tweet[follow])-1
            if index>=0:
                time,tweetId=self.my_tweet[follow][index]
                minheap.append([time,tweetId,follow,index-1])
        heapq.heapify(minheap)

        while minheap and len(res)<10:
            time,tweetId,follow,index=heapq.heappop(minheap)
            res.append(tweetId)
            
            if index>=0:
                time,tweetId=self.my_tweet[follow][index]
                heapq.heappush(minheap,[time,tweetId,follow,index-1])
        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.my_follow[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.my_follow:
            if followeeId in self.my_follow[followerId]:
                self.my_follow[followerId].remove(followeeId)
            
