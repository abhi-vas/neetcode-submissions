# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        self.flag=True

        def issame(p,q):
            if p and not q:
                self.flag=False
                return
            if q and not p:
                self.flag=False
                return
            if not p and not q:
                return 

            if p.val!=q.val:
                self.flag=False
                return 

            issame(p.left,q.left)
            issame(p.right,q.right)

            return

        issame(p,q)
        return self.flag
            
        