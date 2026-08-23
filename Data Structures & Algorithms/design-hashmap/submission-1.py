class Node:
    def __init__(self,key=None,value=None):
        self.key=key
        self.value=value
        self.next=None
class MyHashMap:

    def __init__(self):
        self.map=[Node(None,None) for j in range(100)]
        self.len=len(self.map)
        

    def put(self, key: int, value: int) -> None:
        index=key%self.len
        head=self.map[index]
        curr=head
        if head.key==None:
            head.key=key
            head.value=value
            return
        if head.key==key:
            head.value=value
            return
        while curr.next!=None:
            if curr.next.key==key:
                curr.next.value=value
                return
            curr=curr.next
        curr.next=Node(key,value)

    def get(self, key: int) -> int:
        index=key%self.len
        head=self.map[index]
        curr=head
        if head.key==None:
            return -1
        if head.key==key:
            return head.value
        while curr.next!=None:
            if curr.next.key==key:
                return curr.next.value
            curr=curr.next
        return -1

    def remove(self, key: int) -> None:
        index=key%self.len
        head=self.map[index]
        curr=head
        if head.key==None:
            return 
        if head.key==key:
            if head.next!=None:
                self.map[index]=head.next
                return
            else:
                self.map[index]=Node(None,None)
            
        while curr.next!=None:
            if curr.next.key==key:
                curr.next=curr.next.next
                return 
            curr=curr.next
        return 

        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)