class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        currsum=0
        prefixsum={0:1}
        res=0
        
        for num in nums:
            currsum+=num
            prevsum=currsum-k
            if prevsum in prefixsum:
                res=res+ prefixsum[prevsum]
            if currsum in prefixsum:
                prefixsum[currsum]+=1
            else:
                prefixsum[currsum]=1
        return res


            
            
            
            

        