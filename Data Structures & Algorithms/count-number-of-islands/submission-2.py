class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        visit=set()
        res=0
        def bfs(r,c):
            q=collections.deque()
            visit.add((r,c))
            q.append((r,c))
            while q:
                row,col=q.popleft()
                directions=[[-1,0],[1,0],[0,1],[0,-1]]
                for dr,dc in directions:
                    r,c =row+dr,col+dc
                    if r>=0 and r<rows and c>=0 and c<cols and (r,c) not in visit and grid[r][c]=='1':
                        visit.add((r,c))
                        q.append((r,c))

        
        for r in range(rows):
            for c in range(cols):
                if (not ((r,c)  in visit)) and grid[r][c]=='1':
                    bfs(r,c)
                    res=res+1
        return res
        