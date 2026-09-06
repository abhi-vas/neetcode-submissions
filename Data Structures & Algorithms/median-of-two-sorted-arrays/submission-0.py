class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        l=len(nums1)+len(nums2)
        new_array=nums1+nums2
        new_array.sort()
        x=l//2

        if l%2==0:

            median=(new_array[x-1]+new_array[x])/2
            return median
        else :

            return new_array[x]
        