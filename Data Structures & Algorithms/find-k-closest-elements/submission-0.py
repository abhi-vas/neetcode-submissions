class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        nums=[0]*len(arr)
        for i in range(len(arr)):
            nums[i]=abs(arr[i]-x)
        
        min_,index=float('inf'),-1

        for i in range(len(arr)):
            if nums[i]<min_:
                min_=nums[i]
                index=i

        i=index
        r=index

        while r-i+1<k:
            if i==0:
                r=r+1
            elif r==len(nums)-1:
                i=i-1
            elif nums[i-1]<=nums[r+1]:
                i=i-1
            else:
                r=r+1
           


        return arr[i:r+1]



