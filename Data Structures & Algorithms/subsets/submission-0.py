class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        result=[]

        def sub(i,result):
            if i==len(nums):
                return [result]
            
            with_=sub(i+1,result+[nums[i]])
            without=sub(i+1,result)
            return with_+without

        return sub(0,result)
        