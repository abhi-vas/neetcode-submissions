class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        my_dict={}
        for num in nums:
            my_dict[num]=1+my_dict.get(num,0)
        
        
        count=[[] for _ in range(len(nums)+1)]
        for c,n in my_dict.items():
            count[n].append(c)
        res=[]
        for c in range(len(count)-1,0,-1):
            for item in count[c]:
                res.append(item)
                if len(res)==k:
                    return res




        



    
        