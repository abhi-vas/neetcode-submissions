class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        my_dict={}
        for num in nums:
            my_dict[num]=1+my_dict.get(num,0)
        
        
        my_dict_list=list(my_dict.items())
        my_dict_list=sorted(my_dict_list,key=lambda x:x[-1],reverse=True)
        res=[]
        for i in range(k):
            res.append(my_dict_list[i][0])
        return res




        



    
        