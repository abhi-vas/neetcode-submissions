class Solution:
    def maxProfit(self, prices: List[int]) -> int:
    
        r_max = prices[-1]
        profit = 0

        for i in range(len(prices) - 1, -1, -1):
            r_max = max(r_max, prices[i])
            profit = max(profit, r_max - prices[i])

        return profit
            