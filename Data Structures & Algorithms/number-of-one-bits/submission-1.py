class Solution:
    def hammingWeight(self, n: int) -> int:
        c=0
        bin_ =bin(n)[2:]
        bin_=str(bin_)
        for i in bin_:
            if i=='1':
                c=c+1
        return c

        