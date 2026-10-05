class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graph=defaultdict(list)
        indegree=defaultdict(int)
        for a,b in prerequisites:
            graph[b].append(a)
            indegree[a]+=1
        q=collections.deque()
        for i in range(numCourses):
            if i not in indegree:
                indegree[i]=0

        for key,val in indegree.items():
            if val==0:
                q.append(key)
        count=0
        while q:
            for _ in range(len(q)):
                val=q.popleft()
                count+=1
                for key in graph[val]:
                    indegree[key]-=1
                    if indegree[key]==0:
                        q.append(key)
        
        return count==numCourses    



    


        