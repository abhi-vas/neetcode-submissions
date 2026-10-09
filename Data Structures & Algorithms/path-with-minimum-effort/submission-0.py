from _heapq import heappop
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows=len(heights)
        cols=len(heights[0])
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        dist=[[float('inf') for _ in range(cols)] for _ in range(rows)]
        dist[0][0]=0
        def djkstra():
            
            min_heap=[(0,(0,0))]

            while min_heap:

                d ,(row,col) =heapq.heappop(min_heap)

                if dist[row][col] < d:
                    continue

                for dr,dc in directions:
                    r=row+dr
                    c=col+dc

                    if r>=0 and r<rows and c>=0 and c< cols:
                        new_dist = max(d, abs(heights[r][c] - heights[row][col]))

                        if new_dist < dist[r][c]:
                            dist[r][c]=new_dist
                            heapq.heappush(min_heap,(new_dist,(r,c)))
        djkstra()
        return dist[rows-1][cols-1]

