# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode()
        curr=dummy
        curr1=l1
        curr2=l2
        carry=0
    
        while curr1 or curr2  or carry:

            v1 = curr1.val if curr1 else 0
            v2 = curr2.val if curr2 else 0

            val= v1+v2+carry

            carry= val//10
            val=val%10
            curr.next=ListNode(val)
            curr=curr.next
            curr1 = curr1.next if curr1 else None
            curr2= curr2.next if curr2 else None
        
        return dummy.next


         


   
        
        
        
     

        



        