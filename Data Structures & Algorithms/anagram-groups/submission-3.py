class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict=defaultdict(list)
        for str in strs:
            count=[0]*26
            for s in str:
                count[ord(s)-ord('s')]+=1
    
   
            my_dict[tuple(count)].append(str)
            

        return list(my_dict.values())