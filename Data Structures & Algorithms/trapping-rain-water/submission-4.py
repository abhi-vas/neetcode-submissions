class Solution:
    def trap(self, height: List[int]) -> int:

        max_l=0
        max_r=0

        l=0
        r=len(height)-1
        res=0
        while l<=r:

            if max_l <= max_r:
                y=max_l - height[l]
                res+=y if y >0 else 0
                max_l = max(max_l,height[l])
                l=l+1
            else:
                y=max_r-height[r]
                res+=y if y >0 else 0
                max_r=max(max_r,height[r])
                r=r-1
        return res


            
        