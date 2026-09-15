# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        

        def dfs(root,maxvalue):
            if not root:
                return 0

            res = 1 if root.val>=maxvalue else 0 
            maxvalue=max(root.val,maxvalue)
            res+=dfs(root.left,maxvalue)
            res+=dfs(root.right,maxvalue)

            return res

        return dfs(root,root.val)
                
