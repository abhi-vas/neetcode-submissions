class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        my_dict=defaultdict(int)
        for num in nums:
            my_dict[num]=my_dict[num]+1
        no_zeros=my_dict.get(0,0)
        no_ones=my_dict.get(1,0)
        no_tows=my_dict.get(2,0)
        if no_zeros>0:
            nums[0:no_zeros]=[0]*no_zeros
        if no_ones>0:
            nums[no_zeros:no_zeros+no_ones]=[1]*no_ones
        if no_tows>0:
            nums[no_zeros+no_ones:no_zeros+no_ones+no_tows]=[2]*no_tows

            

      



        