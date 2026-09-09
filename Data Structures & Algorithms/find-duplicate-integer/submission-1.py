class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        my_dict={}

        for num in nums:
            if my_dict.get(num,0)==1:
                return num
            else:
                my_dict[num]=1        