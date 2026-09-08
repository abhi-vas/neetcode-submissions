# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # identify mid

        slow , fast =head , head

        while fast and fast.next:

            slow=slow.next
            fast=fast.next.next
        # reversing second half

        prev=None
        traverse=slow.next
        slow.next=None
        while traverse:
            nxt=traverse.next
            prev,traverse.next=traverse,prev
            traverse=nxt

        # merging
        curr=head

        while prev:
            first=curr
            insert=prev
            second=curr.next
            prev=prev.next
            first.next=insert
            insert.next=second
            curr=second
            
