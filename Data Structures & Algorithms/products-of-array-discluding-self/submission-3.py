class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefix=[1]*len(nums)
        postfix=[1]*len(nums)
        for i in range(len(nums)):
            j=len(nums)-1-i
            if i!=0:
                prefix[i]=nums[i-1]*prefix[i-1]
                postfix[j]=nums[j+1]*postfix[j+1]
            
        
        for i in range(len(nums)):
            nums[i]=prefix[i]*postfix[i]
        return nums
        
        
        
        
        