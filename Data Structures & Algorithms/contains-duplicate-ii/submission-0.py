class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        for i in range(len(nums)):
            
            start = i+1 
            end= start+ k if start+k < len(nums) else len(nums)

            for j in range(start,end):
                if nums[i]==nums[j]:
                    return True
        return False

            


        