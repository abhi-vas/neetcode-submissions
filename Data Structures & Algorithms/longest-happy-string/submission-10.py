class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        

        maxheap = [[cnt, ch] for cnt, ch in ((a, 'a'), (b, 'b'), (c, 'c')) if cnt > 0]
        heapq.heapify_max(maxheap)
        q=deque()
        res=[]
        time =0 

        while maxheap :
            time=time+1
            freq,ch=heapq.heappop_max(maxheap)
            if len(res)>=2 and res[-1]==ch and res[-2]==ch and freq>0:
                    q.append([freq,ch,time+1])   

            else:
                res.append(ch)
                freq=freq-1
                if freq>0:
                    heapq.heappush_max(maxheap,[freq,ch])
            if q and q[0][-1]<=time:
                freq,ch,_=q.popleft()
                heapq.heappush_max(maxheap,[freq,ch])
        return ''.join(res)

                

