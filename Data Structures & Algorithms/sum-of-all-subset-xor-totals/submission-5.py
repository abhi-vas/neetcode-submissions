class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:

        
        def xor(i,total):

            if i==len(nums):

                return total

            return xor(i+1,total ^ nums[i]) + xor(i+1,total)

        return xor(0,0)



            

        