class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        connected=0

        visit=set()

        graph=defaultdict(list)
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
    

        def dfs(node):

            if node in visit:
                return

            visit.add(node)

            for key in graph[node]:
                dfs(key)

        for node in range(n):
            if node not in visit:
                dfs(node)
                connected+=1
        return connected


