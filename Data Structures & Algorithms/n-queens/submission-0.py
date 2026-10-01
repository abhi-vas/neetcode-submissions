class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res=[]
        subset=[['.' for _ in range(n)] for _ in range(n)]
        col=set()
        pos_diag=set()
        neg_diag=set()

        def place(r):

            if r==n:
                copy=[''.join(row) for row in subset]
                res.append(copy)
                return 
            for c in range(n):

                if c in col or (r+c) in pos_diag or (r-c) in neg_diag:
                    continue
                col.add(c)
                pos_diag.add(r+c)
                neg_diag.add(r-c)
                subset[r][c] ='Q'
                place(r+1)
                col.remove(c)
                pos_diag.remove(r+c)
                neg_diag.remove(r-c)
                subset[r][c] ='.'
        place(0)
        return res

            

            