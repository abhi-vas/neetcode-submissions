class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        rows = len(heights)
        cols = len(heights[0])

        visit_pac=set()
        visit_at =set()

        def dfs(r,c,visit,prev_height):
            if r<0 or r>=rows or c<0 or c>=cols or (r,c) in visit or prev_height>heights[r][c]:
                return
            visit.add((r,c))
            dfs(r+1,c,visit,heights[r][c])
            dfs(r-1,c,visit,heights[r][c])
            dfs(r,c-1,visit,heights[r][c])
            dfs(r,c+1,visit,heights[r][c])



        for c in range(cols):
            dfs(0,c,visit_pac,heights[0][c])
            dfs(rows-1,c,visit_at,heights[rows-1][c])

        for r in range(rows):
            dfs(r,0,visit_pac,heights[r][0])
            dfs(r,cols-1,visit_at,heights[r][cols-1])

        return list(visit_pac & visit_at)