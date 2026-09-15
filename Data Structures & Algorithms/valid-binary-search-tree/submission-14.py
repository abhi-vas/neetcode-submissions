# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        mat=[]
        def inordertraversal(root):
            if not root:
                return
            inordertraversal(root.left)
            mat.append(root.val)
            inordertraversal(root.right)

        inordertraversal(root)

        for i in range(1,len(mat)):
            if mat[i]<=mat[i-1]:
                return False
        return True