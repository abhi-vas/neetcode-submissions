# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if len(lists)==0:
            return 

        
    

        
        def merge_and_sort(left,right):
            dummy=ListNode(-1)
            curr1=left
            curr2=right
            prev=dummy
            while curr1 and curr2:
                if curr1.val<curr2.val:
                    prev.next=curr1
                    prev=curr1
                    curr1=curr1.next
                else:
                    prev.next=curr2
                    prev=curr2
                    curr2=curr2.next


            if curr1:
                prev.next=curr1

            if curr2:
                prev.next=curr2
            to_return=dummy.next
            del dummy
            return to_return



        def divide(lists,l,r):
            if l==r:
                return lists[l]
            m=(l+r)//2
            left=divide(lists,l,m)
            right=divide(lists,m+1,r)
            return merge_and_sort(left,right)
        
        
        l=0
        r=len(lists)-1

        return divide(lists,l,r)



        