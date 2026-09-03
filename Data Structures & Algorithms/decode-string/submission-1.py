class Solution:
    def decodeString(self, s: str) -> str:

        stack=[]
        i=0
        while i <len(s):
            
            if s[i]==']':
                res=''
                while stack and not (stack[-1].isdigit()):
                    if stack[-1]!='[':
                        res=stack.pop()+res
                    else:
                        stack.pop()
        
                y=int(stack.pop())
                res=y*res
                stack.append(res)
            
            
            else:
                if s[i].isdigit():
                    digit=''
                    while s[i]!='[':
                        digit=digit+s[i]
                        i=i+1
                    stack.append(digit)
                stack.append(s[i])
                    
            i=i+1
            
        return ''.join(stack)





        