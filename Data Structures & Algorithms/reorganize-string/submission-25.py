class Solution:
    def reorganizeString(self, s: str) -> str:

        my_dict=Counter(s)
        lists=[]
        
        for val,key in my_dict.items():
            lists.append([key,val])
        
        q=deque()

        res=[]
    
        time=0
        while lists or q :
            time=time+1
            if lists:
                freq,ch=heapq._heappop_max(lists)
                if res and res[-1]==ch:
                    res=[]
                    break
                res.append(ch)
                freq=freq-1
         
                if freq>0:
                    q.append([freq,ch,time+1])
                
            if q and q[0][-1]==time:
                freq,ch,_=q.popleft()
                heapq._heappush_max(lists,[freq,ch])

             
        return ''.join(res)


            

                    

                


