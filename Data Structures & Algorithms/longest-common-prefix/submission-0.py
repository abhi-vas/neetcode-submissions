class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        import numpy as np
        pre=''
        min_len=min(len(str ) for str in strs)
        for i in range(min_len):
            flag=True
            for str in strs:
                if str[i]!=strs[0][i]:
                    flag=False
                    return pre

            if flag:
                pre=pre+strs[0][i]
        return pre





        