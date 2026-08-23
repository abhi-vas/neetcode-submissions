class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        my_dict=defaultdict(int)
        for num in nums:
            my_dict[num]=1+my_dict[num ]
        maxi=float('-inf')
        index=-1
        for i,value in enumerate(my_dict.values()):
            if value>maxi:
                maxi=value
                index=i
        return list(my_dict.keys())[index]
                





        