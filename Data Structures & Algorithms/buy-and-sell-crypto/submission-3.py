class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        maxp=0

        i=0
        r=1
        while r <len(prices):

            if prices[i] <prices[r]:
                maxp=max(maxp,prices[r]-prices[i])
            else :
                i=r
            r=r+1
        return maxp
        