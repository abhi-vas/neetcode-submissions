class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res=[]
        subset=[0]
        ch=[]
        def is_palindrome(word):
            i=0
            r=len(word)-1

            while i<=r:
                if word[i]!=word[r]:
                    return False
                i=i+1
                r=r-1

            return True
        


        def comb_dfs(i):

            if i==len(s):
                word=s[subset[-1]:]
                ch.append(word)
                if is_palindrome(word):
                    res.append(ch.copy())
                ch.pop()
                return
            word=s[subset[-1]:i]
            if  is_palindrome(word):
                ch.append(word)
                subset.append(i)
                comb_dfs(i+1)
                subset.pop()
                ch.pop()
            comb_dfs(i+1)
        
        comb_dfs(1)
        return res
