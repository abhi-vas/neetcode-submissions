# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        curr=head
        total=0
        while curr:
            total=total+1
            curr=curr.next
        no_reverse=total//k

        def reverse(head,k,ref):
            prev=None
            curr=head
            while k:
                next=curr.next
                prev,curr.next=curr,prev
                curr=next
                k=k-1
            last=ref.next
            ref.next=prev
            
            last.next=curr
            ref=last
            return ref,curr
        
        dummy=ListNode(-1,head)
        ref=dummy
        for _ in range(no_reverse):
        
            ref,head=reverse(head,k,ref)
        return dummy.next
            


    


        



        



        