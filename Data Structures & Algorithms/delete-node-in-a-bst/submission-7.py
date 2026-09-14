# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        dummy=TreeNode(-100001)
        dummy.left=root


        def isleaf(root):
            if root.left==None and root.right==None:
                return True
            return False
        def isonlyleft(root):
            if root.left!=None and root.right==None:
                return True
            return False
        def isonlyright(root):
            if root.left==None and root.right!=None:
                return True
            return False

        def min_element(root):

            while  root and  root.left:
                root=root.left
            return root


        def delete(root,key):

            if not root:
                return 

            if root.val==key:
                if isleaf(root):
        
                    return None
                elif isonlyleft(root):
                    node=root.left
                    return node
                elif isonlyright(root):
                    node=root.right
                    return node
                else:
                    replace_root=min_element(root.right)
                    replace_root.left,replace_root.right = root.left,delete(root.right,replace_root.val)
        
                    return replace_root



            elif key < root.val:
                root.left=delete(root.left,key)

            else:
                root.right=delete(root.right,key)
            return root

        dummy.left=delete(dummy.left,key)
        return dummy.left


            