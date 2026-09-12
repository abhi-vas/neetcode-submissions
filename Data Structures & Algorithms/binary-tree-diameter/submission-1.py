# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
       
        def height(root):
            if not root:
                return 0
            h=1+max(height(root.left),height(root.right))
            return h
        def diameter(root):
            if not root:
                return 0
            dia=(max((height(root.left)+height(root.right)),
            diameter(root.left),diameter(root.right))
            )
            return dia
        return diameter(root)