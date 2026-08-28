class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
         

        nums.sort()
        res=[]

        def twosum(nums,value,l,r,res):
            
            while l<r:

                currsum=nums[l]+nums[r]+value

                if currsum<0:
                    l=l+1
                elif currsum>0:
                    r=r-1

                elif currsum==0:
                    res.append([value,nums[l],nums[r]])
                    l=l+1
                    while l<r and nums[l-1]==nums[l]:
                        l=l+1
             
        i=0
        while i <len(nums):
            if i>0 and nums[i]==nums[i-1]:
                i=i+1
                continue
            l=i+1
            r=len(nums)-1
            twosum(nums,nums[i],l,r,res) 
            i=i+1
        return res

         