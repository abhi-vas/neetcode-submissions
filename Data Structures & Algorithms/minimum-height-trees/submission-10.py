class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n==1:
            return [0]
        if n==2:
            return [0,1]

        graph=defaultdict(list)
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)

        leaves=[]
        for i in range(n):
            if len(graph[i])>1:
                leaves.append(i)


        def dfs(key,visit,value):
            if key in visit:
                return value
            visit.add(key)
            ans=float('-inf')
            for node in graph[key]:
                ans=max(ans,dfs(node,visit,1+value))
            return ans

        res=[]
        min_val=float('inf')
        for i in leaves:
            val=dfs(i,set(),0)
            min_val=min(min_val,val)
            res.append([val,i])

        result=[]
        for val,root in res:
            if val==min_val:

                result.append(root)
                
        return result


            