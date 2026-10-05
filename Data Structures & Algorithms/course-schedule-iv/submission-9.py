class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:

            graph=defaultdict(list)

            for parent,child in prerequisites:

                graph[child].append(parent)

            parents=defaultdict(set)

            visit=set()

            def dfs(key):

                if key   in visit:
                    return parents[key]

                visit.add(key)
                res=set()
                for parent in graph[key]:
                    pro= dfs(parent)
                    if pro:
                        res.update(pro)
        
                res.add(key)
                parents[key].update(res)

                
                return res


            for i in range(numCourses):
                dfs(i)


            res=[]

            for parent,child in queries:
                if parent in parents[child]:
                    res.append(True)
                else:
                    res.append(False)
            return res



        


    





        
       

