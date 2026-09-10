class Node:

    def __init__(self,key,value,nxt=None,prev=None):
        self.key=key
        self.value=value
        self.nxt=nxt
        self.prev=prev

class LRUCache:

    def __init__(self, capacity: int):
        self.hash_map={}
        self.left=Node(-1,-1)
        self.right=Node(-1,-1,None,self.left)
        self.left.nxt=self.right
        self.size=0
        self.capacity=capacity
        return
    def get(self, key: int) -> int:
        if key in self.hash_map:
            temp=self.hash_map[key]
            value=temp.value
            left=temp.prev
            right=temp.nxt
            left.nxt= right
            right.prev=left
            last=self.right.prev
            self.right.prev=temp
            last.nxt=temp
            temp.prev=last
            temp.nxt=self.right
            return value

        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hash_map:
            temp=self.hash_map[key]
            left=temp.prev
            right=temp.nxt
            left.nxt= right
            right.prev=left
            last=self.right.prev
            self.right.prev=temp
            last.nxt=temp
            temp.prev=last
            temp.nxt=self.right
            temp.value=value
            return
        elif self.size<self.capacity:
            self.size=self.size+1
            temp = Node(key, value, self.right)
            self.hash_map[key]=temp
            last=self.right.prev
            self.right.prev=temp
            last.nxt=temp
            temp.prev=last
        
        elif self.size==self.capacity:
            remove=self.left.nxt
            remove.nxt.prev=self.left
            self.left.nxt=remove.nxt
            del self.hash_map[remove.key]
            del remove
            
            temp = Node(key, value, self.right)
            self.hash_map[key]=temp
            last=self.right.prev
            self.right.prev=temp
            last.nxt=temp
            temp.prev=last

        
        return