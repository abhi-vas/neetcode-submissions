# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:


        def preorder(root):
            if not root:
                return '#,'
            
            return f'{root.val},'+preorder(root.left)+preorder(root.right)
        return preorder(root)  
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:

        data_=data.split(',')
        self.i=0
        def rebuild(data_):
            if self.i<len(data_):
                if data_[self.i]=='#':
                    return None
                else:
                    root=TreeNode(int(data_[self.i]))
                self.i+=1
                root.left=rebuild(data_)
                self.i+=1
                root.right=rebuild(data_)
                return root
        return rebuild(data_)
        
            



        


