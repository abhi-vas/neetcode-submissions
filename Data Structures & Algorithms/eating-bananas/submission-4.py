class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        from math import ceil
        i=1
        r=max(piles)
        def time_calculator(piles,num):
            time=0
            for pile in piles:
                time=time+ceil(pile/num)
            return time
        res=0
        while i<=r:
            mid=(i+r)//2
            time=time_calculator(piles,mid)

            if time<=h:
                r=mid-1
                res=mid
            else:
                i=mid+1
        return res



        






        