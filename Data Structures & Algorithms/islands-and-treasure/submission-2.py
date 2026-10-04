class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        
        rows = len(grid)
        cols = len(grid[0])

        visit = set()
        directions=[[-1,0],[1,0],[0,1],[0,-1]]
        def bfs():
            q=collections.deque()
            for r in range(rows):
                for c in range(cols):
                    if grid[r][c]==0:
                        visit.add((r,c))
                        q.append((r,c))
            dist=0
            while q :
                length = len(q)
                for i in range(length):
                    row,col=q.popleft()
                    grid[row][col]=dist

                    for dr,dc in directions:
                        r=row+dr
                        c=col+dc
                        if r>=0 and r< rows and c>=0 and c<cols and (r,c) not in visit and grid[r][c]!=-1:
                            visit.add((r,c))
                            q.append((r,c))
                dist+=1
        bfs()
                    
            

