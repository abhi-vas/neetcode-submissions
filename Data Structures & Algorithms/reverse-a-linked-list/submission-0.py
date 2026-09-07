# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head:
            curr=head
            prev=None
            while curr:
                forward=curr.next
                prev,curr.next=curr,prev
                curr=forward
            head=prev
        return head