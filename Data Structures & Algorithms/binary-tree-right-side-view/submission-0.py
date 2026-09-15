# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        mat=[]
        q=deque([root])

        while q:
            mat.append(q[-1].val)
            length=len(q)
            for i in range(length):
                Node=q.popleft()
                if Node.left:
                    q.append(Node.left)
                if Node.right:
                    q.append(Node.right)
        return mat    
                