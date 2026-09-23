class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perm=[[]]

        for n in nums:
            perm_new=[]

            for p in perm:
                for i in range(len(p)+1):
                    p_copy=p.copy()
                    p_copy.insert(i,n)
                    perm_new.append(p_copy)
            perm=perm_new
        return perm