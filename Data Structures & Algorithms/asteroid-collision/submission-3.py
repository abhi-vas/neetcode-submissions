class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        stack=[]

        def recurse(stack,ast):
            
            b=ast
            if stack:
                a=stack[-1]
                if (a>0) and (b<0):
                    
                    if abs(a)==abs(b):
                        stack.pop()
                        return
                    if abs(a)<abs(b):
                        stack.pop()
                        recurse(stack,b)
                        return
                    if abs(a)>abs(b):
                        return
                else:
                        stack.append(b)
                        return 
            else:
                stack.append(b)
                return

        for ast in asteroids:
            
            recurse(stack,ast)
            
            
        return stack

                    
                 
        