class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        visit=set()
        rows = len(grid)
        cols=len(grid[0])
        directions=[[-1,0],[1,0],[0,-1],[0,1]]
        def bfs():
            unrotten=0
            q=collections.deque()
            for r in range(rows):
                for c in range(cols):
                    if grid[r][c]==2:
                        visit.add((r,c))
                        q.append((r,c))
                    if grid[r][c]==1:
                        unrotten+=1

            time=0
            while q and unrotten>0:
                length=len(q)
                for _ in range(length):
                    row,col=q.popleft()
                    for dr,dc in directions:
                        r=row+dr
                        c=col+dc
                        
                        if r>=0 and r< rows and c>=0 and c< cols and (r,c) not in visit and grid[r][c]==1:
                            visit.add((r,c))
                            grid[r][c]=2
                            unrotten-=1
                            q.append((r,c))
                time+=1
            if unrotten==0:
                return time
            else:
                return -1
        return bfs()

