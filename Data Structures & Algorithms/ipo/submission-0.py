class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:

        maxheap=[]

        minheap=[[c,p]  for c,p in zip(capital,profits)]

        heapq.heapify(minheap)
        profit=0
        while k>0:

            while minheap and w>=minheap[0][0]:
                _,p=heapq.heappop(minheap)
                heapq.heappush_max(maxheap,p)

            if maxheap:
                ps=heapq.heappop_max(maxheap)
                profit=profit+ps
                w=w+ps
                k=k-1
            else:
                break

        return w


        
        
        
        
            





    

        
        

        




        
        