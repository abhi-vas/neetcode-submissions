class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        pre=''
        
        for i in range(len(strs[0])):
            flag=True
            for str in strs:
                if  i==len(str) or str[i]!=strs[0][i]:
                    return pre
            pre=pre+strs[0][i]
        return pre





        