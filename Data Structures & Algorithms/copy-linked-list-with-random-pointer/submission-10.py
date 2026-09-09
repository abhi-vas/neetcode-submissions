"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr=head
        my_map={}

        while curr:
            new_node=Node(curr.val)
            my_map[curr]=new_node
            curr=curr.next
        curr=head
        while curr:
            new_node=my_map[curr]
            new_node.next=my_map.get(curr.next,None)
            new_node.random=my_map.get(curr.random,None)
            curr=curr.next
        
        return my_map.get(head,None)