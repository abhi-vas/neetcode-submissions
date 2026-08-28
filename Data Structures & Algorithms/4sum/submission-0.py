class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
      
        res=[]
        nums.sort()

        def twosum(nums,value1,value2,l,r,res,target):

            while l<r:

                if value1 + value2 + nums[l] +nums[r] >target:
                    r=r-1
                
                elif value1 + value2 + nums[l] +nums[r] <target:
                    l=l+1
                
                else:
                
                    res.append([value1 , value2 , nums[l] ,nums[r]])
                    l=l+1

                    while l<r and nums[l]==nums[l-1]:
                        l=l+1
        

        def threesum(nums,value1,res,target,m):

            for i,k in enumerate(range(m,len(nums))): 
                value2=nums[k]
                if i>0 and value2==nums[k-1]:
                    continue
                
                l=k+1
                r=len(nums)-1
                

                twosum(nums,value1,value2,l,r,res,target)
        

        for i ,value1 in enumerate(nums):
            if i>0 and value1==nums[i-1]:
                    continue
            
            
            threesum(nums,value1,res,target,i+1)
        return res

            



                




        