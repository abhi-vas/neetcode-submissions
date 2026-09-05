class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        i = max(weights)
        r = sum(weights)

        def day_required(weights,weight):
            day=1
            weigh_track=0
            for w in weights:
                if weigh_track+w<=weight:
                    weigh_track+=w
                    
                else:
                    weigh_track=w
                    day=day+1
            return day
        res=r
        while i<=r:
            m=(i+r)//2
            day=day_required(weights,m)
            if day<=days:
                r=m-1
                res=m
            else:
                i=m+1
        return res


        