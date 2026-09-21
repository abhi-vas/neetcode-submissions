class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:

           
        trips.sort(key=lambda x: x[1])
        vacant_seat=capacity
        heap=[]
        distance=set()
        for trip in trips:
            if not (trip[1]  in distance):
                distance.add(trip[1])
            if not (trip[2]  in distance):
                distance.add(trip[2])
        distance=list(distance)
        distance.sort()
        i=0
        j=0
        while j<len(distance):
            dist=distance[j]
            while i<len(trips ) and dist>=trips[i][1]:
                vacant_seat-=trips[i][0]
                pass_,from_,to_=trips[i]
                heapq.heappush(heap,[to_,pass_])
                i=i+1   
            
            if heap:
                while heap and  dist >=heap[0][0] :
                    to_,pass_=heapq.heappop(heap)
                    vacant_seat+=pass_
            if vacant_seat<0:
                return False
            j=j+1
            
        
        return True




            

            
        
    


    
    