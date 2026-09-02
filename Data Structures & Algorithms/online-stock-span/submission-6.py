class StockSpanner:

    def __init__(self):
        self.prices=[]
        self.stack=[]
        self.span=[]
        
        

    def next(self, price: int) -> int:
           
        self.prices.append(price)
        i=len(self.prices)-1
        index=-1
        while self.stack and self.prices[i]>=self.prices[self.stack[-1]]:
            index=self.stack.pop()

        self.span.append((self.span[index] + (i-index)) if index > -1 else 1)
        self.stack.append(i)
        return self.span[i]
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)