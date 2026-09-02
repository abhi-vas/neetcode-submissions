class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for token in tokens:

            if token=='+':
                x=stack.pop()
                y=stack.pop()
                z=int(x)+int(y)
                stack.append(z)
            
            elif token =='-':
                x=stack.pop()
                y=stack.pop()
                z=int(y)-int(x)
                stack.append(z)
            
            elif token=='*':
                x=stack.pop()
                y=stack.pop()
                z=int(x)*int(y)
                stack.append(z)
            
            elif token=='/':
                x=stack.pop()
                y=stack.pop()
            
                z=int(int(y)/int(x))
                stack.append(z)
            else:
                stack.append(token)
        return int(stack[-1])

        