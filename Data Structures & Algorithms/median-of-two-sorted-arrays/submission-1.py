class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        l1=len(nums1) + len(nums2)
        l=l1//2+1

        nums3=[0]*l

        a,b,c=0,0,0

        while a<len(nums1)  and b<len(nums2) and c<l:
            if nums1[a]<nums2[b]:
                nums3[c]=nums1[a]
                a=a+1
            else:
                nums3[c]=nums2[b]
                b=b+1
            c=c+1
        while a<len(nums1)  and c<l:
            nums3[c]=nums1[a]
            a=a+1
            c=c+1
        while  b<len(nums2) and c<l:
            nums3[c]=nums2[b]
            b=b+1
            c=c+1
        if l1%2==0:
            return (nums3[l1//2-1]+nums3[l1//2])/2
        else:
            return nums3[l1//2]
        
        
        