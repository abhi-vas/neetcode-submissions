class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        L=0
        R=len(nums)-1
        i=0
    
    
        while i<=R:
            if nums[i]==0:
                nums[i],nums[L]=nums[L],nums[i]
                L=L+1
        
            if nums[i]==2:
                nums[i],nums[R]=nums[R],nums[i]
                R=R-1
                i=i-1
            i=i+1

            

            

      



        