class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        
        min_length=float('inf')
        pre_sum=0
        flag=False
        l=0
        for r in range(len(nums)):
            pre_sum=pre_sum+nums[r]     
            
            while pre_sum>=target:
                min_length=min(min_length,r-l+1)
                pre_sum-=nums[l]
                l=l+1
         
         
                flag=True
        if flag:
            return min_length
        else:
            return 0



            
        