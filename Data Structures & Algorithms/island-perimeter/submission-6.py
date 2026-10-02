class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        

        path=set()
        rows=len(grid)
        cols=len(grid[0])

        def search(r,c):

            if r<0 or c<0 or r>=rows or c>=cols or grid[r][c] ==0 :
                return 1
            
            if (r,c) in path:
                return 0
            path.add((r,c))
            return (search(r+1,c)+
                    search(r-1,c)+
                    search(r,c+1)+
                    search(r,c-1))
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    return search(r,c)
                    
                
    

    

        
        



    