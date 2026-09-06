class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        def can_feasible(nums,m,k):
            no=1
            carr_sum=0

            for num in nums:
                carr_sum+=num
                if carr_sum>m:
                    no+=1
                    carr_sum=num
            return  no<=k



        l= max(nums)
        r=sum(nums)
        res=r
        while l<=r:
            m=(l+r)//2

            if can_feasible(nums,m,k):
                res=m
                r=m-1
            else:
                l=m+1
        return res