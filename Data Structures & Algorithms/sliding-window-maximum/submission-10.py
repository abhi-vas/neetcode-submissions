class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        l=0
        r=0
        q=[]
        output=[]

        while r<len(nums):

            while q and nums[r]>nums[q[-1]]:
                q.pop(-1)
            
            q.append(r)

            if l>q[0]:
                q.pop(0)

            if r-l+1>=k:
                output.append(nums[q[0]])
                l=l+1
            r=r+1
        return output

        
        
        

            
                    
            
        