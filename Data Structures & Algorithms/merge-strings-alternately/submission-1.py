class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        
        l=0
        m=0
        k=0
        res=''

        while l<len(word1) and m<len(word2):
            if k==0:
                res=res+word1[l]
                k=1
                l=l+1
            if k==1:
                res=res+word2[m]
                k=0
                m=m+1
        
        while l<len(word1):
            res=res+word1[l]
            l=l+1
        
        while m<len(word2):
            res=res+word2[m]
            m=m+1
        return res


             

        
        
        