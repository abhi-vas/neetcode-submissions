class Solution:
    def simplifyPath(self, path: str) -> str:
        path_=path.split('/')
        stack=[]
        stack.append('/')
        print(path_)
        for p in path_:
            
            if p=='..' and len(stack)>2:
                stack.pop()
                stack.pop()
            elif p!='.' and p!='/' and p!='' and p!=' ' and p!= "..":
                
                stack.append(p)
                stack.append('/')
                
                


        if stack[-1]=='/' and len(stack)>1:
            stack.pop()
        return ''.join(stack)


        