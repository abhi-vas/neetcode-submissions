class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        r_max=prices[-1]
        
        r_list=[0]*len(prices)

        for r in range(len(prices)-1,-1,-1):
            r_max=max(prices[r],r_max)
            r_list[r]=r_max
        profit=0
        for i in range(len(prices)):

            profit = max (profit, r_list[i]-prices[i])
        
        return profit



       
        