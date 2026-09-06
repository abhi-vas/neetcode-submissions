class Solution:
    def search(self, nums: List[int], target: int) -> int:

        

        def min_index_func(nums):
            l=0
            r=len(nums)-1

            while l<r:
                m=(l+r)//2

                if nums[m]>nums[r]:

                    l=m+1
                else:
                    r=m
            return l

        def find_index(nums,l,r,target):

            while l<=r:
                m=(l+r)//2
                if nums[m]==target:
                    return m
                elif nums[m]>target:
                    r=m-1
                else:
                    l=m+1
            return -1


        min_id=min_index_func(nums)
        l=0
        r=len(nums)-1
        if nums[min_id]<=target<=nums[r]:
            return find_index(nums,min_id,r,target)
        else:
            return find_index(nums,0,min_id-1,target)








        