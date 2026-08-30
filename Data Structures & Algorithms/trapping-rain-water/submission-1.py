class Solution:
    def trap(self, height: List[int]) -> int:
        l_max=[0]*len(height)
        r_max=[0]*len(height)
        curr_max=0
        for i in range(1,len(height)):
            curr_max=max(curr_max,height[i-1])
            l_max[i]=curr_max
        
        curr_max=0

        for i in range(len(height)-2,-1,-1):
            curr_max=max(curr_max,height[i+1])
            r_max[i]=curr_max

        res=0

        for i in range(len(height)):
            y=min(l_max[i],r_max[i])-height[i]
            res+= y if y>0 else 0
        
        return res



            