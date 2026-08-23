class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict={}
        for i,str in enumerate(strs):
            a=sorted(str)
            atr=''.join(a)
            if atr in my_dict:

                my_dict[atr]=my_dict[atr]+[strs[i]]
            else:
                my_dict[atr]=[strs[i]]
        return list(my_dict.values())
            
            

        