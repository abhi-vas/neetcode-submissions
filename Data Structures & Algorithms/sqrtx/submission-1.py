class Solution:
    def mySqrt(self, x: int) -> int:

        i=1
        r=x

        while i<=r:
            m= (i+r)//2

            if m*m==x:
                return m
            elif m*m<x:
                i=m+1
            else:
                r=m-1 
        return r     