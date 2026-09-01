class MinStack:

    def __init__(self):
        self.stack=[]
        self.min_=[]
        

    def push(self, val: int) -> None:
        if self.stack==[]:
            self.min_.append(val)
        self.stack.append(val)
        if val<=self.min_[-1]:
            self.min_.append(val)
        
        

    def pop(self) -> None:
        val= self.stack.pop()
        if self.min_[-1]==val:
            self.min_.pop()
        
        return val

        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_[-1]
        
