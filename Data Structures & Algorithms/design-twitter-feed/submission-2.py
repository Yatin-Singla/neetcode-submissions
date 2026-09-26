from collections import defaultdict
class Twitter:
    def __init__(self):
        self.counter = 1
        # userID: [(time, tweet)]
        self.tweets = defaultdict(list)
        # user with "userID": follows [users]
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.counter, tweetId))
        self.counter += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        def buildHeap(user):
            for time, tweet in self.tweets[user]:
                if len(heap) >= 10:
                    heapq.heappushpop(heap, (time, tweet))
                else:
                    heapq.heappush(heap, (time, tweet))

        #get all tweets from following
        for user in self.following[userId]:
            buildHeap(user)

        # get all personal tweets
        buildHeap(userId)

        output = []
        while heap:
            _, tweet = heapq.heappop(heap)
            output.append(tweet)

        return output[::-1]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
        
