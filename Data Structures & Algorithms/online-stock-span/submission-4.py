class StockSpanner:


    def __init__(self):
        self.prices=[]
        self.stack=[]
        self.spans=[]
        
        

    def next(self, price: int) -> int:
           
        self.prices.append(price)
        i=len(self.prices)-1
        span=1
        while self.stack and self.prices[i]>=self.prices[self.stack[-1]]:
            index=self.stack.pop()
            span+=self.spans[index]
        self.stack.append(i)
        self.spans.append(span)
        return span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)