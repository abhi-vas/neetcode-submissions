class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        res=[]
        graph=defaultdict(list)
        tickets.sort(reverse =True)
        for a,b  in tickets:
            graph[a].append(b)
        def dfs(airport):
            while graph[airport]:
                next_airport =graph[airport].pop()
                dfs(next_airport)
            res.append(airport)
           
        dfs('JFK')
        return res[::-1]


             

                

