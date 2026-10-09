class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        graph=defaultdict(list)
        
        for u,v,t in times:
            graph[u-1].append((v-1,t))
        distance = [(float('inf'))]*n
        def djkstra():

            min_heap=[(0,k-1)]
            
        
            while min_heap:
                d, node = heapq.heappop(min_heap)

                if distance[node] < d:
                    continue

                for child , weight in graph[node]:

                    new_dist  = d + weight 
                  
                    if new_dist < distance[child]:
                        distance[child] = new_dist
                        heapq.heappush(min_heap,(new_dist,child))

        djkstra()
        min_dist=-1
        for i,dist in enumerate(distance):
            if i==k-1:
                continue
            if dist ==float('inf'):
                return -1
            min_dist = max(min_dist,dist)
        return min_dist
