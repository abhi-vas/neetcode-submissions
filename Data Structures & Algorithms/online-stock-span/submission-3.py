class StockSpanner:

    def __init__(self):
        self.prices=[]
        self.stack=[]
        
        

    def next(self, price: int) -> int:
        
        self.prices.append(price)
        i=len(self.prices)-1
        if i>=0:
            self.stack.append(i)
        stack=self.stack.copy()
        index=i
        while stack and self.prices[i]>=self.prices[stack[-1]]:
            index=stack.pop()
        return (i+1-index)
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)