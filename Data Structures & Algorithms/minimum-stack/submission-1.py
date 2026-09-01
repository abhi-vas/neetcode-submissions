class MinStack:

    def __init__(self):
        self.stack=[]
        self.min_=0
        

    def push(self, val: int) -> None:
        if self.stack==[]:
            self.min_=val
        self.stack.append(val)
        if val<self.min_:
            self.min_=val
        
        

    def pop(self) -> None:
        val= self.stack.pop()
        if self.stack!=[]:
            self.min_=min(self.stack)
        return val

        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_
        
