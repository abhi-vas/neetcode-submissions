class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        my_dict={}
        res,maxvalue=0,0
        for num in nums:
            my_dict[num]=1+my_dict.get(num,0)
            res= num if my_dict[num]>maxvalue else res
            maxvalue=max(my_dict[num],maxvalue)
        return res
        
                





        