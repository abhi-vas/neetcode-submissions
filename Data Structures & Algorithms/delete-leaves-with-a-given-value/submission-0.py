# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        
        def isleaf_and_target(root,target):

            if root.val==target and root.left==None and root.right==None:
                return True
            else:
                return False


        def dfs(root,target):

            if not root:
                return

            root.left=dfs(root.left,target)
            root.right=dfs(root.right,target)
            if isleaf_and_target(root,target):
                return None
            return root

        return dfs(root,target)