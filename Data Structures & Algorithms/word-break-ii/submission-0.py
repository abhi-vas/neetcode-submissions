class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
    
        space=[0]
        res=[]
        subset=[]

        def back_track(i):

            if i ==len(s):
                lst=s[space[-1]:]
                if lst in wordDict:
                    subset.append(lst)
                    res.append(' '.join(subset))
                    subset.pop()
                return

            lst=s[space[-1]:i]
            if lst in wordDict:
                subset.append(lst)
                space.append(i)
                back_track(i+1)
                subset.pop()
                space.pop()
            back_track(i+1)
        back_track(0)
        return res