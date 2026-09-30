class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
         
        my_dict={}
        for k,i in enumerate(range(2,7)):
            my_dict[str(i)]=[chr(ord('a')+k*3+j) for j in range(3)]
    

        for k,i in enumerate(range(7,10)):
            my_dict[str(i)]=[chr(ord('p')+k*4+j) for j in range(4)]
        

        my_dict['8'].pop()
        my_dict['9'].insert(0,'w')
        my_dict['9'].pop()

        res=[]
        subset=[]

        def comb(i):
            if i==len(digits):
                res.append(''.join(subset))
                return

            lst=my_dict[digits[i]]

            for j in lst:
                subset.append(j)
                comb(i+1)
                subset.pop()
        if digits:
            comb(0)
        return res
