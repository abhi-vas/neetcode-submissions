class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        class Trie:
            def __init__(self):
                self.children={}
                self.end=False
        root=Trie()
    
        def insert(root,word):
            curr=root
            for w in word:
                if w not in curr.children:
                    curr.children[w]=Trie()
                curr=curr.children[w]
            curr.end=True

        for word in words:
             insert(root,word)
        curr=root
        res=[]
        subset=[]
        rows = len(board)
        cols=  len(board[0])
        path=set()
        def search(r,c,curr):

            if curr.end:
                res.append(''.join(subset))
                curr.end=False
            if (r<0 or c < 0 or r>=rows or c>= cols) or (r,c) in path:
                    return 
            for key in curr.children:
                if   board[r][c] !=key :
                    continue
                path.add((r,c))
                subset.append(key)
                search(r+1,c,curr.children[key])
                search (r-1 ,c,curr.children[key])  
                search(r,c+1,curr.children[key]) 
                search(r,c-1,curr.children[key])
                subset.pop()
                path.remove((r,c))

    
    
        for r in range(rows):
            for c in range(cols):
               search(r,c,curr)
        return res     

