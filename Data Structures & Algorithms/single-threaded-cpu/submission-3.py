class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        
        for i in range(len(tasks)):
            tasks[i].append(i)
    
        heapq.heapify(tasks)
        time=tasks[0][0]
        stack=[]
        res=[]

        while tasks or stack:
            while tasks and tasks[0][0] <=time:
                _,proecesstime,index=heapq.heappop(tasks)
                stack.append([proecesstime,index])
            if stack:
                heapq.heapify(stack)
                time=time+stack[0][0]
                res.append(heapq.heappop(stack)[-1])
            else:
                time=tasks[0][0]

        return res

















        
            

            