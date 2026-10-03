class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        path=set()
        res=0
        def search(r,c):

            if r<0 or c<0 or r>=rows or c>=cols or (r,c) in path or grid[r][c] =='0' :
                return 

            path.add((r,c))

            search(r+1,c)
            search(r-1,c)
            search(r,c-1)
            search(r,c+1)
        
        for r in range(rows):
            for c in range(cols):
                if (not ((r,c)  in path)) and grid[r][c]=='1':
                    search(r,c)
                    res=res+1
        return res
        