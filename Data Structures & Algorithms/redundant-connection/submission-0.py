
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        class union_find:

            def __init__(self,n):
                self.parent =list(range(n))
                self.size=[1]*n

            def find(self,x):
                while self.parent[x]!=x:
                    self.parent[x]=self.parent[self.parent[x]]
                    x=self.parent[x]
                return x

            def union(self,a,b):
                parent_a=self.find(a)
                parent_b=self.find(b)

                if parent_a==parent_b:
                    return True

                if self.size[parent_a]< self.size[parent_b]:
                    parent_a,parent_b=parent_b,parent_a
                self.parent[parent_b]=parent_a
                self.size[parent_a]+=self.size[parent_b] 
                return False 

        u=union_find(len(edges))
        for a,b in edges:
            if u.union(a-1,b-1):
                return [a,b]

                
