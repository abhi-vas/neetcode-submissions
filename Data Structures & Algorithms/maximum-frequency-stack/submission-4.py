class FreqStack:

    def __init__(self):
        self.freq={}
        self.group={}
        self.maxcount=0
        

    def push(self, val: int) -> None:
        self.freq[val]=1+self.freq.get(val,0)
        freq=self.freq[val]
        self.group[freq]=self.group.get(freq,[])+[val]
        if freq>self.maxcount:
            self.maxcount=freq


    def pop(self) -> int:
        val= self.group[self.maxcount].pop()
        if not self.group[self.maxcount]:
            self.maxcount-=1
        if self.freq[val]>1:
            self.freq[val]=-1+self.freq.get(val,0)
        else:
            self.freq[val]=0
        return val

        

        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()