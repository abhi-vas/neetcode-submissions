class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def mergeandsort(arr,l,r):
            m=(l+r)//2
            left=arr[l:m+1]
            right=arr[m+1:r+1]
            i,j,k=l,0,0
            while j<len(left) and k<len(right):
                if left[j]<=right[k]:
                    arr[i]=left[j]
                    j=j+1
                else:
                    arr[i]=right[k]
                    k=k+1
                i=i+1
            while j<len(left):
                arr[i]=left[j]
                j=j+1
                i=i+1
            while k<len(right):
                arr[i]=right[k]
                k=k+1
                i=i+1
            return arr


        def split(arr,l,r):
            if l==r:
                return arr
            m=(l+r)//2
            split(arr,l,m)
            split(arr,m+1,r)
            mergeandsort(arr,l,r)
            return arr
        split(nums,0,len(nums)-1)



        