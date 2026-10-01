class Trie:
    def __init__(self):
        self.children={}
        self.end=False
    
class WordDictionary:

    def __init__(self):
        self.root=Trie()
        

    def addWord(self, word: str) -> None:
        curr=self.root

        for w in word:
            if w not in curr.children:
                curr.children[w]=Trie()
            curr=curr.children[w]
        curr.end=True
    
        

    def search(self, word: str) -> bool:

        
        
        def search(curr,i):
            if i==len(word):
                return curr.end
            w=word[i]

            if w=='.':
                for key in curr.children:
                    if search(curr.children[key],i+1):
                        return True
            if w not in curr.children:
                return False
            return search(curr.children[w],i+1)
        return search(self.root,0)



