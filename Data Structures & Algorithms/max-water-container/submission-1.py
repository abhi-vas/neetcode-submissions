class Solution:
    def maxArea(self, heights: List[int]) -> int:
     

        maxi=float('-inf')

        i=0
        r=len(heights)-1

        while i<r:
            value=(r-i)*min(heights[i],heights[r])
            if value> maxi:
                maxi=value
            if heights[i]<=heights[r]:
                i=i+1
            else:
                r=r-1

        return maxi
     


        


        
        