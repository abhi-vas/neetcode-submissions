class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        def nearest_binary(nums,target):
            l=0
            r=len(nums)-1

            while l<=r:
                mid=(l+r)//2
                if nums[mid]>target:
                    r=mid-1
                elif nums[mid]<target:
                    l=mid+1
                else:
                    return mid
            if l==len(nums):
                return r
            if r==-1:
                return l
            if abs(nums[l]-target)<abs(nums[r]-target):
                return l
            else:
                return r
        index=nearest_binary(arr,x)
        i=index
        r=index

        while r-i+1<k:
            if i==0:
                r=r+1
            elif r==len(arr)-1:
                i=i-1
            elif abs(arr[i-1]-x)<=abs(arr[r+1]-x):
                i=i-1
            else:
                r=r+1
           


        return arr[i:r+1]



