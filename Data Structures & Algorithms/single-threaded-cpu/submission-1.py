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
                stack.append(heapq.heappop(tasks))
            if stack:
                stack.sort(key=lambda x : (x[1],x[-1]))
                time=time+stack[0][1]
                res.append(stack.pop(0)[-1])
            else:
                time=tasks[0][0]

        return res

















        
            

            