class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        length=len(nums)
        nums=set(nums)
        
        for sol in range(1,length+1):
            if sol not in nums:
                return sol
        return 1+length
      