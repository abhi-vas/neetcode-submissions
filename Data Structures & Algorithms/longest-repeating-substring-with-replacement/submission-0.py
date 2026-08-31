class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        hash_map=defaultdict(int)
        L=0
        max_length=0
        
        
        for r in range(len(s)):
            hash_map[s[r]]=1+hash_map.get(s[r],0)
            
            if  (r-L+1)-max(hash_map.values())>k: 
                hash_map[s[L]]-=1
                L=L+1
            max_length=max(max_length,r-L+1)
        
            
                

          

                
        return max_length
                
            
            

        