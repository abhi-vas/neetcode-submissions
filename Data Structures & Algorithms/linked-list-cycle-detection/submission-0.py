# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        my_set=set()

        curr1=head

        while curr1:
            if curr1 in my_set:
                return True
            else:
                my_set.add(curr1)
                curr1=curr1.next
        return False
        