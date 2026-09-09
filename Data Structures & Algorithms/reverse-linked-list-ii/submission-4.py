# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        pleft=dummy
        curr=head

        for _ in range(left-1):
            pleft=curr
            curr=curr.next  
        prev=None
        for _ in range(right - left +1):
            nxt=curr.next
            prev,curr.next=curr,prev
            curr=nxt
        pleft.next.next=curr
        pleft.next=prev

        return dummy.next
