# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        
            mat1=[]
            mat2=[]
            def path(root,node,mat):

                if not root:
                    return 

                if node.val==root.val:
                    mat.append(root)
                    return
                elif node.val < root.val:
                    mat.append(root)
                    path(root.left,node,mat)
                
                else:
                    mat.append(root)
                    path(root.right,node,mat)

            path(root,q,mat1)
            path(root,p,mat2)

            if len(mat1) > len(mat2):
                mat1,mat2=mat2,mat1
            for i in range(len(mat2)-len(mat1)):
                mat1.extend([None])
            i=0
            for i in range(len(mat2)):
                if  mat1[i]!=mat2[i]:
                    break
            return mat2[i-1]


            
            





        

        
             
        