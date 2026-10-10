class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        dist = [[float('inf') for _ in range(cols)] for _ in range(rows)]
        dist[0][0]=grid[0][0]
        dir_=[[-1,0],[1,0],[0,1],[0,-1]]
        visit=set()
        start=(0,0)
        goal=(rows-1,cols-1)

        min_heap=[(grid[0][0],0,0)]

        while min_heap:

            curr_max,row,col =heapq.heappop(min_heap)
            visit.add((row,col))
            if (row,col) ==(rows-1,cols-1):
                return curr_max

            for dr,dc in dir_:
                r=row+dr
                c=col+dc
                if r<0 or c<0 or r==rows or c==cols or (r,c) in visit:
                    continue

                min_dist = max(curr_max, grid[r][c])
                if min_dist < dist[r][c]:
                    dist[r][c]=min_dist
                    heapq.heappush(min_heap,(min_dist,r,c))
        return -1
        
            


             





             