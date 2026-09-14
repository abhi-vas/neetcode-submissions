# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        


        def preorder(root):
            if not root:
                return '#'
            
            return  f'{root.val}{preorder(root.left)}{preorder(root.right)}'


        val1=preorder(root)
        val2=preorder(subRoot)

        return val2 in val1
