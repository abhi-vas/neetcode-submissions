# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        total=0
        curr=head
    
        while curr:
            total=total+1
            curr=curr.next

        elem_back=(total-1)//2
        elem_front=total-elem_back

        elem_back_address=[]
        i=0
        curr=head
    
        while curr:
            if i==elem_front-1:
                nxt=curr.next
                curr.next=None
                curr=nxt

            elif i>elem_front-1:
                elem_back_address.append(curr)
                curr=curr.next
            else:
                curr=curr.next
            i=i+1
        

        curr=head
        while elem_back_address:
            first=curr
            second=curr.next
            insert=elem_back_address.pop()
            first.next=insert
            insert.next=second
            curr=second
            
        
            
            
        
        





        