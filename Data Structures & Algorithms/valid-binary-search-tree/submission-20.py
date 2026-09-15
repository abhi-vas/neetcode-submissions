# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.prev_value=float('-inf')
        self.flag=True
        def inordertraversal(root):
            if not root:
                return
            inordertraversal(root.left)
            if self.prev_value>=root.val:
                self.flag=False
                return
            self.prev_value=root.val
            inordertraversal(root.right)

        inordertraversal(root)
        return self.flag

     