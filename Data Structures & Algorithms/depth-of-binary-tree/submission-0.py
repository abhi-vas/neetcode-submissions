# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        

        def checker(root):
            if not root:
                return 0
            depth=max(checker(root.left),checker(root.right)) + 1
            return depth

        return checker(root)
        