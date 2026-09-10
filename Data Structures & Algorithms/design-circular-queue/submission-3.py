class Node:

    def __init__(self,value=0,nexti=None,prev=None):

        self.value=value
        self.nxt=nexti
        self.prev=prev

class MyCircularQueue:

    def __init__(self, k: int):

        self.left= Node(0)
        self.right=Node(0,None,self.left)
        self.left.nxt=self.right
        self.size=0
        self.capacity=k

        

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.size+=1
        temp=Node(value)
        left=self.right.prev
        left.nxt=temp
        self.right.prev=temp
        temp.prev=left
        temp.nxt=self.right
        return True

        

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False

        self.size=self.size-1
        temp=self.left.nxt
        address=temp.nxt
        self.left.nxt=address
        address.prev=self.left
        return True
        

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.left.nxt.value
        

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.right.prev.value
        

    def isEmpty(self) -> bool:
        return self.size==0
        

    def isFull(self) -> bool:
        return self.size==self.capacity

        
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()