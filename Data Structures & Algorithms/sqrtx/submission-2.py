class Solution:
    def mySqrt(self, x: int) -> int:

        i=0
        r=x
        res=0


        while i<=r:
            m= (i+r)//2

            if m*m==x:
                return m
            elif m*m<x:
                i=m+1
                res=m
            else:
                r=m-1 
        return res    