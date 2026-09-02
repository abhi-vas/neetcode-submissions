class StockSpanner:

    def __init__(self):
        self.prices=[]
        self.stack=[]
        

    def next(self, price: int) -> int:
        stack=list(range(0,len(self.prices)))
        self.prices.append(price)
        i=len(self.prices)-1
        index=i
        while stack and self.prices[i]>=self.prices[stack[-1]]:
            index=stack.pop()
        return (i+1-index)
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)