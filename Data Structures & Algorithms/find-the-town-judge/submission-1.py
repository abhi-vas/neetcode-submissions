class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        
        graph=[[0 for i in range(n)] for i in range(n)]

        graph_t=[[0 for i in range(n)] for i in range(n)]
        

        for a_i,b_i in trust:
            graph[a_i-1][b_i-1]=1
            graph_t[b_i-1][a_i-1]=1

        for i in range(len(graph)):
            if graph[i]==[0]*n:
                if graph_t[i][i]==0 and all(graph_t[i][j] for j in range(n) if j!=i):
                    return i+1
        return -1
        
        







