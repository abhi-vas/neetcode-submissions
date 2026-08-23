class Node:
    def __init__(self,key=None):
        self.key=key
        self.next=None


class MyHashSet:

    def __init__(self):
        self.set=[Node(None) for j in range(10000)]
        self.len=len(self.set)
        

    def add(self, key: int) -> None:
        index=key%self.len
        head=self.set[index]
        if head.key==None:
            head.key=key
            return
        if head.key==key:
            return
        curr=head
        while curr.next!=None:
            if curr.next.key==key:
                return
            curr=curr.next
        curr.next=Node(key)
   

    def remove(self, key: int) -> None:
        index=key%self.len
        head=self.set[index]
        curr=head
        if head.key==key:
            if head.next!=None:
                self.set[index]=head.next
                return 
            else:
                self.set[index]=Node(None)
                return 

            
        while curr.next!=None:
            if curr.next.key==key:
                curr.next=curr.next.next
                return
            curr=curr.next


    def contains(self, key: int) -> bool:
        index=key%self.len
        head=self.set[index]
        curr=head
        if head.key==key:
            return True
            
            
        while curr.next!=None:
            if curr.next.key==key:
                return True
            curr=curr.next
        return False
        
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)