class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        max_area=0

        path=set()

        rows=len(grid)
        cols=len(grid[0])

        def search(r,c):

            if r<0 or c<0 or r>=rows or c>=cols or (r,c)   in path or grid[r][c]==0:
                return 0

        
            path.add((r,c))
            return(1+search(r+1,c)+
                search(r-1,c)+
                search(r,c+1)+
                search(r,c-1))

        for r in range(rows):
            for c in range(cols):
                if (r,c) not in path and grid[r][c]==1:
                    max_area=max(search(r,c),max_area)

        return max_area

            