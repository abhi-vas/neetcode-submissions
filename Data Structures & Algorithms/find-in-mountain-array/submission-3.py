class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:

        l=0
        r=mountainArr.length() -1


        while l<r:


            m=(l+r)//2

            if mountainArr.get(m) < mountainArr.get(m+1):
                l=m+1

            else:
                r=m
        peak = r

        l=0
        r=peak
        while l<=r:
            m=(l+r)//2

            if  mountainArr.get(m)==target:
                return m

            elif mountainArr.get(m)<target :
                l=m+1
            else:
                r=m-1
        l=peak
        r=mountainArr.length() -1

        while l<=r:
            m=(l+r)//2

            if  mountainArr.get(m)==target:
                return m

            elif mountainArr.get(m)<target :
                r=m-1
            else:
                l=m+1

        return -1

        

        

        

        
        