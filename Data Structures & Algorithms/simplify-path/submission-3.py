class Solution:
    def simplifyPath(self, path: str) -> str:
        path_=path.split('/')
        stack=[]
        print(path_)
        for p in path_:
            
            if stack and p=='..' :
                stack.pop()
            elif p!='.' and p!='/' and p!='' and p!=' ' and p!= "..":
                
                stack.append(p)
                
                



        return '/'+ '/'.join(stack)


        