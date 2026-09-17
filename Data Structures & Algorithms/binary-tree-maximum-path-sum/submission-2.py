# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        self.max_value=-10001

        def dfs(root):
            if not root:
                return 0

            val1=dfs(root.left)
            val2=dfs(root.right)
            if val1 <0:
                val1=0
            if val2<0:
                val2=0

            val=root.val+val1+val2

            self.max_value=max(self.max_value,val)

            return max(root.val+val1, root.val+val2)

        dfs(root)

        return self.max_value