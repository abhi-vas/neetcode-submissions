class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        max_length=0
        hash_set=set()
        l=0
        length=0

        for r in range(len(s)):

            while  s[r] in hash_set:
                
                hash_set.remove(s[l])
                l=l+1
                length=length-1

            
            hash_set.add(s[r])
            length=length+1
            max_length=max(max_length,length)

        return max_length
        

        