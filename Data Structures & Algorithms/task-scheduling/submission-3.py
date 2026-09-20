class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        count=Counter(tasks)
        maxheap=list(count.values())
        heapq._heapify_max(maxheap)
        q=deque()
        
        time=0

        while maxheap or q:
            time=time+1

            if maxheap:
                cnt=heapq._heappop_max(maxheap) -1
                if cnt>0:
                    q.append([cnt,time+n])

            if q and q[0][1]<=time:
                heapq._heappush_max(maxheap,q.popleft()[0])

        return time
