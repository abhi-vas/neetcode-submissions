class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)>len(s):
            return ''
        s_dict=defaultdict(int)
        t_dict=defaultdict(int)
        for i in range(len(t)):
            t_dict[t[i]]+=1
        required=len(t_dict)
        l=0
        matches=0
        start=0
        min_length=float('inf')
        for r in range(len(s)):
            flag1=False
            if t_dict[s[r]]>s_dict[s[r]] and t_dict[s[r]]>0:
                flag1=True
            s_dict[s[r]]+=1
            if t_dict[s[r]]<=s_dict[s[r]] and t_dict[s[r]]>0 and flag1==True:
                matches+=1

            while matches==required and l < len(s):
                    if r-l+1<min_length:
                        min_length=r-l+1
                        start=l
                    flag2=False
                    if t_dict[s[l]]==s_dict[s[l]] and t_dict[s[l]]>0:
                        flag2=True
                    s_dict[s[l]]-=1
                    if flag2:
                        matches-=1
                    l=l+1
    
        return '' if min_length==float('inf') else s[start:start+min_length]