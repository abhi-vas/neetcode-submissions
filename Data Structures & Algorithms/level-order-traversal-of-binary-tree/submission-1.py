# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root :
            return []
        
        q=deque([(root,0)])
        mat=[[root.val]]
        level=0
        while q:

            Node,level=q.popleft()
            level+=1
            

            if Node.left:
                q.append((Node.left,level))
                if  level <len(mat):
                    mat[level].append(Node.left.val)
                else:
                    mat.append([])
                    mat[level].append(Node.left.val)
            
            if Node.right:
                q.append((Node.right,level))
                if level <len(mat):
                    mat[level].append(Node.right.val)
                else:
                    mat.append([])
                    mat[level].append(Node.right.val)
        
            

        return mat


