# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.res=None
        self.capacity=k
        self.k=1


        def kthsmall(root):
            if not root:
                return 
            kthsmall(root.left)
            if self.res != None:
                return
            
            if (self.capacity==self.k):
                self.res=root.val
                return            
               
            self.k=self.k+1
            kthsmall(root.right)

        kthsmall(root)
        return self.res 