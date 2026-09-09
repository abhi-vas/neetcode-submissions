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
        dummy= Node(0)
        new_curr=dummy

        curr=head
        my_dict={}
        #address={}
        i=0
        while curr:
            val=curr.val
            #my_dict[curr]=i
            new_node=Node(val)
            #address[i]=new_node
            my_dict[curr]=new_node
            new_curr.next=new_node
            new_curr=new_node
            curr=curr.next
            i=i+1

        head2=dummy.next
        del dummy
        curr2= head2

        curr=head
        while curr:
            idx=my_dict.get(curr.random,None)
            if idx!=None:
                #curr2.random=address[idx]
                curr2.random=idx
            curr=curr.next
            curr2=curr2.next
        return head2



                


        
    
        
       


        