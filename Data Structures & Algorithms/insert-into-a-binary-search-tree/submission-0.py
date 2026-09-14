# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    
        Node=TreeNode(val)
        if not root:
            return Node
        parent=None
        def insert(root,val,parent):

            if not root:
                if val<parent.val:
                    parent.left=Node
                else:
                    parent.right=Node
                return
            if val<root.val:
                
                parent=root
                insert(root.left,val,parent)
            else:
                parent=root
                insert(root.right,val,parent)
                
        insert(root,val,parent)
        return root

        