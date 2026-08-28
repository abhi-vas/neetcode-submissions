class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        i=1
        k=1
        while k<len(nums):
            if nums[k]!=nums[k-1]:
                nums[i]=nums[k]
                i=i+1
            k=k+1
        return i
        






















        





        