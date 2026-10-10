class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        if len(points)==0:
            return 0
        if len(points) == 1:
            return 0

        def prims(start):

            min_heap=[]
        
            visit = set()
            mst=0
            visit.add(start)

            for c in range(len(points)):
                if c== start:
                    continue
                weight = abs(points[start][0]-points[c][0]) + abs(points[start][1]-points[c][1])

                heapq.heappush(min_heap,(weight,start,c))

            while min_heap and len(visit) < len(points):
                w,u,v=heapq.heappop(min_heap)
                if v in visit:
                    continue
                visit.add(v)
                mst=mst+w
                for nei in range(len(points)):
                    if nei== v:
                        continue
                    weight = abs(points[v][0]-points[nei][0]) + abs(points[v][1]-points[nei][1])

                    heapq.heappush(min_heap,(weight,v,nei))
            return mst
        return prims(0)
        
        

    
        

        
        



     