class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        i=0
        

        while i<len(nums):
            k=i
            while k<len(nums)-1   and nums[k]==nums[k+1]:
                nums.remove(nums[k])
                
                
            i=k+1
        k=len(nums)
        return k
            




















        





        