class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        import gc
        s=list(s)
        t=list(t)
        s.sort()
        t.sort()
        gc.collect()
        if s==t:
            return True
        return False
        
        