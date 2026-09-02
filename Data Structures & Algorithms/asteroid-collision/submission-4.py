class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]

        for ast in asteroids:

            while stack and stack[-1]>0 and ast<0:
                res=stack[-1] + ast 

                if res>0:
                    ast=0
                elif res<0:
                    stack.pop()
                elif res==0:
                    stack.pop()
                    ast=0
            if ast:
                stack.append(ast)
        return stack
        