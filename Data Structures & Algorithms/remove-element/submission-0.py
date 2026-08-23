class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k=0
        for i,num in enumerate(nums):
            if num==val:
                nums[i]=float('inf')
                k=k+1
        nums.sort()
        return len(nums)-k


        