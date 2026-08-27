class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        length=len(nums)
        for i in range(length):
            if nums[i]<0:
                nums[i]=0
        
        for i in range(length):
            val=abs(nums[i])
            if 1<=val<=length:
                if nums[val-1]==0:
                    nums[val-1]=-(1+length)
                elif nums[val-1]>0:
                    nums[val-1]=-1*nums[val-1]
        for i in range(length):

            if nums[i]>=0:
                return i+1
        return 1+length


            