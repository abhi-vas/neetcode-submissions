class Solution:
    def validPalindrome(self, s: str) -> bool:
        global i,r
        i=0
        r=len(s)-1
        
        def ispalindrome(s):
            
            global i,r
            
            while i<r:
                
                while i<r and not(s[i].isalnum()):
                    i=i+1
                
                while i<r and not(s[r].isalnum()):
                    r=r-1
                
                if s[i].lower()!=s[r].lower():
                    return False
                

                i,r=i+1,r-1
            return True
        
        
            
        if ispalindrome(s):
            return True
        i=i+1
        if ispalindrome(s):
            return True
        i=i-1
        r=r-1
        if ispalindrome(s):
            return True
            
        return False


       
        