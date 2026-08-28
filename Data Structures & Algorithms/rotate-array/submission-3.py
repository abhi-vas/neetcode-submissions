class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k=k%len(nums)

        def reverse(nums,l,r):

            while l<r:
                nums[l],nums[r]=nums[r],nums[l]
                l=l+1
                r=r-1


        l,r=0,len(nums)-1
        reverse(nums,l,r)

        l,r=0,k-1

        reverse(nums,l,r)

        l,r=k,len(nums)-1
        reverse(nums,l,r)