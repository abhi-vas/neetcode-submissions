class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        hash_set=set(nums)
        sol_len=list(range(1,len(nums)+1)) 
        for sol in sol_len:
            if sol not in hash_set:
                return sol
        return 1+len(nums)
      