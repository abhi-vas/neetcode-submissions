class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area=0

        path=set()

        rows=len(grid)
        cols=len(grid[0])

        def bfs(r,c):
            q=collections.deque()
            path.add((r,c))
            q.append((r,c))
            area=1
            while q:
                row,col=q.popleft()

                directions=[[-1,0],[1,0],[0,1],[0,-1]]

                for dr,dc in directions:
                    r,c=row+dr,col+dc
                    if r>=0 and r<rows and c>=0 and c<cols and (r,c) not in path and grid[r][c]==1:
                        area+=1
                        path.add((r,c))
                        q.append((r,c))
            return area

        for r in range(rows):
            for c in range(cols):
                if (r,c) not in path and grid[r][c]==1:
                    max_area=max(bfs(r,c),max_area)

        return max_area
