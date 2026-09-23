class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        

        res=[]
        self.k=k
        subset=[]
        self.n=n
        def dfs(i):

            if i>self.n+1:
                return

            if len(subset)==self.k:
                res.append(subset.copy())
                return 

            subset.append(i)
            dfs(i+1)
            subset.pop()
            dfs(i+1)
        
        dfs(1)
        return res
