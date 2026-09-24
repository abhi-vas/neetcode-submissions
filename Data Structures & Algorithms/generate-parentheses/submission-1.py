class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res=[]

        subset=[]
        count={'(':0,')':0}
        nums=['(',')']
        def dfs(n):
            if len(subset)==2*n :
                res.append(''.join(subset.copy()))
                return 
           
            for num in nums:
                if (num=='(' and count[num]<n ) or (num==')' and count[')']<count['(']):
                    subset.append(num)
                    count[num]+=1
                    dfs(n)
                    subset.pop()
                    count[num]-=1
        dfs(n)
        return res


