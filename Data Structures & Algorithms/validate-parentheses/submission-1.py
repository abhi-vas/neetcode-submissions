class Solution:
    def isValid(self, s: str) -> bool:

        # rules to pop

        stack=[]

        def stack_pop(stack_top ,new):

            my_dict= {'(': ')',
             '{': '}', '[':']'}

            if my_dict.get(stack_top,'')== new:
                return True
            else:
                    return False

        for i in s:

            if stack==[]:
                stack.append(i)
            
            elif stack_pop(stack[-1],i):
                stack.pop()
            else:
                stack.append(i)

        if stack==[]:
            return True
        else:
            return False
       

        