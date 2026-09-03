class FreqStack:

    def __init__(self):
        self.stack=[]
        self.my_dict={}
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.my_dict[val]=1+self.my_dict.get(val,0)        

    def pop(self) -> int:
        most_freq=max(list(self.my_dict.values()))
        most=[]
        for key , val in self.my_dict.items():
            if val==most_freq:
                most.append(key)
    
        
        for i in range(len(self.stack)-1,-1,-1):
            if self.stack[i] in most:
                break
        val= self.stack.pop(i)
        self.my_dict[val]=-1+self.my_dict.get(val,0)
        return val

        

        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()