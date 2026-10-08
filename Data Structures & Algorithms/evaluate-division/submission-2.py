class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        graph={}

        for i in range(len(values)):
            a,b= equations[i]
            value =values[i]
            if a in graph:
                graph[a].append([b,value])
            else:
                graph[a]=[]
                graph[a].append([b,value])
            if b in graph:
                graph[b].append([a,1/value])
            else:
                graph[b]=[]
                graph[b].append([a,1/value])
    
        def dfs(key,goal,visit,value):
            if key == goal:
                return value
            
            visit.add(key)
            for node,val in graph[key]:
                if node not in visit:
                    res=dfs(node,goal,visit,val*value)
                    if res!=-1:
                        return res
            return -1


            
        result=[]
        for key,goal in queries:
            if key in graph and goal in graph:
                result.append(dfs(key,goal,set(),1))
            else:
                result.append(-1)
        return result
                    


