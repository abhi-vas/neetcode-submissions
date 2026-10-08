class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        graph=defaultdict(list)
        def diffrence(a,b):
            diff=0
            for i,j in zip(a,b):
                if i!=j:
                    diff+=1
            return diff==1
        if endWord not in wordList:
            return 0    

        for i in range(len(wordList)):
            for j in range(i+1,len(wordList)):
                if diffrence(wordList[i],wordList[j]):
                    graph[wordList[i]].append(wordList[j])
                    graph[wordList[j]].append(wordList[i])

        for word in wordList:
          
                
            if diffrence(beginWord,word):
                graph[word].append(beginWord)
                graph[beginWord].append(word)
            
        


        visit=set()
        def bfs(key,goal):
            q=collections.deque()
            q.append([key,0])
            visit.add(key)
            while q:
                key,val=q.popleft()
                if key ==goal:
                    return val+1
                for node in graph[key]:
                    if node not in visit:
                        visit.add(node)
                        q.append([node,val+1])
            return 0
            


        return bfs(beginWord,endWord)
            
            