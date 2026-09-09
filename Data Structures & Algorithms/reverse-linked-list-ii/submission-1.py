# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        dummy=ListNode(0,head)
        curr=dummy
        i=0
        while curr:
            if (i+1)==left:
                start=curr
                prev=None
                imp=curr.next
                curr=curr.next
                i=i+1
                while i!=right:
                    nxt=curr.next
                    prev,curr.next=curr,prev
                    curr=nxt
                    i=i+1
                nxt=curr.next
                prev,curr.next=curr,prev
                curr=nxt
                start.next=prev
                imp.next=curr
                break
            curr=curr.next
            i=i+1
        return dummy.next







                

        