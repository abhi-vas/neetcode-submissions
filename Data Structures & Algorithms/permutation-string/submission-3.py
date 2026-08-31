class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2)<len(s1):
            return False
        dict_s1=defaultdict(int)
        dict_s2=defaultdict(int)

        for i in range(len(s1)):
            dict_s1[s1[i]]+=1
            dict_s2[s2[i]]+=1
        matches=0
        for i in range(26):
            al_=chr(ord('a')+i)
            if dict_s1.get(al_,0)==dict_s2.get(al_,0):
                matches+=1
        l=0
        for r in range(len(s1),len(s2)):
            if matches==26:
                return True
            dict_s2[s2[r]]+=1
            if dict_s2[s2[r]]==dict_s1[s2[r]]:
                matches+=1
            elif dict_s2[s2[r]]==dict_s1[s2[r]]+1:
                matches-=1
            dict_s2[s2[l]]-=1
            if dict_s2[s2[l]]==dict_s1[s2[l]]:
                matches+=1
            elif dict_s2[s2[l]]==dict_s1[s2[l]]-1:
                matches-=1
            l=l+1
        return matches==26



      
        





        

        


        