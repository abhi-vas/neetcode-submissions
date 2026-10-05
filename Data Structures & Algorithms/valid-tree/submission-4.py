class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n==1:
            return True
        if len(edges) != n-1:
            return False
        graph=defaultdict(list)
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visit=set()
        stack=[edges[0][0]]
        visit.add(edges[0][0])

        def dfs():

            while stack:

                curr_node=stack.pop()

                for node in graph[curr_node]:

                    if node not in visit:
                        stack.append(node)
                        visit.add(node)
        dfs()

        return n==len(visit)








        
        