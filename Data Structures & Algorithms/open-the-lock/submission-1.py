class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        visit =set()
        
        if "0000" in deadends:            
            return -1
        
        def bfs():
            q=collections.deque()
            q.append([0,0,0,0])
            visit.add(('0000'))
    
            iteration=0
            while q:

                for _ in range(len(q)):
                    val=q.popleft()
                    if ''.join(map(str, val))==target:
                            return iteration
                    for i in range(4):
                        copy=val.copy()
                        if val[i]<=8:
                            copy[i]=copy[i]+1
                        else:
                            copy[i]=0
                        
                        if ''.join(map(str, copy)) not in deadends and ''.join(map(str, copy)) not in visit:
                            visit.add(''.join(map(str, copy)))
                            q.append(copy)
                    for i in range(4):
                        copy=val.copy()
                        if val[i]>0:
                            copy[i]=copy[i]-1
                        else:
                            copy[i]=9
                        
                        if ''.join(map(str, copy)) not in deadends and ''.join(map(str, copy)) not in visit:
                            visit.add(''.join(map(str, copy)))
                            q.append(copy)
                iteration+=1
            return -1
        return bfs()


                




